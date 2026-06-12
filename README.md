# Ian Alloway - Resume & Career Tools

**Applied AI Engineer | Data Scientist | Evaluation-Driven Software and Agent App Builder**

[![Download Resume (PDF)](https://img.shields.io/badge/Download-Resume%20(PDF)-blue?style=for-the-badge&logo=adobe-acrobat-reader)](https://github.com/ianalloway/Resume/raw/main/Ian_Alloway_Resume_CV.pdf)
[![Portfolio](https://img.shields.io/badge/Portfolio-ianalloway.xyz-00D100?style=for-the-badge&logo=google-chrome&logoColor=white)](https://ianalloway.xyz)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ianit)

---

## About Me

Applied AI engineer and data scientist with a B.S. in Information Science from the University of South Florida, completed in May 2026, and an M.S. in Artificial Intelligence at USF in progress. I build evaluation-driven software, agent-developed apps, analytics workflows, and public-facing AI products. Founder of Alloway LLC, with work spanning AI evaluation, data auditing, predictive analytics, and decision-support systems. Proven track record of reducing fraud incidents by 30% through anomaly-detection workflows and improving client operational efficiency by 40%.

**Key Skills:** Python, SQL, TypeScript, JavaScript, R, FastAPI, React, Scikit-learn, XGBoost, PyTorch, TensorFlow, LLM-as-judge evaluation, prompt-injection testing, calibration, NLP, PostgreSQL, Pandas, NumPy, Tableau, Power BI, Docker, GitHub Actions, AWS

## Open Source Contributions

- **[juryrig](https://github.com/ianalloway/juryrig)** - Zero-dependency Python toolkit for auditing LLM judges across position bias, verbosity bias, prompt-injection susceptibility, self-consistency, panels, and calibration scoring
- **[OpenClaw](https://github.com/openclaw/openclaw)** - Contributor to the OpenClaw AI agent framework with bug fixes, skill system improvements, and published agent skills
- **[ClawHub Skills](https://clawhub.ai)** - Published AI agent skills focused on practical workflows and developer utility
- **[repo-health](https://github.com/ianalloway/repo-health)** - CLI that scores repository quality across README, CI, licensing, maintenance, and staleness indicators

## Projects

- **[juryrig](https://github.com/ianalloway/juryrig)** - Audit LLM-as-judge pipelines before trusting their scores: position bias, verbosity bias, prompt-injection susceptibility, self-consistency, judge panels, and calibration. Zero dependencies. (Python, AI evals)
- **[ian-web-forge](https://github.com/ianalloway/ian-web-forge)** - Recruiter-facing portfolio site and product surface for project proof, resume distribution, writing, and public case studies. (React, TypeScript)
- **[repo-health](https://github.com/ianalloway/repo-health)** - Repository-quality CLI for README quality, CI, licensing, maintenance, and staleness indicators. (Python, Developer Tools)
- **[AI Advantage Sports](https://aiadvantagesports.com)** - Public-facing ML product with integrated predictions, Kelly sizing, and workflow design that feels like a real application, not just a benchmark. (React, Python, XGBoost)
- **[kelly-js](https://github.com/ianalloway/kelly-js)** - TypeScript package for Kelly sizing, odds conversion, and bankroll math. (TypeScript, npm)
- **[nba-clv-dashboard](https://github.com/ianalloway/nba-clv-dashboard)** - FastAPI + Chart.js dashboard for calibration, rolling accuracy, and CLV-style reporting. (FastAPI, JavaScript)
- **[macOS Disk Cleanup](https://github.com/ianalloway/macos-disk-cleanup)** - Careful Bash CLI for selective macOS cache cleanup with documented safeguards and ShellCheck CI. (Bash, GitHub Actions)

## Certifications

- **Deep Learning Specialization** - Coursera (Andrew Ng)
- **Machine Learning Engineering** - Google Cloud
- **AWS Certified Cloud Practitioner** - Amazon Web Services
- **Blockchain Fundamentals** - UC Berkeley Extension
- **Tableau Desktop Certified Professional** - Tableau / Salesforce
- **Oracle Database SQL Certified Associate** - Oracle

## Education

- **M.S. Artificial Intelligence (MSAI)** - University of South Florida (In Progress)
- **B.S. Information Science** - University of South Florida (Completed May 2026)
- **Diploma, Hospitality Management** - Commonwealth University (June 2022)

## Writing

**[Alloway AI (Substack)](https://allowayai.substack.com)** - Technical writing on applied AI, model behavior, AI agent architecture, and evaluation-focused software.

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
| `RESUME_PATH` | Default resume file path | `Ian_Alloway_Resume_CV.pdf` |
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
