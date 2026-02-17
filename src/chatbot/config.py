import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
env_path = Path(__file__).parent.parent.parent / '.env'
if env_path.exists():
    load_dotenv(env_path)


class Config:
    
    # API Configuration
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
    GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")
    
    # NLP Configuration
    SPACY_MODEL = os.getenv("SPACY_MODEL", "en_core_web_md")
    
    # Chat Configuration
    MAX_HISTORY = int(os.getenv("MAX_HISTORY", "10"))
    TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))
    
    # Bot Configuration
    BOT_NAME = os.getenv("BOT_NAME", "🤖 Bot")
    WELCOME_MESSAGE = os.getenv(
        "WELCOME_MESSAGE",
        "🤖 Bot is live! (Type 'exit' to quit)"
    )
    
    # Exit commands
    EXIT_COMMANDS = ["exit", "quit", "bye", "goodbye", "q"]
    
    @classmethod
    def is_valid(cls):
        return bool(cls.GEMINI_API_KEY and cls.GEMINI_API_KEY != "your_gemini_api_key_here")
