from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

@app.post("/api/honeypot/test")
def test_honeypot(x_api_key: str = Header(None)):
    if x_api_key != "guvi123":
        raise HTTPException(status_code=401, detail="Invalid API Key")

    return {
        "status": "ok",
        "message": "Honeypot API is reachable"
    }
