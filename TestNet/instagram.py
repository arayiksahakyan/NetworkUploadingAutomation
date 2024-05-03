import requests
import os
import time
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

def create_media_container(access_token, instagram_account_id, video_url, caption):
    """Creates a media container for a video on Instagram that can be later published."""
    url = f'https://graph.facebook.com/v14.0/{instagram_account_id}/media'
    payload = {
        'media_type': 'VIDEO',
        'video_url': video_url,
        'caption': caption,
        'access_token': access_token
    }
    response = requests.post(url, data=payload).json()
    return response

def publish_media_container(access_token, instagram_account_id, creation_id):
    """Publishes a previously created media container to Instagram."""
    url = f'https://graph.facebook.com/v14.0/{instagram_account_id}/media_publish'
    payload = {
        'creation_id': creation_id,
        'access_token': access_token
    }
    response = requests.post(url, data=payload).json()
    return response

def schedule_post(access_token, instagram_account_id, creation_id, schedule_time):
    """Schedules the publishing of a media container at a specified time."""
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        publish_media_container,
        'date',
        run_date=schedule_time,
        args=[access_token, instagram_account_id, creation_id]
    )
    scheduler.start()
    print(f"Post scheduled at {schedule_time}, which is {schedule_time - datetime.now()} from now.")

# Example usage
access_token = 'YOUR_LONG_LIVED_ACCESS_TOKEN'
instagram_account_id = 'YOUR_INSTAGRAM_ACCOUNT_ID'
video_url = 'URL_OF_THE_VIDEO_TO_UPLOAD'
caption = 'Your caption here'
schedule_time = datetime.strptime('2024-05-01 15:00:00', '%Y-%m-%d %H:%M:%S')  # Time when you want to publish

# Create the video container
container_response = create_media_container(access_token, instagram_account_id, video_url, caption)
if 'id' in container_response:
    creation_id = container_response['id']
    # Schedule the video to be published
    schedule_post(access_token, instagram_account_id, creation_id, schedule_time)
else:
    print('Error in creating video container:', container_response)
