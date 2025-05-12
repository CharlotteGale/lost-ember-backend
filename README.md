# Lost Ember (Backend API)

The backend engine for **Lost Ember** — a narrative-driven, browser-based RPG focused on dynamic player state, branching logic, and modular storytelling.

## 🔧 Tech Stack
- **Python (3.11+)** for core application logic
- **Flask** for a lightweight, extensible RESTful API
- **PostgreSQL** for player data, branching narrative storage, and world-state
- **JSON-driven content** for flexible narrative modules
- **(Planned)** Integration with a standalone **Codex API** for world lore and system data

## 🧠 Core Responsibilities
- Serve **character data** and manage stat/skill progression
- Deliver **story blocks** via narrative node logic
- Maintain **event flags, inventory, and branching choices**
- Provide endpoints for **frontend UI integration**
- Future support for **combat logic, spellcasting, and Codex lookups**

## 🗺 Project Structure (WIP)
<pre>
lost-ember-backend/
├── README.md
├── requirements.txt
├── run.py
├── app/
│   ├── __init__.py
│   ├── routes/
│   │   ├── character.py
│   │   └── narrative.py
│   ├── models/
│   │   └── player.py
│   ├── utils/
│   │   └── parser.py
│   └── config/
│       └── db_config.py
└── db/
    ├── dnd_game.sql
    ├── classes.json
    ├── races.json
    ├── seed_classes.py
    └── seed_races.py

</pre>

## 🎮 Current Endpoints (Coming Soon)
- `POST /character/create` – Register a new character build
- `GET /story/start` – Begin story at selected intro node
- `POST /story/choice` – Submit a player decision, update world state
- `GET /codex/:entry` – Retrieve lore or game system reference

## ✍️ Development Notes
- Designed for **clean integration** with React frontend
- JSON-first structure allows for rapid prototyping and branching logic
- Will expand with:
  - **Session management**
  - **Combat resolution**
  - **Narrative triggers & world state tracking**

## 🚧 Status
**In scaffolding phase** — foundational routes and player schema are being implemented.

Upcoming tasks:
- Establish narrative loader from static or DB-based content
- Build player session model
- Begin testing integration with frontend character creation

## 📃 License
This is a personal project in private development.   
Public contributions may open post-alpha.
