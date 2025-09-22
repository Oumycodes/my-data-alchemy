
# DeepSeek Usage Documentation

## Prompt Used for AI Enrichment

```python
prompt = 
Perform the following tasks on the text below:
1. Analyze the sentiment as either 'Positive', 'Negative', or 'Neutral'.
2. Generate a one-sentence summary.

Return your answer in the exact following format:
Sentiment: <result>
Summary: <result>

Text: {text} 
Why This Prompt Was Chosen
Clear Instructions: The numbered tasks (1. and 2.) make it easy for the AI to understand what is required.

Structured Output: The required format (Sentiment: <result>\nSummary: <result>) is crucial. It allows the Python code to automatically parse the AI's response and add it to the DataFrame as new columns (ai_sentiment, ai_summary). Without this structure, parsing the response would be much harder.

Conciseness: Asking for a "one-sentence summary" guides the AI to be brief and to the point, which is perfect for a dataset summary.

Implementation Details
Function: The prompt is used in the get_ai_analysis(text) function within deepseek_enrichment.py.

Model: deepseek-chat

Temperature: Set to 0.1 to ensure more deterministic and consistent outputs, which is essential for automated data processing.

Challenges and Solutions
Challenge: Initially, the AI would sometimes respond with creative, non-structured answers that were impossible to parse automatically (e.g., "Sure! I'd be happy to help. The sentiment is positive and the summary is...").

Solution: The prompt was refined to be extremely specific about the required format. A robust parsing function (parse_ai_response) with try-except blocks was also added to handle any unexpected responses gracefully.

Cost and Usage
The assignment-provided API key was used (sk-a7f42564324a433b836f39b479e4dfa8).

The pipeline processed approximately 10-15 articles, making a separate API call for each one. With rate limiting (time.sleep(1)), this was a minimal and efficient use of credits.
