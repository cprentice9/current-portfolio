from urllib.parse import quote

import pytest
from markupsafe import escape

import content
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()


def test_page_renders_every_section(client):
    response = client.get("/")
    assert response.status_code == 200
    body = response.get_data(as_text=True)
    assert content.NAME in body
    for project in content.PROJECTS:
        assert project["title"] in body
        assert project["repo"] in body
    for _label, href in content.LINKS:
        assert href in body
    assert content.PRICING_NOTE in body
    for tier in content.PRICING:
        assert tier["title"] in body
        assert tier["price"] in body


def test_first_paragraph_gets_the_drop_cap(client):
    body = client.get("/").get_data(as_text=True)
    assert body.count('class="opener"') == 1


def test_unknown_path_is_404(client):
    assert client.get("/nope").status_code == 404


def test_security_headers(client):
    response = client.get("/")
    assert "default-src 'self'" in response.headers["Content-Security-Policy"]
    assert response.headers["X-Content-Type-Options"] == "nosniff"


def test_hiring_sections_render(client):
    body = client.get("/").get_data(as_text=True)
    texts = content.INCLUDED + content.NOT_INCLUDED
    for pair in content.PROCESS + content.FAQ:
        texts += list(pair)
    for text in texts:
        assert str(escape(text)) in body


def test_each_tier_has_an_email_link(client):
    body = client.get("/").get_data(as_text=True)
    for tier in content.PRICING:
        subject = quote("Website inquiry: " + tier["title"])
        assert f"mailto:{content.EMAIL}?subject={subject}&amp;body=" in body


def test_hire_link_lands_on_pricing(client):
    body = client.get("/").get_data(as_text=True)
    assert 'href="#pricing"' in body
    assert 'id="pricing"' in body


def test_colophon_renders_and_its_claims_hold(client):
    response = client.get("/")
    body = response.get_data(as_text=True)
    for para in content.COLOPHON:
        assert str(escape(para)) in body
    assert f'href="{content.SOURCE}"' in body
    assert "<script" not in body
    assert "Set-Cookie" not in response.headers
