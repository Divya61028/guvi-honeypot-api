from fastapi import FastAPI, Header, HTTPException, Request
import google.generativeai as genai
import os

app = FastAPI()


@app.get("/")
def home():
    return {
        "status": "Online",
        "project": "Agentic Honeypot - GUVI HCL Hackathon",
        "how_to_test": "Go to /docs to send a message"
    }


@app.post("/api/honeypot/test")
async def test_honeypot(request: Request, x_api_key: str = Header(None)):

    if x_api_key != "guvi123":
        raise HTTPException(status_code=401, detail="Invalid API Key")

   
    data = await request.json()
    scammer_msg = data.get("message", "Hello")

    
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return {"error": "AI Key missing in Replit Secrets"}
    
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
   
    system_prompt = (
        "You are acting as a gullible person being scammed. "
        "Your goal is to keep the scammer talking and try to get them to "
        "reveal their UPI ID or bank details. Be polite and worried."
    )
    
    
    response = model.generate_content(f"{system_prompt}\nScammer says: {scammer_msg}")

    return {
        "status": "Success",
        "agent_response": response.text,
        "captured_intel": "Scanning for UPI/Bank details..."
    }
