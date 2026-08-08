import json
import os

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from models import (
    ChatRequest,
    ChatResponse,
    JobFitResponse
)

from prompts import (
    create_system_prompt,
    create_job_fit_prompt
)

from llm import get_llm_response

from memory import (
    add_message,
    get_history
)

from parser import extract_text_from_file


app = FastAPI()

# --------------------------------------------------
# CORS
# --------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------------------------------
# Load portfolio information
# --------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

PORTFOLIO_PATH = os.path.join(
    BASE_DIR,
    "data",
    "portfolio.txt"
)


with open(PORTFOLIO_PATH, "r", encoding="utf-8") as file:
    portfolio = file.read()


# --------------------------------------------------
# Create portfolio chatbot system prompt
# --------------------------------------------------

system_prompt = create_system_prompt(portfolio)


# --------------------------------------------------
# Chat endpoint
# --------------------------------------------------

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    # Store user's message
    add_message(
        role="user",
        content=request.message
    )

    # Build messages for the LLM
    messages = [
        {
            "role": "system",
            "content": system_prompt
        },
        *get_history()
    ]

    # Generate answer
    answer = get_llm_response(messages)

    # Store assistant's answer
    add_message(
        role="assistant",
        content=answer
    )

    return ChatResponse(
        response=answer
    )


# --------------------------------------------------
# Job fit endpoint
# --------------------------------------------------

@app.post("/job-fit", response_model=JobFitResponse)
async def job_fit(file: UploadFile = File(...)):

    # Read uploaded file
    file_content = await file.read()

    # Extract text from PDF/DOCX
    job_description = extract_text_from_file(
        file_content,
        file.filename
    )

    # Create job-fit prompt
    prompt = create_job_fit_prompt(
        portfolio,
        job_description
    )

    # Send job-fit request to LLM
    messages = [
        {
            "role": "system",
            "content": prompt
        }
    ]

    llm_response = get_llm_response(messages)

    # Convert JSON string into Python dictionary
    try:
        result = json.loads(llm_response)

    except json.JSONDecodeError:
        return JobFitResponse(
            match_percentage=0,
            matching_skills=[],
            missing_skills=[],
            reason="The AI returned an invalid job-fit response."
        )

    # Validate the result using Pydantic
    return JobFitResponse(**result)