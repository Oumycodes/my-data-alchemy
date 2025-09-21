# techcrunch_scraper.py
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_techcrunch():
    """
    Scrapes the latest headlines from TechCrunch.
    Returns a pandas DataFrame.
    """
    url = 'https://techcrunch.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() # Raises an error for bad status codes (4xx or 5xx)
        
        soup = BeautifulSoup(response.text, 'html.parser')
        data = []
        
        # Find all article headlines on the page. SELECTOR MAY NEED UPDATING.
        # This CSS selector finds <a> tags within <h2> headings that have a specific class.
        articles = soup.select('h2 a') 
        
        for article in articles:
            headline = article.get_text().strip()
            link = article['href']
            # Ensure it's a valid article link, not a homepage link
            if headline and link and '/202' in link: 
                data.append({
                    'title': headline,
                    'description': '', # We don't get a description easily here
                    'link': link,
                    'source': 'TechCrunch'
                })
        
        return pd.DataFrame(data)
        
    except requests.exceptions.RequestException as e:
        print(f"Failed to scrape TechCrunch: {e}")
        return pd.DataFrame() # Return empty DataFrame on error

if __name__ == "__main__":
    df = scrape_techcrunch()
    print(f"Scraped {len(df)} headlines from TechCrunch")
    if not df.empty:
        print(df.head())
