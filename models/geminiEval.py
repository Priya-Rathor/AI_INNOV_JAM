import re
from . import gemini_client
from utils.promptsEval import generate_prompt

DEFAULT_GEMINI_MODEL = "gemini-1.5-pro"

def evaluate_with_gemini(state):
    """Evaluates student answer using Gemini LLM."""
    model_name = state.model if state.model else DEFAULT_GEMINI_MODEL
    prompt = generate_prompt(state)  # ✅ Use exact prompt without modification

    try:
        response = gemini_client.generate_content(prompt)  # ✅ Send raw text prompt

        if not response or not hasattr(response, "text") or not response.text:
            return {"score": 0.0, "feedback": "Error: Empty response from Gemini model."}

        output = response.text.strip()

        # ✅ Parse output and ensure "score" is extracted correctly
        return parse_output(output, state.marks)

    except Exception as e:
        return {"score": 0.0, "feedback": f"Error: {str(e)}"}

def parse_output(output, max_marks):
    """Parses Gemini LLM output to extract score and feedback correctly."""
    
    # ✅ Extract numeric score from anywhere in the response
    score_match = re.search(r"(\b\d+(\.\d+)?\b)", output)  # Matches first numeric value
    score = float(score_match.group()) if score_match else 0.0

    # ✅ Extract feedback after score pattern
    feedback = "No valid feedback."

    # Ensure valid feedback is captured
    if " - " in output:
        parts = output.split(" - ", 1)
        if len(parts) > 1 and parts[1].strip():
            feedback = parts[1].strip()
    elif len(output) > 5:
        feedback = output.strip()

    # ✅ Ensure meaningful feedback
    if feedback.lower() in ["no valid feedback.", "", " "]:
        feedback = "The model did not provide a detailed explanation. Please adjust the prompt."

    return {"score": min(score, max_marks), "feedback": feedback}
