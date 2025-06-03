from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from app.schemas.TextInput import TextInput
from app.schemas.SentimentResponse import SentimentResponse
from app.services.sentimentService import analyze_sentiment_text


router = APIRouter()

@router.post("/", response_model=SentimentResponse, summary="Analyze sentiment of a given text")
def analyze_sentiment(payload: TextInput):
    try:

        # validate text input is not empty
        text = payload.text.strip() # strip: remove leading and trailing whitespace
        if not text:
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST,
                detail="Text input cannot be empty",
            )
            
        sentiment, polarity = analyze_sentiment_text(text)
        return SentimentResponse(
            sentiment=sentiment,
            polarity=polarity,
        )

    except Exception as e:
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        )
            

