import json
import requests
import os
import pandas as pd
from langchain.tools import tool

class FinanceTools():
    @tool("Fetch historical stock prices")
    def fetch_historical_prices(ticker, start_date, end_date):
        """
        Fetches historical stock prices for a given ticker between the specified start and end dates.
        
        Args:
            ticker (str): The stock ticker symbol (e.g., 'AAPL').
            start_date (str): The start date in 'YYYY-MM-DD' format.
            end_date (str): The end date in 'YYYY-MM-DD' format.
        
        Returns:
            pd.DataFrame: A DataFrame containing the historical stock prices.
        """
        api_key = os.getenv('ALPHAVANTAGE_API_KEY')
        # url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={api_key}&outputsize=full'
        url = f'https://finnhub.io/api/v1/quote?symbol={ticker}&token={api_key}'
        response = requests.get(url)
        data = response.json()
        return data

    @tool("Fetch stock predictions")
    def fetch_predictions(ticker):
        """
        Fetches stock predictions for a given ticker from the Finnhub API.
        
        Args:
            ticker (str): The stock ticker symbol (e.g., 'AAPL').
        
        Returns:
            dict: A dictionary containing the prediction, confidence, and price target.
        """
        api_key = os.getenv('FINNHUB_API_KEY')
        url = f'https://finnhub.io/api/v1/stock/recommendation?symbol={ticker}&token={api_key}'
        response = requests.get(url)
        data = response.json()
        # Extract the latest recommendation
        if data:
            return data
        else:
            return {
                'ticker': ticker,
                'prediction': 'No data available',
                'confidence': 0,
                'price_target': 'N/A'
            }