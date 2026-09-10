# current-portfolio

A portfolio site that reads like a book. Flask serves one chapter per URL; the front end draws an open two-page spread with running heads, folios, and a page that turns when you follow a link.

## Run it

```
python -m venv .venv
.venv/Scripts/pip install -r requirements.txt
.venv/Scripts/python app.py
```

Then open http://127.0.0.1:5000.

## Edit the book

All copy lives in `content.py`. Each entry in `CHAPTERS` is one spread. Add a project by adding a dict with `kind: "project"`; the contents page and folios update on their own.

## Test

```
.venv/Scripts/pytest
```
