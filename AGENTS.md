# AGENTS.md - Resume & Career Agent

## Overview
AI-powered resume and career assistance tool. CLI-based career agent that helps with job applications, cover letters, and interview prep.

## Tech Stack
- **Language:** Python 3
- **Dependencies:** See requirements.txt
- **AI Providers:** Multiple (see ai_providers.py)

## Commands
```bash
pip install -r requirements.txt    # Install dependencies
python main.py                     # Run the career agent
python cli.py                      # CLI interface
```

## Project Structure
```
main.py              # Entry point
cli.py               # CLI interface
career_agent.py      # Core career agent logic
ai_providers.py      # AI model provider integrations
config.py            # Configuration
document_parser.py   # Resume/document parsing
setup.sh             # Setup script
INTERVIEW_TIPS.md    # Interview preparation guide
Ian Alloway_CV.pdf   # Current CV
```

## Key Conventions
- AI provider abstraction layer for multiple model support
- Document parsing for resume analysis
- Cross-repo updates: When updating resume content, also update GitHub profile README (ianalloway/ianalloway) and portfolio website (ian-web-forge)

## Owner
Ian Alloway (@ianalloway) - Targeting AI / Data Science / Information Science roles.
