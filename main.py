# main.py
import pandas as pd
from news_api import get_news_data
from techcrunch_scraper import scrape_techcrunch  # <-- CHANGED IMPORT
from deepseek_enrichment import enrich_with_deepseek

def main():
    print("Starting the ETL pipeline...")

    # EXTRACT
    print("[1/4] Extracting data from Mediastack...")  # <-- CHANGED MESSAGE
    news_df = get_news_data()

    print("[2/4] Scraping data from TechCrunch...")    # <-- CHANGED MESSAGE
    tc_df = scrape_techcrunch()                        # <-- CHANGED FUNCTION NAME & VARIABLE

    # COMBINE
    print("Combining data...")
    # Make sure both DataFrames have the same columns
    combined_df = pd.concat([news_df, tc_df], ignore_index=True)  # <-- CHANGED VARIABLE

    # TRANSFORM (Basic Cleaning)
    print("[3/4] Cleaning data...")
    combined_df.drop_duplicates(subset=['title'], inplace=True, ignore_index=True)
    combined_df['description'].fillna('No description', inplace=True)

    # Save Raw Data
    combined_df.to_csv('data/raw/combined_news_raw.csv', index=False)
    print("Raw data saved to 'data/raw/combined_news_raw.csv'")

    # ENRICH with AI (This will take a while!)
    print("[4/4] Enriching data with DeepSeek AI. This will take a few minutes...")
    enriched_df = enrich_with_deepseek(combined_df)

    # LOAD Enriched Data
    enriched_df.to_csv('data/enriched/combined_news_enriched.csv', index=False)
    print("Pipeline complete! Enriched data saved to 'data/enriched/combined_news_enriched.csv'")

    # Print a sample to show it worked
    print("\nSample of enriched data:")
    print(enriched_df[['title', 'ai_sentiment']].head())

if __name__ == "__main__":
    main()
