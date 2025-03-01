import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def summarize_ticket(ticket_content):
    """
    Summarize a customer support ticket using DeepSeek's model.
    
    Args:
        ticket_content (str): The full content of the support ticket
        
    Returns:
        str: A concise summary of the ticket
    """
    try:
        url = "https://api.deepseek.com/v1/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.getenv('DEEPSEEK_API_KEY')}"
        }
        
        data = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant that summarizes customer support tickets. Create brief, actionable summaries that capture the main issue and any key details."},
                {"role": "user", "content": f"Please summarize this support ticket:\n\n{ticket_content}"}
            ],
            "max_tokens": 150,
            "temperature": 0.5
        }
        
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        result = response.json()
        return result['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error generating summary: {str(e)}"

def main():
    # Example usage
    example_ticket = """
    Subject: Mobile App Sync Issues & Data Loss After Latest Update

    Dear Support,

    I'm experiencing serious issues with your mobile app since the update to version 2.5.1 
    released three days ago. Here are the specific problems I'm encountering:

    1. App crashes when trying to sync large files (over 50MB)
    2. Previously synced documents are showing as "pending" but never complete
    3. Some of my folder structures have disappeared completely
    4. The offline mode is not working at all

    I've already tried:
    - Uninstalling and reinstalling the app
    - Clearing the cache and app data
    - Logging out and back in
    - Restarting my device (Samsung Galaxy S23)

    This is severely impacting my work as I manage construction project documents 
    through your platform. I have an important client meeting tomorrow and need 
    access to these files urgently.

    Device Details:
    - Phone: Samsung Galaxy S23
    - Android Version: 14
    - App Version: 2.5.1
    - Account Type: Business Premium
    - User ID: BUS_789012

    Please help resolve this ASAP.

    Best regards,
    Sarah Chen
    Project Manager
    """
    
    print("Original Ticket:")
    print("-" * 50)
    print(example_ticket)
    print("\nGenerated Summary:")
    print("-" * 50)
    print(summarize_ticket(example_ticket))

if __name__ == "__main__":
    main() 