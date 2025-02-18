import re
from . import gpt_client
from utils.promptsEval import generate_prompt

DEFAULT_GPT_MODEL = "gpt-4-turbo"  # ✅ Default GPT model

def evaluate_with_gpt(state):
    """Evaluates student answer using GPT LLM."""
    model_name = state.model if state.model else DEFAULT_GPT_MODEL  # ✅ Use default model if not provided
    prompt = generate_prompt(state)  # ✅ Generate prompt

    try:
        response = gpt_client.chat.completions.create(
            model=model_name,  # ✅ Use the correct model name
            messages=[{"role": "system", "content": prompt}],
            temperature=state.temperature
        )
        output = response.choices[0].message.content.strip()
        
        # ✅ Parse output and ensure "score" is used instead of "gpt_score"
        return parse_output(output, state.marks, "score")

    except Exception as e:
        return {"score": 0.0, "feedback": f"Error: {str(e)}"}

def parse_output(output, max_marks, score_key):
    """Parses LLM output and extracts score & feedback."""
    
    # ✅ Extract numeric score
    score_match = re.search(r"\d+(\.\d+)?", output)
    score = float(score_match.group()) if score_match else 0.0

    # ✅ Extract feedback after score pattern
    feedback = "No valid feedback."
    if " - " in output:
        parts = output.split(" - ", 1)
        if len(parts) > 1 and parts[1].strip():
            feedback = parts[1].strip()

    # ✅ Ensure meaningful feedback
    if feedback.lower() in ["no valid feedback.", "", " "]:
        feedback = "The model did not provide a detailed explanation. Please adjust the prompt."

    return {score_key: min(score, max_marks), "feedback": feedback}
