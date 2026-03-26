# Ian Alloway - Resume & Career Tools

**AI/ML Engineer | Data Scientist | Business Intelligence Specialist**

[![Download Resume (PDF)](https://img.shields.io/badge/Download-Resume%20(PDF)-blue?style=for-the-badge&logo=adobe-acrobat-reader)](https://github.com/ianalloway/Resume/raw/main/Ian_Alloway_Resume_CV.pdf)
[![Portfolio](https://img.shields.io/badge/Portfolio-ianalloway.xyz-00D100?style=for-the-badge&logo=google-chrome&logoColor=white)](https://ianalloway.xyz)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ianit)

---

## About Me

ML Engineer and Data Scientist completing a B.S. in Information Science at the University of South Florida in May 2026 and starting an M.S. in Artificial Intelligence in August 2026. Builds production ML systems, analytics tooling, and AI-powered products. Founder of Alloway LLC, delivering data-driven solutions across sports analytics, fintech, and cybersecurity. Proven track record of reducing fraud incidents by 30% through AI-based anomaly detection and improving client operational efficiency by 40%.

**Key Skills:** Python, TensorFlow, PyTorch, Scikit-learn, XGBoost, Deep Learning, NLP, Computer Vision, YOLOv8, SQL, PostgreSQL, Pandas, NumPy, Tableau, Power BI, Docker, AWS, React, TypeScript, FastAPI, Ethereum, Solidity, MAVLink

## Open Source Contributions

- **[OpenClaw](https://github.com/openclaw/openclaw)** - Active contributor to the 194k+ star AI agent framework. Bug fixes, skill system improvements, and published 4 skills to ClawHub: sports-odds, nft-tracker, data-viz, screenshot-annotator
- **[ClawHub Skills](https://clawhub.ai)** - Published 4 AI agent skills to the marketplace
- **[repo-health](https://github.com/ianalloway/repo-health)** - CLI that scores repository quality across README, CI, licensing, maintenance, and staleness indicators

## Projects

- **[AI Advantage Sports](https://aiadvantagesports.com)** - Sports betting platform with integrated XGBoost ML predictions, Kelly Criterion bet sizing, and value bet detection for NBA games. Model achieved 68% prediction accuracy. (React, Python, XGBoost)
- **[repo-health](https://github.com/ianalloway/repo-health)** - CLI that scores repository quality across README, CI, licensing, and maintenance indicators. (Python, CLI)
- **[nba-clv-dashboard](https://github.com/ianalloway/nba-clv-dashboard)** - FastAPI + Chart.js dashboard for calibration, rolling accuracy, and CLV-style reporting. (FastAPI, JavaScript)
- **[Sports Betting ML](https://huggingface.co/spaces/ianalloway/sports-betting-ml)** - NBA game prediction model deployed on HuggingFace. XGBoost classifier with feature engineering on player stats, team metrics, and historical matchups. (Python, XGBoost, Streamlit)
- **[kelly-js](https://github.com/ianalloway/kelly-js)** - TypeScript package for Kelly sizing, odds conversion, and bankroll math. (TypeScript, npm)
- **[macOS Disk Cleanup](https://github.com/ianalloway/macos-disk-cleanup)** - Open-source Bash CLI for selective macOS cache cleanup (Homebrew, Go, Chrome, npm/pip, optional Docker/Xcode); documented algorithm, `--dry-run`, ShellCheck CI. (Bash, GitHub Actions)
- **[odds-drift-watch](https://github.com/ianalloway/odds-drift-watch)** - Webhook-based line-move monitoring with FastAPI and SQLite. (Python, FastAPI)
- **[nba-ratings](https://github.com/ianalloway/nba-ratings)** - Installable Elo, logistic win probability, and Kelly helpers for NBA-style models. (Python)
- **[backtest-report-gen](https://github.com/ianalloway/backtest-report-gen)** - Generate static HTML backtest reports from evaluation JSON. (Python, Reporting)
- **[nba-clv-dashboard](https://github.com/ianalloway/nba-clv-dashboard)** - FastAPI + Chart.js calibration / rolling accuracy / CLV demo dashboard. (FastAPI, JavaScript)
- **[metric-regression-gate](https://github.com/ianalloway/metric-regression-gate)** - GitHub Action for blocking metric regressions in CI. (GitHub Actions, MLOps)
- **[code-stash](https://github.com/ianalloway/code-stash)** - SQLite-backed snippet manager with local LLM search. (Python, Developer Tools)
- **[repo-health](https://github.com/ianalloway/repo-health)** - Scores repo quality across README, licensing, CI, and staleness signals. (Python, CLI)

## Certifications

- **Deep Learning Specialization** - Coursera (Andrew Ng)
- **Machine Learning Engineering** - Google Cloud
- **AWS Certified Cloud Practitioner** - Amazon Web Services
- **Blockchain Fundamentals** - UC Berkeley Extension
- **Tableau Desktop Certified Professional** - Tableau / Salesforce
- **Oracle Database SQL Certified Associate** - Oracle

## Education

- **M.S. Artificial Intelligence (MSAI)** - University of South Florida (Starting August 2026)
- **B.S. Information Science** - University of South Florida (Expected May 2026)
- **Diploma, Hospitality Management** - Commonwealth University (June 2022)

## Writing

**[Alloway AI (Substack)](https://allowayai.substack.com)** - Technical writing on ML model development, AI agent architecture, and sports analytics.

---

## Career Agent Tool

An AI-powered career assistance tool that helps you optimize your resume, prepare for interviews, get career advice, and accelerate your professional growth. Built with modular architecture supporting multiple AI providers (OpenAI and Anthropic).

## ✨ Features

- **📊 Resume Analysis**: Comprehensive analysis with improvement suggestions
- **💡 Career Advice**: Personalized guidance based on your background
- **🎯 Job Optimization**: Tailor your resume for specific job opportunities
- **✉️ Cover Letter Generation**: Create compelling, customized cover letters
- **🎤 Interview Preparation**: Generate likely questions and strategic answers
- **📚 Skill Development**: Get recommendations for career advancement
- **🔄 Interactive Mode**: User-friendly CLI with rich formatting
- **🌐 Multi-Provider Support**: Choose between OpenAI GPT-4 or Anthropic Claude
- **💾 Export Capabilities**: Save all outputs to formatted files

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- API key from OpenAI or Anthropic (or both)

### Setup

1. **Clone or download the project**
   ```bash
   git clone <repository-url>  # or download files
   cd career-agent
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   ```bash
   cp env.example .env
   # Edit .env with your API keys and preferences
   ```

4. **Set up your API keys**
   
   Get an API key from at least one provider:
   - **OpenAI**: [platform.openai.com](https://platform.openai.com)
   - **Anthropic**: [console.anthropic.com](https://console.anthropic.com)
   
   Add your key(s) to the `.env` file:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   # or
   ANTHROPIC_API_KEY=your_anthropic_api_key_here
   ```

## 🚀 Quick Start

### Interactive Mode (Recommended)
Start the interactive mode for the best experience:
```bash
python cli.py interactive
```

### Command Line Usage

**Analyze your resume:**
```bash
python cli.py analyze --detailed --save
```

**Get career advice:**
```bash
python cli.py advice "How can I transition into data science?" --save
```

**Optimize resume for a job:**
```bash
python cli.py optimize --save
# Then paste the job description when prompted
```

**Generate a cover letter:**
```bash
python cli.py cover-letter --company "TechCorp" --save
# Then paste the job description when prompted
```

**Prepare for interviews:**
```bash
python cli.py interview --type technical --save
# Then paste the job description when prompted
```

**Get skill development suggestions:**
```bash
python cli.py skills --target-role "Senior Developer" --save
```

## 📋 Detailed Usage

### Resume Analysis
Analyzes your resume structure, content, ATS optimization, and provides improvement suggestions:
```bash
python cli.py analyze --resume-path path/to/resume.pdf --detailed
```

### Career Advice
Get personalized career guidance based on your background:
```bash
python cli.py advice "Should I pursue an MBA?" --context "I'm a software engineer with 5 years experience"
```

### Job Optimization
Tailor your resume for specific opportunities:
```bash
python cli.py optimize --job-file job_description.txt
```

### Cover Letter Generation
Create compelling cover letters:
```bash
python cli.py cover-letter --company "Google" --additional-info "I'm particularly interested in AI research"
```

### Interview Preparation
Prepare for different types of interviews:
```bash
python cli.py interview --type behavioral  # Options: general, technical, behavioral, panel
```

### Skill Development
Get recommendations for career growth:
```bash
python cli.py skills --target-role "Machine Learning Engineer"
```

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `OPENAI_API_KEY` | OpenAI API key | None |
| `ANTHROPIC_API_KEY` | Anthropic API key | None |
| `DEFAULT_AI_PROVIDER` | Default provider to use | `openai` |
| `OPENAI_MODEL` | OpenAI model to use | `gpt-4` |
| `ANTHROPIC_MODEL` | Anthropic model to use | `claude-3-sonnet-20240229` |
| `MAX_TOKENS` | Maximum tokens per response | `4000` |
| `TEMPERATURE` | AI creativity level (0-1) | `0.7` |
| `RESUME_PATH` | Default resume file path | `Ian Alloway_CV.pdf` |
| `OUTPUT_DIR` | Directory for saved outputs | `output` |

### Provider Selection
You can specify which AI provider to use:
```bash
python cli.py --provider anthropic analyze
python cli.py --provider openai advice "Career question here"
```

## 📁 Project Structure

```
career-agent/
├── career_agent.py      # Main agent class
├── ai_providers.py      # AI provider abstractions
├── document_parser.py   # Resume/document parsing
├── config.py           # Configuration management
├── cli.py              # Command-line interface
├── requirements.txt    # Python dependencies
├── env.example       # Environment template
├── output/            # Generated files (created automatically)
└── README.md          # This file
```

## 🤖 Supported AI Models

### OpenAI
- GPT-4 (recommended)
- GPT-3.5-turbo
- Custom models

### Anthropic
- Claude-3 Sonnet (recommended)
- Claude-3 Haiku
- Claude-2.1

## 📄 Supported Document Formats

- **PDF**: `.pdf` files
- **Word**: `.docx` files  
- **Text**: `.txt` and `.md` files

## 💡 Tips for Best Results

1. **Resume Quality**: Ensure your resume is well-formatted and contains complete information
2. **Specific Queries**: Be specific in your career advice questions
3. **Job Descriptions**: Provide complete job descriptions for optimization and interview prep
4. **Context**: Add relevant context to get more tailored advice
5. **Regular Updates**: Re-analyze your resume after making changes

## 🔒 Privacy & Security

- Your data is only sent to the selected AI provider (OpenAI or Anthropic)
- No data is stored on external servers beyond the AI provider's processing
- All outputs are saved locally on your machine
- Consider using environment variables for API keys (never commit them to version control)

## 🐛 Troubleshooting

### Common Issues

**"API key not found" error:**
- Check that your `.env` file exists and contains valid API keys
- Ensure the API key variable names match exactly

**"File not found" error:**
- Verify the resume file path in your `.env` file
- Use the `--resume-path` option to specify a different file

**"Model not available" error:**
- Check that you have access to the specified model
- Try switching to a different model in your configuration

**Dependencies issues:**
- Make sure all packages are installed: `pip install -r requirements.txt`
- Consider using a virtual environment

### Getting Help

1. Check the error message for specific guidance
2. Verify your API keys and configuration
3. Try using the interactive mode for easier troubleshooting
4. Ensure your resume file is accessible and in a supported format

## 🔮 Future Enhancements

- **Web Interface**: Browser-based UI for easier access
- **Job Search Integration**: Connect with job boards and applicant tracking systems
- **Networking Features**: LinkedIn integration and networking advice
- **Salary Negotiation**: Guidance for compensation discussions
- **Career Path Planning**: Long-term career roadmap generation
- **Industry Insights**: Real-time job market analysis
- **Skills Assessment**: Interactive skills evaluation

## 📜 License

This project is open source. Feel free to modify and adapt it for your needs.

## 🤝 Contributing

Contributions are welcome! Areas for improvement:
- Additional AI providers
- Enhanced document parsing
- New career guidance features
- UI/UX improvements
- Performance optimizations

---

**Happy job hunting! 🎯**
