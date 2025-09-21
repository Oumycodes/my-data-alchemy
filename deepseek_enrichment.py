# deepseek_enrichment.py
import requests
import pandas as pd
import time
from config import DEEPSEEK_API_KEY  # Import from our config file

url = "https://api.deepseek.com/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
    "Content-Type": "application/json"
}

def get_ai_analysis(text):
    """Sends a single text to DeepSeek API and returns the response."""
    # A clear, structured prompt is key to getting a structured response.
    prompt = f"""
    Perform the following tasks on the text below:
    1. Analyze the sentiment as either 'Positive', 'Negative', or 'Neutral'.
    2. Generate a one-sentence summary.

    Return your answer in the exact following format:
    Sentiment: <result>
    Summary: <result>

    Text: {text}
    """

    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.1  # Low temperature for more focused, deterministic outputs
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except requests.exceptions.RequestException as e:
        print(f"API Error for text '{text[:50]}...': {e}")
        return "Error: Analysis failed"

def parse_ai_response(response):
    """Parses the structured response from DeepSeek into a dictionary."""
    sentiment = "Unknown"
    summary = "No summary generated."

    try:
        # Split the response into lines and parse them
        lines = response.split('\n')
        for line in lines:
            if line.startswith('Sentiment:'):
                sentiment = line.replace('Sentiment:', '').strip()
            elif line.startswith('Summary:'):
                summary = line.replace('Summary:', '').strip()
    except Exception as e:
        print(f"Could not parse AI response: {response}. Error: {e}")

    return {"sentiment": sentiment, "summary": summary}

def enrich_with_deepseek(df):
    """Applies AI enrichment to a DataFrame."""
    results = []
    for index, row in df.iterrows():
        # Combine title and description for analysis
        text_to_analyze = f"{row['title']}. {row['description']}"
        print(f"Analyzing: {text_to_analyze[:50]}...")

        ai_response = get_ai_analysis(text_to_analyze)
        parsed_data = parse_ai_response(ai_response)

        # Add new columns to the row
        new_row = row.copy()
        new_row['ai_sentiment'] = parsed_data['sentiment']
        new_row['ai_summary'] = parsed_data['summary']
        results.append(new_row)

        time.sleep(1)  # Pause for 1 second to respect rate limits

    return pd.DataFrame(results)
