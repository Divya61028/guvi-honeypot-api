from fastapi import FastAPI, Header, HTTPException, Request
import google.generativeai as genai
import os

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Online", "message": "Agentic Honeypot Active"}

@app.post("/api/honeypot/test")
async def test_honeypot(request: Request, x_api_key: str = Header(None)):
  
    if x_api_key != "guvi123":
        raise HTTPException(status_code=401, detail="Invalid API Key")

  
    data = await request.json()
    scammer_msg = data.get("message", "No message provided")

    
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return {"error": "API Key missing in Replit Secrets"}
    
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    system_prompt = "You are a gullible person. Respond to this scammer to keep them talking."
    response = model.generate_content(f"{system_prompt}\nScammer: {scammer_msg}")

    return {
        "status": "Success",
        "agent_response": response.text
    }
