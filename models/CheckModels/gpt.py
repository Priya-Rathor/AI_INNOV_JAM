import openai
async def check_gpt(api_key:str,model:str):
    try:
        client = openai.OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model=model,
            messages=[{"role":"system","content":"Test message"}],
            max_tokens=5
        )

        return {"status":"success","message":"API key is valid and has quota available."}
    
    except openai.AuthenticationError:
        return {"status":"error","message":"Invalid API key!"}
    
    except openai.RateLimitError:
        return {"status":"error","message":"Quota exceeded or rate limit reached!"}
    except Exception:
        return {"status":"error","message":"An unknown error occurred."}