import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Groq API Key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Model to use
MODEL_NAME = "llama-3.3-70b-versatile"

# Input and Output folders
INPUT_FOLDER = "input"
OUTPUT_FOLDER = "output"
#BATCH_SIZE = 10
INTENT_BATCH_SIZE = 10
ACTION_BATCH_SIZE = 5