import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_hn_headlines():
    """
    Scrapes the top headlines from Hacker News.
    Returns a pandas DataFrame with titles and links.
    """
    url = 'https://news.ycombinator.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    titles = soup.find_all('span', class_='titleline')
    data = []
    for title in titles:
        a_tag = title.find('a')
        headline = a_tag.get_text()
        link = a_tag['href']
        data.append({'title': headline, 'link': link, 'description': '', 'source': 'Hacker News'})

    return pd.DataFrame(data)

# Test the function if this file is run directly
if __name__ == "__main__":
    df = scrape_hn_headlines()
    print(df.head())
