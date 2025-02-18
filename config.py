import os
from dotenv import load_dotenv
#-----------------------------------------------------------------
#                Load environment variables from .env file
#----------------------------------------------------------------
load_dotenv()

class Config:
    """Centralized configuration settings for LLM API Keys and settings."""



#-----------------------------------------------------------------------------------------    
#                               API Keys
#------------------------------------------------------------------------------------------
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    OPENAI_API_KEY =os.getenv("OPENAI_API_KEY")
#----------------------------------------------------------------------------------------------
#                                       Default Models
#----------------------------------------------------------------------------------------------



    DEFAULT_GEMINI_MODEL = "gemini-1.5-pro"
    DEFAULT_GROQ_MODEL = "groq-mixtral-8x7b"
#--------------------------------------------------------------------------------------------------
#                                        Server Configuration
#---------------------------------------------------------------------------------------------------
    HOST = "127.0.0.1"
    PORT = 7100
     

# Initialize a global config instance
config = Config()


