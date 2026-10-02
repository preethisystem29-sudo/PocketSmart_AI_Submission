import os
import asyncio
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from google import genai


# ============================================================
# POCKETSMART AI - SERVER
# ============================================================

BASE_DIR = Path(__file__).resolve().parent


# ============================================================
# LOAD .ENV
# ============================================================

env_file = BASE_DIR / ".env"

if not env_file.exists():
    raise RuntimeError(
        f".env file was not found at:\n{env_file}\n\n"
        "Create a .env file in the same folder as server.py."
    )

load_dotenv(dotenv_path=env_file)


# ============================================================
# GEMINI SETTINGS
# ============================================================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()

GEMINI_MODEL = os.getenv(
    "GEMINI_MODEL",
    "gemini-3.8-flash"
).strip()


# ============================================================
# CHECK API KEY
# ============================================================

if not GEMINI_API_KEY:
    raise RuntimeError(
        "GEMINI_API_KEY is missing.\n\n"
        "Your .env file should contain:\n\n"
        "GEMINI_API_KEY=YOUR_REAL_GEMINI_API_KEY\n"
        "GEMINI_MODEL=gemini-3.8-flash\n"
    )


# ============================================================
# CREATE GEMINI CLIENT
# ============================================================

client = genai.Client(
    api_key=GEMINI_API_KEY
)


# ============================================================
# CREATE FASTAPI APPLICATION
# ============================================================

app = FastAPI(
    title="PocketSmart AI",
    description="AI-powered budget and recommendation assistant",
    version="1.1.0"
)


# ============================================================
# CORS
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# REQUEST MODEL
# ============================================================

class AskRequest(BaseModel):
    message: str


# ============================================================
# WEBSITE
# ============================================================

@app.get("/")
async def home():
    index_file = BASE_DIR / "index.html"

    if not index_file.exists():
        raise HTTPException(
            status_code=404,
            detail=f"index.html was not found at: {index_file}"
        )

    return FileResponse(index_file)


# ============================================================
# HEALTH CHECK
# ============================================================

@app.get("/health")
async def health():
    return {
        "status": "ok",
        "message": "PocketSmart AI API is running!",
        "model": GEMINI_MODEL,
        "api_key_loaded": bool(GEMINI_API_KEY)
    }


# ============================================================
# GEMINI AI
# ============================================================

@app.post("/api/ask")
async def ask_gemini(request: AskRequest):

    message = request.message.strip()

    if not message:
        raise HTTPException(
            status_code=400,
            detail="Message cannot be empty."
        )

    prompt = f"""
You are PocketSmart AI, a smart budget-aware
recommendation assistant.

The user has provided the following request:

{message}

YOUR TASK:

Create a practical, personalized recommendation
based on the user's budget, requirements and preferences.

IMPORTANT RULES:

1. Always respect the user's stated budget.
2. Never recommend a total amount greater than the user's budget.
3. If you mention prices or amounts, describe them as estimates
   unless the user supplied exact amounts.
4. Do not claim live prices.
5. Do not claim live product availability.
6. Do not claim discounts unless the user provides them.
7. Do not make financial guarantees.
8. Keep the recommendation practical and easy to understand.
9. If information is missing, make a reasonable assumption and
   clearly mention the assumption.
10. Try to keep some money as a reserve when appropriate.

RETURN THE ANSWER USING THIS FORMAT:

1. Recommendation Summary

Give a short and clear recommendation.

2. Suggested Budget Allocation

Give 3 to 6 categories.

Show the estimated amount for each category in INR.

The total must NOT exceed the user's budget.

3. Why This Plan Fits

Explain why this plan is suitable for the user's requirements
and budget.

4. Alternatives / Trade-offs

Give two alternative approaches.

Explain the main advantage and disadvantage of each.

5. Practical Tips

Give three useful practical tips.

6. Verification Note

Remind the user that AI-generated estimates should be checked
before making real purchases.
"""

    try:
        # Use the standard Gemini content-generation method.
        # This avoids requiring the Interactions API for this project.
        response = await asyncio.to_thread(
            client.models.generate_content,
            model=GEMINI_MODEL,
            contents=prompt
        )

        result = getattr(response, "text", None)

        if not result:
            result = "Gemini returned an empty response."

        return {
            "success": True,
            "response": result,
            "model": GEMINI_MODEL
        }

    except Exception as error:
        print()
        print("==============================================")
        print("              GEMINI ERROR")
        print("==============================================")
        print(type(error).__name__)
        print(str(error))
        print("==============================================")
        print()

        # Return the real error to the local frontend so troubleshooting
        # is much easier. The API key itself is never included.
        raise HTTPException(
            status_code=500,
            detail=(
                f"Gemini request failed: {type(error).__name__}: {error}"
            )
        )


# ============================================================
# SERVER STARTUP MESSAGE
# ============================================================

@app.on_event("startup")
async def startup_event():
    print()
    print("==============================================")
    print("          POCKETSMART AI STARTED")
    print("==============================================")
    print("Website:")
    print("http://127.0.0.1:8000")
    print()
    print("Health check:")
    print("http://127.0.0.1:8000/health")
    print()
    print("Gemini model:")
    print(GEMINI_MODEL)
    print()
    print("Gemini API key:")
    print("Loaded from .env" if GEMINI_API_KEY else "NOT LOADED")
    print()
    print("API endpoint:")
    print("POST /api/ask")
    print("==============================================")
    print()
