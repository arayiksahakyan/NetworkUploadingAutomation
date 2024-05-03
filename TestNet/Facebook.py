import requests
import os
import time

def upload_video_to_facebook(access_token, page_id, video_path, description="", scheduled_time=None):
    # Initialize the upload session
    url = f"https://graph.facebook.com/v14.0/{page_id}/videos"
    payload = {
        'access_token': access_token,
        'upload_phase': 'start',
        'file_size': os.path.getsize(video_path)
    }
    response = requests.post(url, data=payload).json()
    upload_session_id = response['upload_session_id']
    video_id = response['video_id']

    # Upload the video chunks
    with open(video_path, 'rb') as video_file:
        bytes_sent = 0
        while bytes_sent < os.path.getsize(video_path):
            chunk = video_file.read(2000000)  # Read 2MB at a time
            payload = {
                'access_token': access_token,
                'upload_phase': 'transfer',
                'start_offset': bytes_sent,
                'upload_session_id': upload_session_id,
                'video_file_chunk': chunk
            }
            response = requests.post(url, files=payload).json()
            bytes_sent += len(chunk)

    # Finish the upload
    finish_payload = {
        'access_token': access_token,
        'upload_phase': 'finish',
        'upload_session_id': upload_session_id
    }
    if scheduled_time:
        finish_payload['scheduled_publish_time'] = scheduled_time
    response = requests.post(url, data=finish_payload).json()

    # Optionally, update the video details
    if description:
        update_url = f"https://graph.facebook.com/v14.0/{video_id}"
        payload = {
            'access_token': access_token,
            'description': description
        }
        requests.post(update_url, data=payload)

    return video_id

# Usage
access_token = 'YOUR_ACCESS_TOKEN'
page_id = 'YOUR_PAGE_ID'
video_path = 'path/to/your/video.mp4'
description = "Here is a new video!"
scheduled_time = int(time.mktime(time.strptime("YYYY-MM-DD HH:MM:SS", "%Y-%m-%d %H:%M:%S")))  # Set the exact time
video_id = upload_video_to_facebook(access_token, page_id, video_path, description, scheduled_time)
print(f"Video scheduled with ID: {video_id}")
