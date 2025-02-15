import requests
from core.config import Config

RAIN_FOREST_API_URL = "https://api.rainforestapi.com/request"

def fetch_rainforest_data(asin: str):
    params = {
        "api_key": Config.RAINFOREST_API_KEY,
        "amazon_domain": "amazon.com",
        "asin": asin,
        "type": "product"
    }

    # DEBUG LOGGING
    print(f"[DEBUG] Calling Rainforest API with: {params}")

    try:
        response = requests.get(RAIN_FOREST_API_URL, params=params, timeout=10)
        response.raise_for_status()


        data = response.json()
        print(f"[DEBUG] Rainforest API Response: {data}")  # Debug log

        return data
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Rainforest API Error: {str(e)}")  # Debug log
        return {"error": f"Failed to fetch data: {str(e)}"}

