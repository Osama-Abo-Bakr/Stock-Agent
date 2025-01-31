import json
import os
import requests
from langchain.tools import tool
from datetime import datetime, timedelta


class SearchTools():
    @tool("Search financial news")
    def search_internet(query):
        """Useful to search the internet
        about a a given topic and return relevant results"""
        print("Searching the internet...")
        top_result_to_return = 5
        url = "https://google.serper.dev/search"
        
        # payload = json.dumps(
        #     {"q": query, "num": top_result_to_return, "tbm": "nws"})
        
        # Get news from last 4 hours (API limitation)
        time_filter = (datetime.now() - timedelta(hours=4)).strftime('%Y-%m-%dT%H:%M:%S')
        
        payload = json.dumps({
            "q": f"{query} after:{time_filter}",
            "num": 5,
            "tbm": "nws",
            "sort": "date"
        })
        headers = {
            'X-API-KEY': os.environ['SERPER_API_KEY'],
            'content-type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        # check if there is an organic key
        if 'organic' not in response.json():
            return "Sorry, I couldn't find anything about that, there could be an error with you serper api key."
        else:
            results = response.json()['organic']
            string = []
            print("Results:", results[:top_result_to_return])
            for result in results[:top_result_to_return]:
                try:
                    # Attempt to extract the date
                    date = result.get('date', 'Date not available')
                    string.append('\n'.join([
                        f"Title: {result['title']}",
                        f"Link: {result['link']}",
                        f"Date: {date}",  # Include the date in the output
                        f"Snippet: {result['snippet']}",
                        "\n-----------------"
                    ]))
                except KeyError:
                    next

            return '\n'.join(string)