
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
