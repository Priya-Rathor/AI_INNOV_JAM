import re 
import json 
from models.EvalModels import gemini_client
from utils.promptFormatter import get_extraction_prompt
import google.generativeai as genai



def extract_questions_answers_with_gemini(content:str):
    """Extracts questions and answers from  content using Gemini"""
    print("Started exracting questions and answers..")
    model = genai.GenerativeModel("gemini-2.0-flash-exp")

    prompt = get_extraction_prompt(content)

    try:
        print("Sending request to Gemini model...")
        response = model.generate_content(prompt)
        print("Received response from Gemini  model.")

        if hasattr(response,'text'):
            result = response.text.strip()

        else:
            result ="No valid content returned"

        cleaned_result = re.sub(r'```json\n|\n```','',result)

        json_result = json.loads(cleaned_result)

        print(f"Cleaned result:{json_result}")

        return json_result

    except Exception as e:
        print(f"Error during the request:{e}")
        return {"error":f"Error processing the  request:{str(e)}"}        