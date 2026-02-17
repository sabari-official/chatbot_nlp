import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from engine import NLPEngine
from ai_client import GeminiClient
from config import Config

def run_bot():
    # Load environment variables from .env
    env_path = Path(__file__).parent.parent.parent / '.env'
    load_dotenv(env_path)
    
    # Validate API key
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key or api_key == 'your_gemini_api_key_here':
        print("❌ Error: GEMINI_API_KEY not found in .env file")
        print("Please set your Gemini API key in the .env file:")
        print("  GEMINI_API_KEY=your_actual_api_key")
        print("\nGet your API key from: https://aistudio.google.com/app/apikey")
        sys.exit(1)
    
    try:
        nlp = NLPEngine()
        ai = GeminiClient()
        
        print("🤖 Bot is live! (Type 'exit' to quit)")
        
        while True:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Goodbye!")
                break
                
            # 1. Structural Analysis (No hardcoded Q&A)
            context = nlp.get_structure(user_input)
            
            # 2. Get Dynamic Response
            reply = ai.ask(user_input, context)
            print(f"Bot: {reply}\n")
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        print("Please check your API key and try again")
        sys.exit(1)

if __name__ == "__main__":
    run_bot()