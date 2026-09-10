from flask import Flask, abort, render_template, request

from content import BOOK_SUBTITLE, BOOK_TITLE, CHAPTERS, chapter_index


def create_app():
    app = Flask(__name__)

    @app.after_request
    def security_headers(response):
        response.headers["Content-Security-Policy"] = (
            "default-src 'self'; "
            "style-src 'self' https://fonts.googleapis.com; "
            "font-src https://fonts.gstatic.com; "
            "img-src 'self' data:"
        )
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["Referrer-Policy"] = "same-origin"
        return response

    def render_chapter(index):
        chapter = CHAPTERS[index]
        context = {
            "book_title": BOOK_TITLE,
            "book_subtitle": BOOK_SUBTITLE,
            "chapters": CHAPTERS,
            "chapter": chapter,
            "index": index,
            "prev": CHAPTERS[index - 1] if index > 0 else None,
            "next": CHAPTERS[index + 1] if index + 1 < len(CHAPTERS) else None,
            "folio": 2 * index - 1,
        }
        template = "spread.html" if request.args.get("fragment") else "book.html"
        return render_template(template, **context)

    @app.get("/")
    def cover():
        return render_chapter(0)

    @app.get("/<slug>")
    def chapter(slug):
        index = chapter_index(slug)
        if index is None:
            abort(404)
        return render_chapter(index)

    @app.errorhandler(404)
    def missing_page(_error):
        return render_template("404.html", book_title=BOOK_TITLE), 404

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
