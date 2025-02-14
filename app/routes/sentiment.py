from fastapi import APIRouter
from transformers import pipeline

router = APIRouter()

# Use Hugging Face API instead of requiring local PyTorch/TensorFlow
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english", device=-1)

@router.post("/analyze")
async def analyze(text: str):
    sentiment = sentiment_pipeline(text)
    return sentiment
