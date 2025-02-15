import requests
import logging
from core.config import Config

logging.basicConfig(level=logging.INFO)

RAIN_FOREST_API_URL = "https://api.rainforestapi.com/request"

def fetch_rainforest_data(asin: str):
    params = {
        "api_key": Config.RAINFOREST_API_KEY,
        "amazon_domain": "amazon.com",
        "asin": asin,
        "type": "product"
    }

    logging.info(f"Calling Rainforest API with ASIN: {asin}")

    try:
        response = requests.get(RAIN_FOREST_API_URL, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Rainforest API Error: {str(e)}")
        return {"error": f"Failed to fetch data: {str(e)}"}