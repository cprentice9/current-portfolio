"""Everything written on the page."""

NAME = "Connor Prentice"
TAGLINE = "Software, mostly in Python, that I wanted for myself first."

ABOUT = [
    "I build small, useful software and I like it when the seams show. "
    "Most of what I make starts as a tool I wanted for myself: a name for "
    "an anonymous process, a citation I did not want to format by hand, a "
    "library of sources whose licenses I could trust.",
    "I work mostly in Python, with Flask and Django on the server and plain "
    "HTML, CSS, and JavaScript in front. When a problem calls for it I reach "
    "for PyTorch. I prefer the least code that fully solves the problem, and "
    "I would rather extend a pattern than invent one.",
    "Outside of shipping features I care about the parts of software that "
    "are easy to skip: tests that run against the real thing, pages that "
    "work without JavaScript, and commit messages a stranger can read a "
    "year later.",
]

PROJECTS = [
    {
        "title": "Byname",
        "deck": "Names for Claude Code subagents, and a way to call them back.",
        "stack": "Node, shell hooks, Claude Code skills",
        "repo": "https://github.com/cprentice9/byname",
        "body": "When Claude Code delegates work to a subagent, that agent is "
        "an anonymous hex id that vanishes when the session ends. Byname "
        "gives each one a human name, keeps a roster of who did what, and "
        "lets you say \"ask Otto to finish that\" days later and have Otto "
        "pick up where he left off. No database, just files you can read.",
    },
    {
        "title": "Growing neural cellular automata",
        "deck": "A CPU-only PyTorch reimplementation of the 2020 Distill paper.",
        "stack": "Python, PyTorch",
        "repo": "https://github.com/cprentice9/neural-cellular-automata",
        "body": "Each cell holds sixteen float channels and perceives its "
        "neighborhood through fixed identity and Sobel filters, then a small "
        "network decides how to update. A single emoji grows from one seed "
        "pixel and holds its shape after a few thousand steps on a laptop "
        "CPU. The repo ships checkpoints and an export script for the browser.",
    },
    {
        "title": "Primary source library",
        "deck": "A provenance-first library of primary sources for the classroom.",
        "stack": "Python, SQLite",
        "repo": "https://github.com/cprentice9/primary-source-library",
        "body": "An ancient text is public domain, but the translation you "
        "photocopy usually is not. So translator, translation year, and "
        "license code are first-class fields, not notes in a margin. A test "
        "suite checks that every record has a license a teacher can act on.",
    },
    {
        "title": "DKM Artists",
        "deck": "The site behind dkmartists.com, rebuilt from Node to Django.",
        "stack": "Django, PostgreSQL, Render",
        "repo": "https://github.com/cprentice9/song-submissions",
        "body": "Artists submit songs, A&R accounts pick from the catalog, and "
        "the DKM team runs shows, reviews, opportunities, and leaderboards "
        "from custom admin pages. The Django rewrite kept every URL that "
        "mattered, moved the data across with a migration script, and "
        "deploys from main on Render.",
    },
]

LINKS = [
    ("GitHub", "https://github.com/cprentice9"),
    ("Email", "mailto:cprentice94@icloud.com"),
]
