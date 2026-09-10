# current-portfolio

A one-page portfolio set like a page from a book: paper texture across the whole page, EB Garamond, a drop cap, small-caps section heads. Flask serves it.

## Run it

```
python -m venv .venv
.venv/Scripts/pip install -r requirements.txt
.venv/Scripts/python app.py
```

Then open http://127.0.0.1:5000.

## Edit the page

All copy lives in `content.py`. Add a project by adding a dict to `PROJECTS`.

## Test

```
.venv/Scripts/pytest
```
