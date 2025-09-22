# DeepSeek Usage Documentation

## Prompt Used for AI Enrichment
Perform the following tasks on the text below:

Analyze the sentiment as either 'Positive', 'Negative', or 'Neutral'.

Generate a one-sentence summary.

Return your answer in the exact following format:
Sentiment: <result>
Summary: <result>


## Why This Prompt Was Chosen

I designed this prompt for specific technical reasons:
- **Numbered Instructions (1., 2.)**: Makes the AI process both tasks systematically without missing steps
- **Structured Output Format**: The "Sentiment: <result>" format is crucial for automated parsing - it enables my code to split the response into clean DataFrame columns (ai_sentiment, ai_summary)
- **One-Sentence Summary**: Ensures concise, database-friendly outputs rather than lengthy paragraphs

## Implementation Details

- **Location**: Used in get_ai_analysis(text) function in deepseek_enrichment.py
- **Model**: deepseek-chat
- **Temperature**: 0.1 (low value for consistent, reproducible outputs ideal for data processing)
- **Headers**: Included authorization and content-type headers as required by API

## Challenges and Solutions

- **Challenge**: AI occasionally returned free-form responses instead of the specified format
- **Solution**: Added try-except blocks in parse_ai_response() function to handle irregular responses gracefully without crashing the pipeline
- **Challenge**: API rate limiting with multiple rapid requests
- **Solution**: Implemented time.sleep(1) between requests to maintain stable API usage

## Cost and Usage

- Used provided API key: sk-a7f42564324a433b836f39b479e4dfa8
- Processed approximately 10-15 news articles total
- Added rate limiting (1-second delay between calls) to avoid exceeding API limits
- Total cost: Minimal usage within free tier limits
