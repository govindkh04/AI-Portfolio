from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str

class JobFitResponse(BaseModel):
    match_percentage: int
    matching_skills: list[str]
    missing_skills: list[str]
    reason: str
