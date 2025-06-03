from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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

    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:3000",
            "http://127.0.0.1:3000",
            "http://localhost:8000",
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include the router
    app.include_router(
        router,
        prefix="/sentiment",
        tags=["sentiment"]
    )

    return app

app = create_app()
