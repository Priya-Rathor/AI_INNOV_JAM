from groq import Groq


async def check_groq(api_key:str,model:str):
    try:
        client = Groq(api_key=api_key)
        response = client.chat.completions.create(
            model=model,
            messages=[{"role":"system","content":"Test message"}],
            max_tokens=5
        )

        return {"status":"success","message":"API key ia va;id and  has quota available."}
        
    except Groq.AuthentcationError:
      return{"status":"error","message":"Invalid API key!"}
    
    except Groq.RateLimitError:
       return {"status":"error","message":"Quota exceeded or rate limit reached!"}
    
    except Exception:
       return {"status":"error","message":"An unknown error occurred."}
   