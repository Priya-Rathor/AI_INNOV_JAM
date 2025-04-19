from fastapi import APIRouter, Form,HTTPException
from pydantic import BaseModel
from typing import List
from models.EvalModels.groqEval import evaluate_with_groq
from models.EvalModels.geminiEval import evaluate_with_gemini
from models.EvalModels.gptEval import evaluate_with_gpt
from models.CheckModels.gpt import check_gpt
from fastapi.responses import JSONResponse
from models.FormatterModel.gptFormatter import extract_questions_answers_with_gpt
from models.CheckModels.gemini import check_gemini
from models.CheckModels.groq import check_groq
from models.FormatterModel.gemini import extract_questions_answers_with_gemini






router = APIRouter()





#--------------------------------------------------------------------------------
#                                Model for evaluation
#---------------------------------------------------------------------------------
class EvaluationRequest(BaseModel):
    question: str
    suggested_answer: str
    student_answer: str
    comparison_count: str
    marks: int
    temperature: float
    model: str
    provider: str







#----------------------------------------------------------------------------------
#                                    Model for the Check api
#----------------------------------------------------------------------------------


class CheckRequest(BaseModel):
    api_key: str
    model:str




#------------------------------------------------------------------------------------
#                           Evaluation Routes  
#------------------------------------------------------------------------------------
# Route for Groq evaluation 
@router.post("/evaluate/groq")
async def evaluate_groq(items: List[EvaluationRequest]):
    return {"results": [evaluate_with_groq(item) for item in items]} 





# Route for Gemini evaluation
@router.post("/evaluate/gemini")
async def evaluate_gemini(items: List[EvaluationRequest]):
    return {"results": [evaluate_with_gemini(item) for item in items]}  





@router.post("/evaluate/gpt")
async def evaluate_gpt(items: List[EvaluationRequest]):
    return {"results": [evaluate_with_gpt(item) for item in items]}







#-------------------------------------------------------------------------------------------------
#                                              Check API Routes 
#-------------------------------------------------------------------------------------------------


@router.post("/check/gpt")
async def check_gpt_status(request: CheckRequest):
    try:
        status = await check_gpt(api_key=request.api_key, model=request.model)
        return JSONResponse(content=status)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error: {str(e)}")
    





@router.post("/check/gemini")
async def check_gemini_status(request:CheckRequest):
    try:
        status = await check_gemini(api_key=request.api_key,model=request.model)
        return JSONResponse(content=status)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error:{str(e)}")    
    






@router.post("/check/groq")
async def check_groq_status(request:CheckRequest):
    try:
        status =await check_groq(api_key=request.api_key,model=request.model)
        return JSONResponse(content=status)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error:{str(e)}")
    





#-------------------------------------------------------------------------------------------------
#                                    FormatterAPI  Routes
# -----------------------------------------------------------------------------------------------


@router.post("/extract/")
async def extract_data_from_text(content: str = Form(...)):
    """API endpoint to process the text and extract structured data."""
    print(f"Received request: Content length = {len(content)} characters")

    extracted_data = extract_questions_answers_with_gpt(content)

    try:
        return JSONResponse(content=extracted_data, status_code=200)
    except Exception as e:
        return {"error": f"Error processing request: {str(e)}"}
    






@router.post("/extract/gemini")
async def extract_data_from_text_gemini(content:str = Form(...)):
    """API endpoint to process the text and extract structured data."""
    print(f"Received request:Content length ={len(content)} characters")

    extrated_data = extract_questions_answers_with_gemini(content)
    
    try:
        return JSONResponse(content=extrated_data,status_code=200)
    except Exception as e:
        return {"error":f"Error processing request:{str(e)}"}
