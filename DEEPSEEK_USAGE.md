

## Why This Prompt Was Chosen

I designed the prompt this way for specific reasons:

1.  **Numbered Instructions (`1.`, `2.`)**: This makes it very clear for the AI to follow both steps without missing any.
2.  **Structured Output Format**: The `Sentiment: <result>` format is the most important part. It forces the AI to give a consistent response that my code can easily split and parse into the `ai_sentiment` and `ai_summary` columns. Without this, the AI's answer would be messy and impossible to process automatically.
3.  **One-Sentence Summary**: This tells the AI to be short and direct, which is perfect for a data table.

## Implementation Details

-   **File:** The prompt is used in the `get_ai_analysis(text)` function in `deepseek_enrichment.py`.
-   **Model:** `deepseek-chat`
-   **Temperature:** `0.1` (I used a low value to get more consistent, less creative answers, which is better for data processing).

## Challenges and Solutions

-   **Challenge:** Sometimes the AI ignored my format and wrote a long paragraph instead of using `Sentiment: ...` and `Summary: ...`.
-   **Solution:** I made the prompt more strict and added a `try-except` block in the `parse_ai_response()` function to handle any weird responses without crashing the program.

## Cost and Usage

-   I used the API key from the assignment.
-   The script processed about 10-15 news articles. I added `time.sleep(1)` between calls to avoid overwhelming the API and to stay within rate limits.
