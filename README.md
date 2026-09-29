
# Agentic Chatbot FastAPI

An AI-powered chatbot application built with **FastAPI**, **Streamlit**, **LangChain**, and **LangGraph**.

## Overview

This project provides a chatbot interface where users can interact with AI models through a FastAPI backend and Streamlit frontend. The application is designed to support different model providers and optional web search capabilities.

## Features

- FastAPI backend for handling chat requests
- Streamlit-based frontend
- Support for multiple AI model providers
- Configurable system prompts
- Optional web search
- LangChain and LangGraph based agent workflow

## Project Structure

```text
agentic-chatbot-fastapi/
├── ai_agent.py       # AI agent and model integration
├── backend.py        # FastAPI backend
├── frontend.py       # Streamlit frontend
├── requirements.txt  # Python dependencies
├── Pipfile           # Pipenv configuration
├── Pipfile.lock      # Locked dependencies
├── README.md
└── LICENSE
```
## Requirements
Python 3.10+
Required Python dependencies from requirements.txt
API credentials for the configured AI/search providers when running with live services

## Running the Application

Install the dependencies:

pip install -r requirements.txt

Start the FastAPI backend:

python backend.py

Start the Streamlit frontend in another terminal:

streamlit run frontend.py

The frontend communicates with the FastAPI backend through the /chat endpoint.

## Configuration

The application uses environment variables for external service credentials.

GROQ_API_KEY=
OPENAI_API_KEY=
TAVILY_API_KEY=

Do not commit API keys or other secrets to the repository.

## License

This project is licensed under the MIT License. See the LICENSE file for details.


### GitHub par kaise update karna hai

1. Repo → **README.md** open karo.
2. ✏️ **Edit** button click karo.
3. Purana content delete karo.
4. Upar wala content paste karo.
5. **Commit changes**.
6. Commit message:
