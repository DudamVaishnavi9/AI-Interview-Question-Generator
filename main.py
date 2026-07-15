import os
from typing import Literal

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from google import genai
from google.genai import types
from pydantic import BaseModel, Field

# Load environment variables
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

client = genai.Client(api_key=API_KEY)

app = FastAPI(
    title="AI Interview Question Generator API",
    version="1.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InterviewRequest(BaseModel):
    topic: str = Field(min_length=2, max_length=50)
    difficulty: Literal["Easy", "Medium", "Hard"]
    num_questions: int = Field(gt=0, le=20)


@app.get("/")
def home():
    return {
        "message": "AI Interview Question Generator API is running."
    }


@app.post("/interview")
def generate_questions(req: InterviewRequest):

    prompt = f"""
Generate exactly {req.num_questions} interview questions.

Topic:
{req.topic}

Difficulty:
{req.difficulty}

Rules:

1. Number every question.
2. Questions should be unique.
3. Focus on technical interviews.
4. Do NOT provide answers.
5. Do NOT add introductions or conclusions.
6. Keep questions concise.
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.7,
                system_instruction="""
You are an expert technical interviewer.

Generate only numbered interview questions.

Do not include explanations.
Do not include greetings.
Do not include headings.
"""
            )
        )

        if not response.text:
            raise HTTPException(
                status_code=500,
                detail="Empty response received from Gemini."
            )

        return {
            "topic": req.topic,
            "difficulty": req.difficulty,
            "questions": response.text.strip()
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Gemini API Error: {str(e)}"
        )
