## Prompt Used for AI Enrichment

```python
prompt = f"""
Perform the following tasks on the text below:
1. Analyze the sentiment as either 'Positive', 'Negative', or 'Neutral'.
2. Generate a one-sentence summary.

Return your answer in the exact following format:
Sentiment: <result>
Summary: <result>

Text: {text}
"""

