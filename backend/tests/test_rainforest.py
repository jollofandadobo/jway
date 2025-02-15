import pytest
import requests
import requests_mock
from services.rainforest_service import fetch_rainforest_data

# Sample Mock Response
MOCK_RESPONSE = {
    "request_info": {"success": True},
    "product": {
        "title": "SanDisk 128GB Ultra MicroSDXC",
        "asin": "B073JYC4XM",
        "price": {"symbol": "$", "value": 13.75, "currency": "USD", "raw": "$13.75"},
    },
}

RAIN_FOREST_API_URL = "https://api.rainforestapi.com/request"


def test_fetch_rainforest_data_success():
    """Test successful API call to Rainforest API"""
    with requests_mock.Mocker() as mock:
        mock.get(RAIN_FOREST_API_URL, json=MOCK_RESPONSE, status_code=200)

        asin = "B073JYC4XM"
        response = fetch_rainforest_data(asin)

        assert response["request_info"]["success"] is True
        assert response["product"]["asin"] == asin
        assert response["product"]["title"] == "SanDisk 128GB Ultra MicroSDXC"
        assert response["product"]["price"]["value"] == 13.75


def test_fetch_rainforest_data_error():
    """Test handling of API request failure"""
    with requests_mock.Mocker() as mock:
        mock.get(RAIN_FOREST_API_URL, status_code=500, json={"error": "Internal Server Error"})

        asin = "INVALID-ASIN"
        response = fetch_rainforest_data(asin)

        assert "error" in response
        assert "Failed to fetch data" in response["error"]