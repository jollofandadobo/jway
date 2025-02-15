import os
import openai
import logging
import config

# Load API Key from environment variables
openai.api_key = config.Config.OPENAI_API_KEY
# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)