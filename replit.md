# Agentic Honeypot - GUVI HCL Hackathon

## Project Overview
A FastAPI-based honeypot API that uses Google's Gemini AI to engage scammers in conversation. The AI poses as a gullible person, keeping scammers talking while attempting to extract their UPI IDs or bank details.

## Tech Stack
- **Language:** Python 3.12
- **Framework:** FastAPI
- **AI Model:** Google Gemini 1.5 Flash (`google-generativeai`)
- **Server:** Uvicorn (ASGI)

## Project Structure
- `main.py` - Core application with FastAPI routes and Gemini AI integration
- `requirements.txt` - Python dependencies

## API Endpoints
- `GET /` - Returns project status and info
- `POST /api/honeypot/test` - Main honeypot endpoint (requires `x-api-key: guvi123` header)
- `GET /docs` - Interactive Swagger UI for testing

## Environment Variables / Secrets
- `GEMINI_API_KEY` - Google Gemini API key (required for AI responses)

## Running the App
```bash
uvicorn main:app --host 0.0.0.0 --port 5000
```

## API Usage
Send a POST request to `/api/honeypot/test` with:
- Header: `x-api-key: guvi123`
- Body: `{"message": "your scammer message here"}`
