import re
from . import gemini_client
from utils.promptsEval import generate_prompt


DEFAULT_GEMINI_MODEL = "gemini-1.5-pro" 
def evaluate_with_gemini(state):
    """Evaluates student answer using Gemini LLM."""
    prompt = generate_prompt(state)  # ✅ Generate prompt as raw text
    
    try:
        # ✅ Correct request format for Gemini API
        response = gemini_client.generate_content(prompt)  # ✅ Send raw text prompt

        # Ensure response is valid
        if not response or not hasattr(response, "text") or not response.text:
            return {"gemini_score": 0.0, "feedback": "Error: Empty response from Gemini model."}

        output = response.text.strip()

        # Parse output to extract score and feedback
        return parse_output(output, state.marks, "gemini_score")

    except Exception as e:
        return {"score": 0.0, "feedback": f"Error: {str(e)}"}

def parse_output(output, max_marks, score_key):
    """Parses Gemini LLM output to extract score and feedback correctly."""
    
    # Extract numeric score (must be at the beginning of the response)
    score_match = re.search(r"^(\d+(\.\d+)?)", output)
    score = float(score_match.group()) if score_match else 0.0

    # Extract feedback after score pattern
    feedback = "No valid feedback."
    
    if " - " in output:
        parts = output.split(" - ", 1)
        if len(parts) > 1 and parts[1].strip():
            feedback = parts[1].strip()
    
    # If feedback is missing, attempt to extract from the response
    elif len(output) > 5:
        feedback = output.strip()

    # Ensure feedback is meaningful
    if feedback.lower() in ["no valid feedback.", "", " "]:
        feedback = "The model did not provide a detailed explanation. Please adjust the prompt."

    return {score_key: min(score, max_marks), "feedback": feedback}
