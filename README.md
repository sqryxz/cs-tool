# AI Support Ticket Summarizer

A minimal Python tool that uses DeepSeek's AI to automatically summarize customer support tickets.

## Setup

1. Clone this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory with your DeepSeek API key:
   ```
   DEEPSEEK_API_KEY=your_api_key_here
   ```

## Usage

Run the script with:
```bash
python ticket_summarizer.py
```

The script includes an example ticket by default. To use it with your own tickets, you can modify the `example_ticket` variable in the `main()` function or import the `summarize_ticket()` function into your own code:

```python
from ticket_summarizer import summarize_ticket

ticket_content = """Your ticket content here"""
summary = summarize_ticket(ticket_content)
print(summary)
```

## Features

- Uses DeepSeek's chat model for high-quality summaries
- Compatible with OpenAI's API format
- Handles error cases gracefully
- Configurable through environment variables
- Easy to integrate into existing systems

## Requirements

- Python 3.6+
- DeepSeek API key (get one at https://platform.deepseek.com)
- Required packages listed in requirements.txt 