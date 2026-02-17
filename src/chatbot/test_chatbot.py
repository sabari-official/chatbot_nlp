#!/usr/bin/env python
"""
Test script for the Intelligent Chatbot
Tests all components to ensure the system is working correctly
"""

import os
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from dotenv import load_dotenv
from engine import NLPEngine
from ai_client import GeminiClient

def test_chatbot():
    """Test the chatbot with a sample query"""
    
    # Load environment variables
    env_path = Path(__file__).parent.parent.parent / '.env'
    load_dotenv(env_path)
    
    print("=" * 60)
    print("CHATBOT TEST SUITE")
    print("=" * 60)
    
    # Test 1: API Key
    print("\n[Test 1] API Key Configuration")
    api_key = os.getenv('GEMINI_API_KEY')
    if api_key and api_key != 'your_gemini_api_key_here':
        print("✓ API Key is configured")
    else:
        print("✗ API Key is missing or invalid")
        return False
    
    # Test 2: NLP Engine
    print("\n[Test 2] NLP Engine Initialization")
    try:
        nlp = NLPEngine()
        print("✓ NLP Engine initialized successfully")
    except Exception as e:
        print(f"✗ NLP Engine failed: {e}")
        return False
    
    # Test 3: Test NLP Analysis
    print("\n[Test 3] NLP Text Analysis")
    test_text = "Tell me about machine learning and artificial intelligence"
    try:
        context = nlp.get_structure(test_text)
        print(f"✓ Text analyzed successfully")
        print(f"  - Entities: {context['entities']}")
        print(f"  - Topics: {context['nouns']}")
        print(f"  - Verbs: {context['verbs']}")
    except Exception as e:
        print(f"✗ NLP Analysis failed: {e}")
        return False
    
    # Test 4: Gemini Client
    print("\n[Test 4] Gemini API Client Initialization")
    try:
        ai = GeminiClient()
        print(f"✓ Gemini Client initialized")
        print(f"  - Model: {ai.model_name}")
    except Exception as e:
        print(f"✗ Gemini Client failed: {e}")
        return False
    
    # Test 5: Generate Response
    print("\n[Test 5] AI Response Generation")
    try:
        test_query = "What is artificial intelligence?"
        context = nlp.get_structure(test_query)
        response = ai.ask(test_query, context)
        print(f"✓ Response generated successfully")
        print(f"\nQuery: {test_query}")
        print(f"Response: {response[:200]}..." if len(response) > 200 else f"Response: {response}")
    except Exception as e:
        print(f"✗ Response generation failed: {e}")
        return False
    
    print("\n" + "=" * 60)
    print("ALL TESTS PASSED ✓")
    print("=" * 60)
    print("\nThe chatbot is ready to use!")
    print("Run: python main.py")
    return True

if __name__ == "__main__":
    success = test_chatbot()
    sys.exit(0 if success else 1)
