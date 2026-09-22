from flask import Flask, render_template

import content


def create_app():
    app = Flask(__name__)

    @app.after_request
    def security_headers(response):
        response.headers["Content-Security-Policy"] = (
            "default-src 'self'; "
            "style-src 'self' https://fonts.googleapis.com; "
            "font-src https://fonts.gstatic.com; "
            "img-src 'self' https://avatars.githubusercontent.com"
        )
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["Referrer-Policy"] = "same-origin"
        return response

    @app.get("/")
    def index():
        return render_template(
            "index.html",
            name=content.NAME,
            tagline=content.TAGLINE,
            portrait=content.PORTRAIT,
            about=content.ABOUT,
            projects=content.PROJECTS,
            pricing_note=content.PRICING_NOTE,
            pricing=content.PRICING,
            links=content.LINKS,
        )

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
