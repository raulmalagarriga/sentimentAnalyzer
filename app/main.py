from fastapi import FastAPI
from app.routers.sentimentRouter import router

def create_app() -> FastAPI:
    """
    Application factory: creates and configures the FastAPI instance.
    """
    app = FastAPI(
        title="Sentiment Analysis API",
        description="A simple API that returns positive/negative/neutral sentiment for a given text input.",
        version="1.0.0",
    )

    # Include the router under the "/sentiment" prefix
    app.include_router(
        router,
        prefix="/sentiment",
        tags=["sentiment"]
    )

    return app

# The actual ASGI application
app = create_app()


# class TextInput(BaseModel):
#     text: str

# class SentimentResponse(BaseModel):
#     sentiment: str
#     polarity: float

# @app.post("/sentiment", response_model=SentimentResponse, summary="Analyze sentiment of a given text")
# def analyze_sentiment(payload: TextInput):
#     blob = TextBlob(payload.text)
#     polarity = round(blob.sentiment.polarity, 3)

#     if polarity > 0:
#         sentiment = "positive"
#     elif polarity < 0:
#         sentiment = "negative"
#     else:
#         sentiment = "neutral"

#     return SentimentResponse(sentiment=sentiment, polarity=polarity)
