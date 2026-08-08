import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Get API key from environment
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# LLM model
MODEL_NAME = "llama-3.3-70b-versatile"

# Make sure the API key exists
if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY is missing. Please add it to your .env file."
    )