import requests


def send_video_to_group(video_path, video_text, language):

    fr_access_token = 'Enter French account access token'
    fr_phone_number_id = 'Enter French account phone number id'
    fr_group_id = 'Enter French group id'

    en_access_token = 'Enter English account access token'
    en_phone_number_id = 'Enter English account phone number id'
    en_group_id = 'Enter English group id'

    if language == 'en':
        access_token = en_access_token
        phone_number_id = en_phone_number_id
        group_id = en_group_id
    else:
        access_token = fr_access_token
        phone_number_id = fr_phone_number_id
        group_id = fr_group_id


    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
    }

    # Upload the video to get the media ID
    files = {
        'file': ('video.mp4', open(video_path, 'rb'), 'video/mp4'),
    }
    response = requests.post(f'https://graph.facebook.com/v19.0/{phone_number_id}/media', headers={
        'Authorization': f'Bearer {access_token}'
    }, files=files)

    if response.status_code != 200:
        print("Failed to upload video:", response.text)
        return

    media_id = response.json()['id']

    # Send the video to the group
    payload = {
        'messaging_product': 'whatsapp',
        'recipient_type': 'group',
        'to': group_id,
        'type': 'video',
        'video': {
            'id': media_id,
            'caption': video_text
        }
    }

    response = requests.post(f'https://graph.facebook.com/v19.0/{phone_number_id}/messages', headers=headers,
                             json=payload)
    if response.status_code == 200:
        print("Video sent successfully to the group!")
    else:
        print("Failed to send video:", response.text)

# Usage example: send_video_to_group('path_to_video.mp4', 'Here is your video!', 'your_access_token', 'your_phone_number_id', 'group_id')
