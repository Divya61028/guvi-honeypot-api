from fastapi import FastAPI, Header, HTTPException

app = FastAPI()
@app.get("/")
def home():
    return {
        "status": "Online",
        "message": "Welcome to the Agentic Honeypot",
        "docs_url": "/docs"
    }

@app.post("/api/honeypot/test")
def test_honeypot(x_api_key: str = Header(None)):
    if x_api_key != "guvi123":
        raise HTTPException(status_code=401, detail="Invalid API Key")

    return {
        "status": "Success",
        "agent_behavior": "Gullible Persona Active",
        "response_to_scammer": "Oh no! I didn't know about the fine. Can I pay via UPI right now? Please send me the ID!",
        "intelligence_gathered": {
            "platform": "FastAPI-Honeypot",
            "threat_level": "High"
        }
    }
