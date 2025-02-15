import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

class Config:
    RAINFOREST_API_KEY = os.getenv("RAINFOREST_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    # Validate that keys are set
    if not RAINFOREST_API_KEY:
        raise ValueError("RAINFOREST_API_KEY is missing, add it to your .env file")
    if not OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY is missing, add it to your .env file")