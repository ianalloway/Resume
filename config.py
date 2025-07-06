import os
from typing import Optional
from pydantic import Field
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class AgentConfig(BaseSettings):
    """Configuration settings for the Career Agent"""
    
    # AI Provider Settings
    openai_api_key: Optional[str] = Field(default=None)
    anthropic_api_key: Optional[str] = Field(default=None)
    
    # Default AI provider (openai or anthropic)
    default_provider: str = Field(default="openai")
    
    # Model settings
    openai_model: str = Field(default="gpt-4")
    anthropic_model: str = Field(default="claude-3-sonnet-20240229")
    
    # Agent settings
    max_tokens: int = Field(default=4000)
    temperature: float = Field(default=0.7)
    
    # File paths
    resume_path: str = Field(default="Ian Alloway_CV.pdf")
    output_dir: str = Field(default="output")
    
    model_config = {
        "env_file": ".env",
        "case_sensitive": False,
        "extra": "ignore"
    }

# Global config instance
config = AgentConfig()

def get_config() -> AgentConfig:
    """Get the global configuration instance"""
    return config