import requests
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

def upload_video(access_token, video_path, open_id, client_key):
    """Uploads a video file to TikTok."""
    url = 'https://open-api.tiktok.com/video/upload/'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    files = {
        'video': open(video_path, 'rb')
    }
    data = {
        'open_id': open_id,
        'client_key': client_key
    }
    response = requests.post(url, headers=headers, files=files, data=data).json()
    return response

def post_video(access_token, video_id, text, open_id, client_key):
    """Posts an uploaded video to TikTok."""
    url = 'https://open-api.tiktok.com/video/create/'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    data = {
        'video_id': video_id,
        'text': text,
        'open_id': open_id,
        'client_key': client_key
    }
    response = requests.post(url, headers=headers, data=data).json()
    return response

def schedule_video_upload(access_token, video_path, text, open_id, client_key, schedule_time):
    """Schedules a video to be uploaded and posted at a specific time."""
    scheduler = BackgroundScheduler()
    job = scheduler.add_job(
        lambda: upload_and_post_video(access_token, video_path, text, open_id, client_key),
        'date',
        run_date=schedule_time
    )
    scheduler.start()
    return job

def upload_and_post_video(access_token, video_path, text, open_id, client_key):
    """Uploads and posts a video to TikTok."""
    upload_response = upload_video(access_token, video_path, open_id, client_key)
    if 'video_id' in upload_response:
        video_id = upload_response['video_id']
        post_response = post_video(access_token, video_id, text, open_id, client_key)
        print('Post Response:', post_response)
    else:
        print('Error in uploading video:', upload_response)

# Example usage
access_token = 'YOUR_ACCESS_TOKEN'
open_id = 'YOUR_OPEN_ID'
client_key = 'YOUR_CLIENT_KEY'
video_path = 'path/to/your/video.mp4'
text = 'Your video description'
schedule_time = datetime.strptime('2024-05-01 15:00:00', '%Y-%m-%d %H:%M:%S')

# Schedule the video to be uploaded and posted
job = schedule_video_upload(access_token, video_path, text, open_id, client_key, schedule_time)
print(f"Video upload scheduled, job id: {job.id}")
