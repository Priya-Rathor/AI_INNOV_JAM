from config import config
from groq import Groq
import google.generativeai as genai

import openai
from config import config

# ✅ Initialize OpenAI GPT Client
gpt_client = openai.OpenAI(api_key=config.OPENAI_API_KEY)


# Configure API key globally
genai.configure(api_key=config.GEMINI_API_KEY)

# Create the Gemini model instance
gemini_client = genai.GenerativeModel(model_name=config.DEFAULT_GEMINI_MODEL)

groq_client = Groq(api_key=config.GROQ_API_KEY)

# Import model functions
