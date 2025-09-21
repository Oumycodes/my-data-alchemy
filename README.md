# Week 3: AI-Enhanced Data Pipeline

This project builds an ETL pipeline that extracts news data from an API and a website, cleans it, and uses the DeepSeek AI to perform sentiment analysis and generate summaries.

## Data Sources
1.  **NewsAPI:** Provides recent articles on "Artificial Intelligence".
2.  **Hacker News:** Top headlines scraped from the homepage.

## AI Enhancements
The pipeline uses the DeepSeek API to:
-   **Analyze Sentiment:** Classifies each article as 'Positive', 'Negative', or 'Neutral'.
-   **Generate Summaries:** Creates a one-sentence summary of each article.

## Repository Structure
my_data_alchemy/
├── main.py # Main orchestration script
├── deepseek_enrichment.py # AI enhancement logic
├── news_api.py # Fetches data from NewsAPI
├── hn_scraper.py # Scrapes Hacker News
├── config.py # API Keys (ignored by Git)
├── requirements.txt # Python dependencies
├── data/
│ ├── raw/ # Raw extracted data
│ └── enriched/ # AI-enriched data
└── examples/ # Sample data files


## Installation & Usage

### Prerequisites
- Python 3.7+
- `pip` (Python package installer)

### Steps
1.  **Clone this repository.**
    ```bash
    git clone https://github.com/your-username/week3-data-alchemy.git
    cd week3-data-alchemy
    ```

2.  **Install the required Python packages.**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Get a free API key from [mediastack.com](https://mediastack.com/).**

4.  **Configure your API key.**
    -   Open the `config.py` file.
    -   Replace `"YOUR_MEDIASTACK_KEY_HERE"` with your actual API key from mediastack.
    -   The DeepSeek API key is already pre-filled for use.

5.  **Run the pipeline.**
    ```bash
    python main.py
    ```
    The script will extract, clean, enrich, and save the data. This may take a few minutes due to API rate limiting.

## Example

### Before (Raw Data)
| title | description | source | link |
| :--- | :--- | :--- | :--- |
| New AI Model Breaks Records | Researchers at DeepSeek announced a new breakthrough... | Tech News | https://example.com/article1 |

### After (Enriched Data)
| title | description | source | ai_sentiment | ai_summary |
| :--- | :--- | :--- | :--- | :--- |
| New AI Model Breaks Records | Researchers at DeepSeek announced... | Tech News | **Positive** | DeepSeek researchers have developed a new model that significantly outperforms previous benchmarks. |
