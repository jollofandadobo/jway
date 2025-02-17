import os
import openai
import logging
from core.config import Config

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
        prompt = f"Summarize these product reviews and state if the overall sentiment is positive or negative:\n{reviews}"
        logger.info(f"Prompt: {prompt}")
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an AI that summarizes product reviews."},
                {"role": "user", "content": prompt}
            ]
        )
        logger.info(f"Response: {response}")
        summary = response.choices[0].message["content"].strip().replace('\n', ' ')
        sentiment = "positive" if "positive" in summary.lower() else "negative"
        return f"Reviews state a generally '{sentiment}' response, with the summary statement being: '{summary}'"
    except Exception as e:
        logger.error(f"Error summarizing reviews: {e}")
        return "Error generating summary."