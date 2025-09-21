# news_api.py
import requests
import pandas as pd
from config import MEDIASTACK_API_KEY  # Import from our config file

def get_news_data():
    """
    Fetches news data from the Mediastack API.
    Returns a pandas DataFrame with titles, descriptions, and other info.
    """
    # Construct the URL for the mediastack API
    # Parameters: 
    #   access_key = Your API key
    #   categories = technology, business, etc.
    #   countries = us, gb, etc.
    #   languages = en
    #   limit = 10 (number of articles to fetch)
    base_url = "http://api.mediastack.com/v1/news"
    params = {
        'access_key': MEDIASTACK_API_KEY,
        'categories': 'technology',  # You can change this: general, business, sports, etc.
        'countries': 'us',           # You can change this: us, gb, ca, etc.
        'languages': 'en',
        'limit': 10
    }

    try:
        # Send the GET request to the API
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # This will raise an error for bad status codes (4xx or 5xx)
        
        # Parse the JSON response
        api_data = response.json()
        
        # Check if the API returned an error
        if 'error' in api_data:
            error_msg = api_data['error'].get('message', 'Unknown API error')
            print(f"Mediastack API Error: {error_msg}")
            return pd.DataFrame()  # Return an empty DataFrame on error
        
        # Check if the 'data' key exists in the response
        if 'data' not in api_data:
            print("Error: Unexpected API response format - 'data' key not found")
            print(f"Full API response: {api_data}")
            return pd.DataFrame()
        
        articles = api_data['data']
        news_data = []
        
        # Loop through each article and extract the info we need
        for article in articles:
            news_data.append({
                'title': article.get('title', 'No Title'),
                'description': article.get('description', 'No Description'),
                'link': article.get('url', '#'),
                'source': article.get('source', 'Unknown Source'),
                'published_at': article.get('published_at', '')  # Optional: keep publish date
            })
        
        print(f"Successfully fetched {len(news_data)} articles from Mediastack API")
        return pd.DataFrame(news_data)
        
    except requests.exceptions.RequestException as e:
        print(f"Network error fetching data from Mediastack: {e}")
        return pd.DataFrame()
    except ValueError as e:
        print(f"Error parsing JSON response from Mediastack: {e}")
        return pd.DataFrame()

# Test the function if this file is run directly
if __name__ == "__main__":
    df = get_news_data()
    if not df.empty:
        print("Mediastack API Data Sample:")
        print(df[['title', 'source']].head())
    else:
        print("Failed to fetch data from Mediastack API")
