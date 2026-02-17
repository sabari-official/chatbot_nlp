# Intelligent Chatbot with NLP and Gemini AI

A sophisticated chatbot that combines Natural Language Processing (NLP) with Google's Gemini AI model to provide intelligent, context-aware responses.

## Features

- **NLP-Powered Analysis**: Uses spaCy for entity recognition, noun extraction, and verb identification
- **Google Gemini Integration**: Leverages Google's latest Gemini API for dynamic response generation
- **Context-Aware Responses**: Analyzes user input structure to provide contextually relevant answers
- **No Hardcoded Q&A**: Fully dynamic responses based on real AI inference
- **Interactive CLI**: Simple command-line interface for real-time conversations

## Project Structure

```
src/chatbot/
├── __init__.py           # Package initialization
├── main.py              # Entry point for the chatbot
├── config.py            # Configuration and constants
├── engine.py            # NLP engine using spaCy
├── ai_client.py         # Gemini AI client
```

## Requirements

- Python 3.8+
- spacy (for NLP)
- google-generativeai (for Gemini API)
- python-dotenv (for environment variables)

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the spaCy model:
   ```bash
   python -m spacy download en_core_web_md
   ```

4. Set up environment variables in `.env`:
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

## Usage

Run the chatbot:

```bash
python src/chatbot/main.py
```

Then interact with the bot by typing your messages. Type `exit` or `quit` to end the conversation.

## How It Works

1. **User Input**: User enters a query
2. **NLP Analysis**: The NLPEngine analyzes the input to extract:
   - Named entities (persons, places, organizations, etc.)
   - Noun chunks (relevant topics)
   - Verbs (actions being performed)
3. **Dynamic Prompt Generation**: The AI client creates a contextual prompt based on the analysis
4. **AI Response**: Gemini API generates a natural, context-aware response
5. **Output**: The bot displays the response to the user

## Configuration

Customize chatbot behavior by modifying:
- `config.py`: Model selection, API parameters, NLP settings
- `ai_client.py`: Gemini model selection and parameters
- `engine.py`: NLP processing pipeline

## API Keys

To use this chatbot, you need:
- **Google Gemini API Key**: Get it from [Google AI Studio](https://aistudio.google.com/app/apikey)

## Examples

```
You: What is the capital of France?
Bot: The capital of France is Paris, a major city located in north-central France...

You: Tell me about machine learning
Bot: Machine learning is a subset of artificial intelligence that enables systems...

You: What's the weather today?
Bot: I don't have real-time weather information, but I can help you with...
```

## License

MIT License

## Author

Codtech Technologies
