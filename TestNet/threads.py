import requests
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

def create_media_container(access_token, account_id, image_url, caption):
    """Creates a media container on Threads that can be later published."""
    url = f'https://graph.instagram.com/v14.0/{account_id}/media'
    payload = {
        'image_url': image_url,
        'caption': caption,
        'access_token': access_token,
        'is_for_threads': True  # Hypothetical parameter
    }
    response = requests.post(url, data=payload).json()
    return response

def publish_media_container(access_token, account_id, creation_id):
    """Publishes a previously created media container on Threads."""
    url = f'https://graph.instagram.com/v14.0/{account_id}/media_publish'
    payload = {
        'creation_id': creation_id,
        'access_token': access_token,
        'is_for_threads': True  # Hypothetical parameter
    }
    response = requests.post(url, data=payload).json()
    return response

def schedule_post(access_token, account_id, creation_id, schedule_time):
    """Schedules the publishing of a media container at a specified time."""
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        publish_media_container,
        'date',
        run_date=schedule_time,
        args=[access_token, account_id, creation_id]
    )
    scheduler.start()
    print(f"Post scheduled at {schedule_time}")

# Example usage
access_token = 'YOUR_ACCESS_TOKEN'
account_id = 'YOUR_ACCOUNT_ID'
image_url = 'URL_OF_THE_IMAGE_TO_UPLOAD'
caption = 'Your caption here'
schedule_time = datetime.strptime('2024-05-01 15:00:00', '%Y-%m-%d %H:%M:%S')

# Create the media container
container_response = create_media_container(access_token, account_id, image_url, caption)
if 'id' in container_response:
    creation_id = container_response['id']
    # Schedule the media to be published
    schedule_post(access_token, account_id, creation_id, schedule_time)
else:
    print('Error in creating media container:', container_response)
