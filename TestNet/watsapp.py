import requests
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

def send_whatsapp_message(token, phone_number, media_id, message):
    """Send a video message through WhatsApp Business API."""
    url = 'https://graph.facebook.com/v13.0/YOUR_PHONE_NUMBER_ID/messages'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    data = {
        'messaging_product': 'whatsapp',
        'to': phone_number,
        'type': 'video',
        'video': {
            'id': media_id
        },
        'text': {
            'body': message
        }
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

def schedule_whatsapp_message(token, phone_number, media_id, message, schedule_time):
    """Schedule a WhatsApp message to be sent at a specific time."""
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        send_whatsapp_message,
        'date',
        run_date=schedule_time,
        args=[token, phone_number, media_id, message]
    )
    scheduler.start()
    print(f"Message scheduled to be sent at {schedule_time}")

# Example usage
token = 'YOUR_ACCESS_TOKEN'
phone_number = 'CUSTOMER_PHONE_NUMBER'
media_id = 'MEDIA_ID_OF_UPLOADED_VIDEO'
message = 'Check out our new video!'
schedule_time = datetime.strptime('2024-05-01 15:00:00', '%Y-%m-%d %H:%M:%S')

# Schedule the WhatsApp message
schedule_whatsapp_message(token, phone_number, media_id, message, schedule_time)
