from pydantic import BaseModel

class SentimentResponse(BaseModel):
    sentiment: str
    polarity: float