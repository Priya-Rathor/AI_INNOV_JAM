from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from models.groqEval import evaluate_with_groq
from models.geminiEval import evaluate_with_gemini
from models.gptEval import evaluate_with_gpt

router = APIRouter()

# Define request model
class EvaluationRequest(BaseModel):
    question: str
    suggested_answer: str
    student_answer: str
    comparison_count: str
    marks: float
    temperature: float
    model: str
    provider: str

# Route for Groq evaluation
@router.post("/evaluate/groq")
async def evaluate_groq(items: List[EvaluationRequest]):
    return {"results": [evaluate_with_groq(item) for item in items]}  # ✅ FIXED

# Route for Gemini evaluation
@router.post("/evaluate/gemini")
async def evaluate_gemini(items: List[EvaluationRequest]):
    return {"results": [evaluate_with_gemini(item) for item in items]}  # ✅ FIXED


@router.post("/evaluate/gpt")
async def evaluate_gemini(items: List[EvaluationRequest]):
    return {"results": [evaluate_with_gpt(item) for item in items]}