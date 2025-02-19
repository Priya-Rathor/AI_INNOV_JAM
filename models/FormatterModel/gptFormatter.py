import re
import json
import openai
from models.EvalModels import gpt_client
from utils.promptFormatter import get_extraction_prompt  

DEFAULT_GPT_MODEL = "gpt-4o"  

def extract_questions_answers_with_gpt(content: str):
    """Extracts questions and answers from content using GPT-4o."""
    print("Started extracting questions and answers...")

    
    prompt = get_extraction_prompt(content)

    try:
        response = gpt_client.chat.completions.create(  # ✅ Correct method
            model=DEFAULT_GPT_MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that extracts structured data from text."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.3,
        )

        print("Received response from GPT-4o model.")

        # Extract the response text
        output = response.choices[0].message.content.strip()

        # ✅ Clean unwanted JSON markdown delimiters
        cleaned_result = re.sub(r'```json\n|\n```', '', output)

        # ✅ Parse the cleaned result into a proper JSON format
        json_result = json.loads(cleaned_result)

        print(f"Cleaned result: {json_result}")
        return json_result  # ✅ Return as a JSON object

    except Exception as e:
        print(f"Error during the request: {e}")
        return {"error": f"Error processing the request: {str(e)}"}
