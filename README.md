# Ian Alloway - Resume & Career Tools

**Data Scientist | AI Specialist | Blockchain Analyst**

[![Download Resume](https://img.shields.io/badge/Download-Resume%20(PDF)-blue?style=for-the-badge&logo=adobe-acrobat-reader)](https://github.com/ianalloway/Resume/raw/main/Ian%20Alloway_CV.pdf)
[![Portfolio](https://img.shields.io/badge/Portfolio-ianalloway.xyz-00D100?style=for-the-badge&logo=google-chrome&logoColor=white)](https://ianalloway.xyz)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ianit)

---

## About Me

I'm pursuing a Masters in Artificial Intelligence at the University of South Florida while running Alloway LLC, where I specialize in AI-driven cybersecurity solutions and blockchain analytics. I transform complex datasets into actionable insights, bridging cutting-edge AI research with practical business applications.

**Key Skills:** Python, Machine Learning, TensorFlow, PyTorch, Deep Learning, NLP, SQL, Data Analytics, Blockchain, Power BI, Tableau

## Open Source Contributions

- **[OpenClaw](https://github.com/openclaw/openclaw)** - Active contributor to the 194k+ star AI agent framework
- **[ClawHub Skills](https://clawhub.ai)** - Published AI agent skills: sports-odds, nft-tracker, data-viz, screenshot-annotator
- **[Money Maker Bot](https://github.com/ianalloway/Money-maker-bot)** - Financial intelligence assistant built on OpenClaw

## Education

- **M.S. Artificial Intelligence** - University of South Florida (2024 - Present)
- **B.S. Information Science, Data Science and Analytics** - University of South Florida
- **A.S.** - Hillsborough Community College, Tampa

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
   cp .env.example .env
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
├── .env.example       # Environment template
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
