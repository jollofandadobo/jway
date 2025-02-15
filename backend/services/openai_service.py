import os
import openai
import logging

# Load API Key from environment variables
openai.api_key = os.getenv("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")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)