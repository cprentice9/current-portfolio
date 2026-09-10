import pytest

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


def test_first_paragraph_gets_the_drop_cap(client):
    body = client.get("/").get_data(as_text=True)
    assert body.count('class="opener"') == 1


def test_unknown_path_is_404(client):
    assert client.get("/nope").status_code == 404


def test_security_headers(client):
    response = client.get("/")
    assert "default-src 'self'" in response.headers["Content-Security-Policy"]
    assert response.headers["X-Content-Type-Options"] == "nosniff"
