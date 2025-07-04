import os
from typing import Optional
from pydantic import Field
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class AgentConfig(BaseSettings):
    """Configuration settings for the Career Agent"""
    
    # AI Provider Settings
    openai_api_key: Optional[str] = Field(default=None, env="OPENAI_API_KEY")
    anthropic_api_key: Optional[str] = Field(default=None, env="ANTHROPIC_API_KEY")
    
    # Default AI provider (openai or anthropic)
    default_provider: str = Field(default="openai", env="DEFAULT_AI_PROVIDER")
    
    # Model settings
    openai_model: str = Field(default="gpt-4", env="OPENAI_MODEL")
    anthropic_model: str = Field(default="claude-3-sonnet-20240229", env="ANTHROPIC_MODEL")
    
    # Agent settings
    max_tokens: int = Field(default=4000, env="MAX_TOKENS")
    temperature: float = Field(default=0.7, env="TEMPERATURE")
    
    # File paths
    resume_path: str = Field(default="Ian Alloway_CV.pdf", env="RESUME_PATH")
    output_dir: str = Field(default="output", env="OUTPUT_DIR")
    
    class Config:
        env_file = ".env"
        case_sensitive = False

# Global config instance
config = AgentConfig()

def get_config() -> AgentConfig:
    """Get the global configuration instance"""
    return config