from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from auth.utils import decode_token

security = HTTPBearer()

@app.post("/generate_news")
def generate_news(query: dict, credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        token_data = decode_token(credentials.credentials)
        # Later: run retrieval + react + generation here
        return {
            "summary": f"Personalized news for query: {query['query']}",
            "explanation": "This was generated using private + public retrieval based on your interests."
        }
    except:
        raise HTTPException(status_code=401, detail="Invalid token")
