# Task - 3: AI Chatbot with NLP

**Intelligent Chatbot with Natural Language Processing and Google Gemini AI**

---

**Company**     : CODETECH IT SOLUTIONS

**Name**        : SABARIVASAN E

**Intern ID**   : CTIS3748

**Domain**      : PYTHON PROGRAMMING

**Duration**    : 4 WEEKS

**Mentor**      : NEELA SANTHOSH

---

## **PROJECT OVERVIEW**

This project implements an intelligent conversational chatbot that combines Natural Language Processing (spaCy) with Google's Gemini AI model for dynamic, context-aware responses. The application demonstrates advanced NLP techniques, API integration with modern generative AI, and interactive conversational design without relying on hardcoded Q&A pairs. Users can engage in natural conversations where the bot analyzes linguistic structure (entities, nouns, verbs) and leverages Gemini AI to generate contextually relevant, intelligent responses in real-time.

---

## **TASK TYPE PERFORMED**

1. **Natural Language Processing (NLP)** - spaCy-based text analysis: entity recognition (PERSON, ORG, LOCATION), noun chunk extraction, verb lemmatization, and structural understanding
2. **Generative AI Integration** - Google Gemini API client with dynamic model selection, automatic model discovery, and fallback handling
3. **Context-Aware Response Generation** - Analyzing user input structure to enrich prompts with contextual clues (topics, entities, keywords)
4. **Environment Configuration** - Secure API key management using python-dotenv with validation and error handling
5. **Interactive CLI Development** - Real-time conversational interface with graceful error handling and user-friendly feedback

---

## **TOOLS AND RESOURCES USED**

| **Category** | **Tools & Technologies** |
|-------------|--------------------------|
| **Language** | Python 3.8+ |
| **NLP Framework** | spaCy (v3.7.2) with en_core_web_md model |
| **Generative AI** | Google Generative AI (google-generativeai v0.3.0) |
| **AI Model** | Google Gemini (auto-detected from available models) |
| **Configuration** | python-dotenv (v1.0.0) for API key management |
| **Data Processing** | NumPy, Pandas (dependency of spaCy) |
| **NLP Dependencies** | Thinc, Cymem, Preshed, Murmurhash, Catalogue, Srsly |
| **Utilities** | Typer (CLI), Pydantic (data validation), Requests, Jinja2 |

---

## **EDITOR USED**

- **Visual Studio Code (VS Code)** - Primary development environment
- **Python Extensions** - Debugging, linting, and execution support

---

## **APPLICABILITY & USE CASES**

1. **Customer Service Automation** - Intelligent chatbots for 24/7 customer support without hardcoded responses
2. **Content Generation** - Dynamic text generation for educational tutoring, Q&A systems, and knowledge bases
3. **NLP Research & Development** - Experimentation with entity recognition, named entity extraction, and linguistic analysis
4. **Interactive Conversational Agents** - Building context-aware assistants for specialized domains
5. **Education & Learning** - AI tutors that adapt responses based on user input analysis
6. **Data Analysis & Insights** - Extract named entities and topics from unstructured text conversations
7. **Multilingual Applications** - Foundation for extending to multiple languages using spaCy's multi-language models

---

## **PROJECT STRUCTURE**

```
Task-3/src/chatbot/
├── main.py              (45 lines) - CLI entry point
├── engine.py            (17 lines) - NLP processing
├── ai_client.py         (65 lines) - Gemini API client
├── config.py            - Configuration
└── __init__.py          - Package init
```

**Total Code**: 127 lines across 3 Python modules

---

## **CODE MODULES EXPLANATION**

**engine.py** - NLP Processing with spaCy's en_core_web_md model; extracts entities (PERSON, ORG, LOCATION), noun chunks (topics), and lemmatized verbs for linguistic understanding; auto-downloads model if unavailable

**ai_client.py** - Google Gemini integration (65 lines); validates API key, dynamically discovers available models, sends context-enriched prompts to Gemini, maintains chat history for multi-turn conversations

**main.py** - CLI orchestrator (45 lines); validates environment, initializes NLPEngine and GeminiClient, manages conversation loop, handles errors with helpful guidance

---

## **EXECUTION FLOW**

1. Load GEMINI_API_KEY from .env
2. Initialize NLPEngine (spaCy) & GeminiClient
3. Read user input
4. Extract entities, nouns, verbs via NLP
5. Send enriched prompt to Gemini API
6. Display AI response
7. Loop until user exits

---

## **KEY TECHNICAL FEATURES**

- **Zero Hardcoding**: Fully dynamic AI responses, no predefined Q&A
- **Linguistic Intelligence**: Entity & noun extraction add semantic context
- **Model Flexibility**: Auto-detect available Gemini models with fallback
- **API Resilience**: Comprehensive error handling
- **Multi-Turn Conversations**: Chat history maintained
- **Security**: API keys via .env, never hardcoded


---

## **Output**

https://github.com/user-attachments/assets/3ca3181e-ba01-4e9b-b0a4-88697e93917b

---


