from fastapi import FastAPI, Header, HTTPException, Body
import google.generativeai as genai
import os

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Online", "message": "Honeypot is Running"}

@app.post("/api/honeypot/test")
async def test_honeypot(
    x_api_key: str = Header(None), 
    payload: dict = Body(...)
):
    # 1. Security Check
    if x_api_key != "guvi123":
        raise HTTPException(status_code=401, detail="Invalid API Key")

    # 2. Extract message from the Request Body
    scammer_msg = payload.get("message", "No message provided")

    # 3. AI Logic
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return {"error": "API Key missing in Environment Variables"}
    
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    system_prompt = "You are a gullible person. Respond to this scammer to keep them talking."
    response = model.generate_content(f"{system_prompt}\nScammer: {scammer_msg}")

    return {
        "status": "Success",
        "agent_response": response.text
    }
