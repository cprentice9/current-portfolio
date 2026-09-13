"""Everything written on the page."""

NAME = "Connor Prentice"
TAGLINE = "Django developer and full stack software engineer in Denton, Texas."
PORTRAIT = "https://avatars.githubusercontent.com/u/60930043?v=4"

ABOUT = [
    "I am a Django developer. Most of my working hours go into one Django "
    "project, the site behind DKM Artists, where I own the models, the admin "
    "pages, the deploys, and the parts of the front end that nobody else "
    "wants to touch. Python is the language I think in. Flask is what I reach "
    "for when a thing needs to be small.",
    "The other half of my work is agentic engineering: building with coding "
    "agents and building for them. I run Claude Code with subagents doing the "
    "searching and grunt work while the design stays in one session, and I "
    "write the hooks, skills, and working rules that keep those agents "
    "honest. Byname, below, came out of that: a way to give a subagent a "
    "name and call it back days later. I know where agents save time, where "
    "they lie, and how to set up a review that catches the second before it "
    "ships.",
    "I have been writing code for a living since 2012, first on the front "
    "end and on white-label software for the company that became DKM, later "
    "on everything. Devmountain's web development program in 2022 filled in "
    "the parts I had taught myself around.",
    "In July 2026 I finished a history degree at the University of North "
    "Texas. It taught me to read closely, to care about where a source came "
    "from, and to write for someone who was not in the room. It still shows: "
    "I keep a library of primary sources with the translator and license as "
    "first-class fields, and I would rather write a commit message a "
    "stranger can read a year later than a clever one.",
    "Most importantly, I am a husband and a father, and that is the "
    "part of the day I would not trade. My favorite book series is The "
    "Stormlight Archive by Brandon Sanderson. I have read the whole run more "
    "than once and will argue about it if asked.",
]

PROJECTS = [
    {
        "title": "DKM Artists",
        "deck": "The Django site behind dkmartists.com. My main project.",
        "stack": "Django, PostgreSQL, Render",
        "repo": "https://github.com/cprentice9/song-submissions",
        "body": "Artists submit songs, A&R accounts pick from the catalog, and "
        "the DKM team runs shows, reviews, opportunities, and leaderboards "
        "from custom admin pages. In August 2026 I replaced the original Node "
        "app with one Django project: the rewrite kept every URL that "
        "mattered, moved the data across with a migration script, and "
        "deploys from main on Render. Before that I built the leaderboard "
        "and sign-up flow for the RNR Cup, a contest with more than 2,500 "
        "artists and celebrity judges.",
    },
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
]

LINKS = [
    ("GitHub", "https://github.com/cprentice9"),
    ("Email", "mailto:cprentice94@icloud.com"),
]
