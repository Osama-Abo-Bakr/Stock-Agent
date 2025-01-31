import requests
import os
import pandas as pd
from langchain.tools import tool
import yfinance as yf 

class FinanceTools():
    @tool("Fetch historical stock prices")
    def fetch_historical_prices(ticker, period='5d'):
        """
        Fetches historical stock prices with real-time updates using Yahoo Finance.

        Args:
            ticker (str): Stock ticker symbol
            period (str): Data period (1d, 5d, 1mo, 1y)

        Returns:
            dict: Contains OHLC data, volume, and timestamps in Finnhub-like format
        """
        try:
            stock = yf.Ticker(ticker)
            df = stock.history(period=period)
            
            if df.empty:
                return {"error": f"No data found for {ticker}"}
            
            # Convert to Finnhub-like format for compatibility
            return {
                "o": df['Open'].tolist(),
                "h": df['High'].tolist(),
                "l": df['Low'].tolist(),
                "c": df['Close'].tolist(),
                "v": df['Volume'].tolist(),
                "t": df.index.astype('int64') // 10**9  # Convert timestamps to UNIX
            }
        except Exception as e:
            return {"error": str(e)}


    @tool("Fetch real-time stock quote")
    def fetch_realtime_quote(ticker):
        """
        Fetches the real-time stock quote for the given ticker symbol.
        Returns a JSON object with the current price, bid, ask, open, high, low, and volume.
        """
        try:
            api_key = os.getenv('FINNHUB_API_KEY')
            url = f'https://finnhub.io/api/v1/quote?symbol={ticker}&token={api_key}'
            return requests.get(url).json()
        
        except KeyError:
            return {"error": "Invalid API response"}
        except requests.exceptions.RequestException:
            return {"error": "Network issue"}
    
    
    @tool("Analyze technical indicators")
    def analyze_technical(data):
        """
        Calculates SMAs, RSI, and MACD (with signal line and histogram) from price data.
        """
        try:
            if isinstance(data, dict) and 'data' in data and 'prices' in data['data']:
                prices = data['data']['prices']
                data = prices
                
            df = pd.DataFrame(data)
            
            if 'close' in df.columns:
                df.rename(columns={'close': 'c'}, inplace=True)
            elif 'Close' in df.columns:
                df.rename(columns={'Close': 'c'}, inplace=True)
            
            # Validate input format
            if 'c' not in df.columns:
                return {"error": "Missing 'c' (closing prices) in input data"}
                
            closes = df['c'].ffill().bfill()  # Clean NaN values

            # 1. Simple Moving Averages
            df['sma20'] = closes.rolling(20, min_periods=1).mean()
            df['sma50'] = closes.rolling(50, min_periods=1).mean()

            # 2. MACD Calculations (12/26/9 standard configuration)
            df['ema12'] = closes.ewm(span=12, adjust=False).mean()
            df['ema26'] = closes.ewm(span=26, adjust=False).mean()
            df['macd'] = df['ema12'] - df['ema26']
            df['signal'] = df['macd'].ewm(span=9, adjust=False).mean()
            df['histogram'] = df['macd'] - df['signal']

            # 3. RSI Calculation
            delta = closes.diff()
            gain = delta.where(delta > 0, 0)
            loss = -delta.where(delta < 0, 0)
            
            avg_gain = gain.rolling(14, min_periods=1).mean()
            avg_loss = loss.rolling(14, min_periods=1).mean()
            
            rs = avg_gain / (avg_loss + 1e-10)  # Prevent division by zero
            df['rsi'] = 100 - (100 / (1 + rs))

            # Return last 10 periods for all indicators
            return df[['sma20', 'sma50', 'rsi', 'macd', 'signal', 'histogram']].tail(10).to_dict()
        
        except Exception as e:
            return {"error": f"Technical analysis failed: {str(e)}"}

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