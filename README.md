# Sentiment Analysis API

A simple and efficient FastAPI-based service that performs sentiment analysis on text input. The API uses TextBlob to analyze the sentiment of provided text and returns whether it's positive, negative, or neutral, along with a polarity score.

## Features

- Text sentiment analysis (positive/negative/neutral)
- Polarity score calculation
- RESTful API endpoint
- FastAPI automatic documentation
- Pydantic data validation

## Prerequisites

- Python 3.7+
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd SentimentAnalyzer
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
```

3. Activate the virtual environment:
- Windows:
```bash
.\venv\Scripts\activate
```
- Unix/MacOS:
```bash
source venv/bin/activate
```

4. Install the required dependencies:
```bash
pip install fastapi uvicorn textblob
```

## Running the Application

1. Start the server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, you can access:
- Interactive API documentation (Swagger UI): `http://localhost:8000/docs`
- Alternative API documentation (ReDoc): `http://localhost:8000/redoc`

## API Usage

### Analyze Sentiment

**Endpoint:** `POST /sentiment`

**Request Body:**
```json
{
    "text": "Your text to analyze"
}
```

**Response:**
```json
{
    "sentiment": "positive|negative|neutral",
    "polarity": 0.0
}
```

**Example using curl:**
```bash
curl -X POST "http://localhost:8000/sentiment" \
     -H "Content-Type: application/json" \
     -d '{"text": "I love this project!"}'
```

## Polarity Score Explanation

- Polarity ranges from -1.0 to 1.0
- Values > 0 indicate positive sentiment
- Values < 0 indicate negative sentiment
- Value = 0 indicates neutral sentiment

## License

This project is open source and available under the MIT License.
