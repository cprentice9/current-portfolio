"""Every chapter of the book. Order here is reading order."""

BOOK_TITLE = "Connor Prentice"
BOOK_SUBTITLE = "A working portfolio"

CHAPTERS = [
    {
        "slug": "cover",
        "title": "Cover",
        "kind": "cover",
    },
    {
        "slug": "contents",
        "title": "Contents",
        "kind": "contents",
    },
    {
        "slug": "about",
        "title": "About the author",
        "kind": "prose",
        "left": [
            "I build small, useful software and I like it when the seams show. "
            "Most of what I make starts as a tool I wanted for myself: a name "
            "for an anonymous process, a citation I did not want to format by "
            "hand, a library of sources whose licenses I could trust.",
            "I work mostly in Python, with Flask and Django on the server and "
            "plain HTML, CSS, and JavaScript in front. When a problem calls for "
            "it I reach for PyTorch. I prefer the least code that fully solves "
            "the problem, and I would rather extend a pattern than invent one.",
        ],
        "right": [
            "Outside of shipping features I care about the parts of software "
            "that are easy to skip: tests that run against the real thing, "
            "pages that work without JavaScript, and commit messages a "
            "stranger can read a year later.",
            "This book collects the projects I am proudest of right now. Each "
            "one gets a spread. Turn the page to start, or use the contents "
            "to jump to a chapter.",
        ],
    },
    {
        "slug": "byname",
        "title": "Byname",
        "kind": "project",
        "deck": "Names for Claude Code subagents, and a way to call them back.",
        "stack": "Node, shell hooks, Claude Code skills",
        "repo": "https://github.com/cprentice9/byname",
        "left": [
            "When Claude Code delegates work to a subagent, that agent is an "
            "anonymous hex id that vanishes when the session ends. Byname "
            "gives each one a human name, keeps a roster of who did what, and "
            "lets you say \"ask Otto to finish that\" days later and have Otto "
            "pick up where he left off.",
        ],
        "right": [
            "The interesting part was the roster. Hooks capture each spawn and "
            "each result, and a skill teaches the main session how to look a "
            "name up and resume the right context. No database, just files "
            "you can read.",
        ],
    },
    {
        "slug": "neural-cellular-automata",
        "title": "Growing neural cellular automata",
        "kind": "project",
        "deck": "A CPU-only PyTorch reimplementation of the 2020 Distill paper.",
        "stack": "Python, PyTorch",
        "repo": "https://github.com/cprentice9/neural-cellular-automata",
        "left": [
            "Each cell holds sixteen float channels: RGB premultiplied by "
            "alpha, alpha itself, and twelve hidden channels. A cell perceives "
            "its three-by-three neighborhood through fixed identity and Sobel "
            "filters, then a small network decides how to update.",
        ],
        "right": [
            "Training a single emoji to grow from one seed pixel and then "
            "hold its shape takes a few thousand steps on a laptop CPU. The "
            "repo includes checkpoints and an export script that writes the "
            "trained model out for the browser.",
        ],
    },
    {
        "slug": "primary-source-library",
        "title": "Primary source library",
        "kind": "project",
        "deck": "A provenance-first library of primary sources for the classroom.",
        "stack": "Python, SQLite",
        "repo": "https://github.com/cprentice9/primary-source-library",
        "left": [
            "An ancient text is public domain, but the translation you "
            "photocopy usually is not. So translator, translation year, and "
            "license code are first-class fields in this library, not notes "
            "in a margin.",
        ],
        "right": [
            "The library ships as a SQLite file with a Python package around "
            "it and a test suite that checks every record has a license a "
            "teacher can act on. A packet builder that turns a selection into "
            "a handout is the next chapter.",
        ],
    },
    {
        "slug": "dkm-artists",
        "title": "DKM Artists",
        "kind": "project",
        "deck": "The site behind dkmartists.com, rebuilt from Node to Django.",
        "stack": "Django, PostgreSQL, Render",
        "repo": "https://github.com/cprentice9/song-submissions",
        "left": [
            "Artists submit songs, A&R accounts pick from the catalog, and "
            "the DKM team runs shows, reviews, opportunities, and leaderboards "
            "from custom admin pages.",
        ],
        "right": [
            "In August 2026 the Django site replaced the original Node app. "
            "The rewrite kept every URL that mattered, moved the data across "
            "with a migration script, and deploys from main on Render.",
        ],
    },
    {
        "slug": "contact",
        "title": "Colophon",
        "kind": "contact",
        "left": [
            "Set in EB Garamond. Served by Flask. The page turn is a single "
            "CSS transform and a fetch; the book reads fine with JavaScript "
            "off.",
        ],
        "right": [
            "If you want to talk about any of this, the addresses below reach me.",
        ],
        "links": [
            ("GitHub", "https://github.com/cprentice9"),
            ("Email", "mailto:cprentice94@icloud.com"),
        ],
    },
]


def chapter_index(slug):
    for i, chapter in enumerate(CHAPTERS):
        if chapter["slug"] == slug:
            return i
    return None
