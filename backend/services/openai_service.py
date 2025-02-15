"""
Handles OpenAI API request
"""
import os
import openai
import logging
from ..core.config import Config

# Load API Key from environment variables
openai.api_key = Config.OPENAI_API_KEY
# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def summarize_reviews(reviews: list) -> str:
    """
    Summarizes product reviews using OpenAI GPT.
    :param reviews: List of review texts
    :return: AI-generated summary
    """
    try:
        prompt = f"Summarize these product reviews:\n{reviews}"
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are an AI that summarizes product reviews."},
                      {"role": "user", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        logger.error(f"Error summarizing reviews: {e}")
        return "Error generating summary."

