import pandas_market_calendars as mcal
from datetime import datetime
import pytz

def is_market_open(self):
        """
        Checks if the NYSE market is currently open.
        """
        nyse = mcal.get_calendar('NYSE')
        schedule = nyse.schedule(start_date=datetime.now().date(), end_date=datetime.now().date())
        # If there's no schedule for today (e.g., weekend or holiday), the market is closed
        if schedule.empty:
            return False
        
        # Get the market open and close times for today
        market_open = schedule.iloc[0]['market_open']
        market_close = schedule.iloc[0]['market_close']
        
        # Make the current time timezone-aware (using the same timezone as the market schedule)
        now = datetime.now(pytz.timezone('America/New_York'))
        
        # Check if the current time is within market hours
        return market_open <= now <= market_close