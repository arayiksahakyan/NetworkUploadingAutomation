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
access_token = 'EAAF40l6ZBZAAoBOywS3WaNnhwcud7Xj4YuntZAEnvVc4Ut8kviJhZBZCEnMJ78Y090GcdDj5ZCaL3Gmy9jPnJ9DzJ4lZBuMEAdaoZA51sFIBGM5Qi8ScGML0bGPR0zYOYcCekvIe83v8KvKMYAipZCNr97VxXmf9FMr4F7tRdmzQQm6lmTBIoSFczyCfb6u6aVZCXZAtPFZCCYgZAzaczWxR1ujgpjpuJ4O3STpZBfr6eLKlk5GMYHmxGI4hlSxHmVj1IHcHijUvdjKwZDZD'
page_id = '122108159030294266'
video_path = r'../VideoDirectory/TestVideo.mp4'
description = "Here is a new video!"
scheduled_time = int(time.mktime(time.strptime("2024-05-5 16:02:00", "%Y-%m-%d %H:%M:%S")))  # Set the exact time
video_id = upload_video_to_facebook(access_token, page_id, video_path, description, scheduled_time)
print(f"Video scheduled with ID: {video_id}")
