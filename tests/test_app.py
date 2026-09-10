import pytest

from app import create_app
from content import CHAPTERS


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()


def test_cover_is_the_closed_book(client):
    response = client.get("/")
    assert response.status_code == 200
    body = response.get_data(as_text=True)
    assert "kind-cover" in body
    assert "Open the book" in body


def test_every_chapter_renders_with_running_head_and_folios(client):
    for index, chapter in enumerate(CHAPTERS[1:], start=1):
        response = client.get(f"/{chapter['slug']}")
        assert response.status_code == 200, chapter["slug"]
        body = response.get_data(as_text=True)
        assert chapter["title"] in body
        assert f'<p class="folio">{2 * index - 1}</p>' in body
        assert f'<p class="folio">{2 * index}</p>' in body


def test_contents_folios_match_the_chapters(client):
    body = client.get("/contents").get_data(as_text=True)
    for index, chapter in enumerate(CHAPTERS):
        if chapter["kind"] in ("cover", "contents"):
            continue
        entry = f'href="/{chapter["slug"]}"'
        assert entry in body
        folio = 2 * index - 1
        assert f'<span class="toc-folio">{folio}</span>' in body


def test_fragment_returns_only_the_spread(client):
    body = client.get("/about?fragment=1").get_data(as_text=True)
    assert body.lstrip().startswith("<section")
    assert "<html" not in body


def test_prev_and_next_links(client):
    body = client.get("/about").get_data(as_text=True)
    assert 'href="/contents" rel="prev"' in body
    assert 'href="/byname" rel="next"' in body
    last = client.get("/contact").get_data(as_text=True)
    assert 'rel="next"' not in last
    cover = client.get("/").get_data(as_text=True)
    assert 'rel="prev"' not in cover


def test_missing_chapter_is_a_torn_page(client):
    response = client.get("/nope")
    assert response.status_code == 404
    assert "torn out" in response.get_data(as_text=True)


def test_security_headers(client):
    response = client.get("/")
    assert "default-src 'self'" in response.headers["Content-Security-Policy"]
    assert response.headers["X-Content-Type-Options"] == "nosniff"
