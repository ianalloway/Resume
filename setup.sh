#!/bin/bash

echo "🚀 Setting up Career Agent..."

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "career_agent_env" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv career_agent_env
fi

# Activate virtual environment and install dependencies
echo "📥 Installing dependencies..."
source career_agent_env/bin/activate
pip install -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "⚙️ Creating configuration file..."
    cp .env.example .env
    echo "✅ Configuration file created at .env"
    echo "🔑 Please edit .env and add your API keys before using the agent."
fi

# Make scripts executable
chmod +x cli.py main.py

echo ""
echo "✅ Setup complete!"
echo ""
echo "🔧 Next steps:"
echo "1. Edit .env file and add your OpenAI or Anthropic API key"
echo "2. Run the agent with: source career_agent_env/bin/activate && python main.py --help"
echo "3. Try interactive mode: source career_agent_env/bin/activate && python main.py interactive"
echo ""
echo "📖 For detailed usage instructions, see README.md"