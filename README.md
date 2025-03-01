# AI Support Ticket Summarizer 🎫

A lightweight Python tool that uses DeepSeek's AI to automatically generate concise, actionable summaries of customer support tickets. Perfect for support teams looking to quickly understand ticket content and prioritize responses.

## 🌟 Features

- **AI-Powered Summaries**: Leverages DeepSeek's chat model for intelligent ticket analysis
- **Structured Output**: Generates well-organized summaries highlighting key issues and details
- **Easy Integration**: Simple Python interface that can be integrated into existing support systems
- **Error Handling**: Robust error handling for API calls and input processing
- **Configurable**: Adjustable parameters for summary length and AI response style

## 🚀 Quick Start

### Prerequisites

- Python 3.6+
- DeepSeek API key ([Get one here](https://platform.deepseek.com))

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sqryxz/cs-tool.git
   cd cs-tool
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment:
   ```bash
   cp .env.template .env
   ```
   Then edit `.env` and add your DeepSeek API key:
   ```
   DEEPSEEK_API_KEY=your_api_key_here
   ```

### Usage

#### Basic Usage
```python
from ticket_summarizer import summarize_ticket

ticket = """
Subject: Cannot access account
Hi Support, I can't log in to my account since yesterday.
I've tried resetting my password but still getting errors.
User ID: 12345
"""

summary = summarize_ticket(ticket)
print(summary)
```

#### Command Line
Run the script with the included example:
```bash
python ticket_summarizer.py
```

## 📝 Example Output

### Input Ticket
```
Subject: Mobile App Sync Issues & Data Loss After Latest Update

Dear Support,

I'm experiencing serious issues with your mobile app since the update to version 2.5.1 
released three days ago. Here are the specific problems I'm encountering:

1. App crashes when trying to sync large files (over 50MB)
2. Previously synced documents are showing as "pending"
3. Some of my folder structures have disappeared
4. The offline mode is not working at all

[...]
```

### Generated Summary
```
**Summary:**
- User experiencing multiple issues after app update to v2.5.1
- Key problems: large file sync crashes, pending documents, missing folders
- Device: Samsung Galaxy S23, Android 14
- Impact: Urgent - needed for client meeting
- Troubleshooting already attempted: app reinstall, cache clear, device restart
```

## 🛠️ Configuration

The summarizer can be configured by adjusting these parameters in `summarize_ticket()`:

- `max_tokens`: Controls summary length (default: 150)
- `temperature`: Controls creativity vs consistency (default: 0.5)
- System prompt: Can be modified to change summary style and focus

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔒 Security Note

Never commit your `.env` file or expose your API keys. The `.gitignore` file is set up to prevent this, but always be careful when pushing changes. 