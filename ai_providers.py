from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
import openai
import anthropic
from config import get_config

class AIProvider(ABC):
    """Abstract base class for AI providers"""
    
    @abstractmethod
    def generate_response(self, messages: List[Dict[str, str]], **kwargs) -> str:
        """Generate a response from the AI provider"""
        pass

class OpenAIProvider(AIProvider):
    """OpenAI provider implementation"""
    
    def __init__(self, api_key: Optional[str] = None):
        config = get_config()
        self.client = openai.OpenAI(api_key=api_key or config.openai_api_key)
        self.model = config.openai_model
        
    def generate_response(self, messages: List[Dict[str, str]], **kwargs) -> str:
        config = get_config()
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=kwargs.get('max_tokens', config.max_tokens),
                temperature=kwargs.get('temperature', config.temperature)
            )
            return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"OpenAI API error: {str(e)}")

class AnthropicProvider(AIProvider):
    """Anthropic provider implementation"""
    
    def __init__(self, api_key: Optional[str] = None):
        config = get_config()
        self.client = anthropic.Anthropic(api_key=api_key or config.anthropic_api_key)
        self.model = config.anthropic_model
        
    def generate_response(self, messages: List[Dict[str, str]], **kwargs) -> str:
        config = get_config()
        
        try:
            # Convert messages to Anthropic format
            system_message = ""
            user_messages = []
            
            for msg in messages:
                if msg["role"] == "system":
                    system_message = msg["content"]
                else:
                    user_messages.append(msg)
            
            response = self.client.messages.create(
                model=self.model,
                max_tokens=kwargs.get('max_tokens', config.max_tokens),
                temperature=kwargs.get('temperature', config.temperature),
                system=system_message,
                messages=user_messages
            )
            return response.content[0].text
        except Exception as e:
            raise Exception(f"Anthropic API error: {str(e)}")

class AIProviderFactory:
    """Factory for creating AI providers"""
    
    @staticmethod
    def create_provider(provider_name: Optional[str] = None) -> AIProvider:
        config = get_config()
        provider = provider_name or config.default_provider
        
        if provider.lower() == "openai":
            if not config.openai_api_key:
                raise ValueError("OpenAI API key not found. Please set OPENAI_API_KEY environment variable.")
            return OpenAIProvider()
        elif provider.lower() == "anthropic":
            if not config.anthropic_api_key:
                raise ValueError("Anthropic API key not found. Please set ANTHROPIC_API_KEY environment variable.")
            return AnthropicProvider()
        else:
            raise ValueError(f"Unsupported provider: {provider}")

def get_ai_provider(provider_name: Optional[str] = None) -> AIProvider:
    """Get an AI provider instance"""
    return AIProviderFactory.create_provider(provider_name)