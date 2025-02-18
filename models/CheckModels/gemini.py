import google.generativeai as genai
import os 
async def check_gemini(api_key: str, model: str):
    try:
        # Set API key for gemini (Google generative AI)
        os.environ['GOOGLE_API_KEY'] = api_key
        
        # Make the request to the Gemini API
        response = genai.ChatCompletion.create(  # Use correct method name
            model=model,
            messages=[{"role": "system", "content": "Test message"}],
            max_tokens=5
        )
        
        # If the request is successful
        return {"status": "success", "message": "API key is valid and has quota available."}
    
    except Exception as e:
        # Catch general exceptions and handle them
        error_message = str(e)
        print(f"Error occurred: {error_message}")  # Log to the console for debugging
        
        if "authentication" in error_message.lower():
            return {"status": "error", "message": "Invalid API key!"}
        elif "quota" in error_message.lower() or "rate limit" in error_message.lower():
            return {"status": "error", "message": "Quota exceeded or rate limit reached!"}
        else:
            return {"status": "error", "message": f"An unknown error occurred: {error_message}"}
