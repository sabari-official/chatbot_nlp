import google.generativeai as genai
import os
from pathlib import Path
from dotenv import load_dotenv

# Ensure environment is loaded
env_path = Path(__file__).parent.parent.parent / '.env'
if env_path.exists():
    load_dotenv(env_path)

class GeminiClient:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key or api_key == "your_gemini_api_key_here":
            raise ValueError(
                "GEMINI_API_KEY not configured. Please set a valid API key in .env file.\n"
                "Get one from: https://aistudio.google.com/app/apikey"
            )
        genai.configure(api_key=api_key)
        
        # Get available models from API
        self.model_name = self._get_available_model()
        
        if not self.model_name:
            raise ValueError(
                "https://aistudio.google.com/app/apikey"
            )
        
        self.model = genai.GenerativeModel(self.model_name)
        # Initialize chat with a behavioral instruction
        self.chat = self.model.start_chat(history=[])
    
    def _get_available_model(self):
       
        try:
            # List all available models
            models = genai.list_models()
            
            # Filter for models that support generateContent
            available_models = []
            for model in models:
                if "generateContent" in model.supported_generation_methods:
                    model_name = model.name.replace("models/", "")
                    available_models.append(model_name)
            
            if available_models:
                selected_model = available_models[0]
                print(f"✓ Using model: {selected_model}")
                print(f"  (Available models: {', '.join(available_models[:3])})")
                return selected_model
            
            return None
        except Exception as e:
            print(f"Warning: Could not list models: {e}")
            # Fallback to gemini-pro
            print("✓ Using fallback model: gemini-pro")
            return "gemini-pro"

    def ask(self, query, context):
        
        try:
            # Create a dynamic prompt based on NLP structure
            dynamic_prompt = (
                f"User Query: {query}\n"
                f"Contextual Clues: Topics={context['nouns']}, Entities={context['entities']}\n"
                "Analyze these clues and provide a helpful, natural response."
            )
            response = self.chat.send_message(dynamic_prompt)
            return response.text
        except Exception as e:
            # Provide helpful error message
            error_msg = str(e)
            if "404" in error_msg or "not found" in error_msg.lower():
                raise Exception(
                    f"Model '{self.model_name}' not available with this API key.\n"
                    f"Error: {error_msg}\n"
                    "Please check your API key at: https://aistudio.google.com/app/apikey"
                )
            raise