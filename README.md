# EduMate AI – A Learning Assistant (Team DigiTech 5)

DCIT 313 Semester Project (Route C: Grounded Document Agent / RAG).

## Folder Structure
- `src/` : Document loader, retrieval agent, and quiz generator code
- `data/` : Approved open-licensed Database Management sample notes & data README
- `tests/` : Unit and edge-case tests
- `evaluation/` : Frozen benchmark queries and evaluation scripts
- `docs/` : Milestone 2 Proposal and architecture documentation
- `ai_use_log.md` : Transparent log of AI tools used and verification steps

## Quick Start (Verify Data Access)
1. Ensure Python 3.10+ is installed.
2. Run the data loader test:
   ```bash
   python src/data_loader.py
   python -m unittest discover -s tests -v
   ```
