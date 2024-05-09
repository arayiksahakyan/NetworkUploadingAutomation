import requests


def create_media_container(access_token, instagram_user_id, video_path, video_text, video_tags):
    url = f"https://graph.facebook.com/v19.0/{instagram_user_id}/media"
    payload = {
        'media_type': 'VIDEO',
        'video_url': video_path,
        'caption': f"{video_text} {' '.join(['#' + tag for tag in video_tags])}",
        'access_token': access_token
    }
    response = requests.post(url, data=payload)
    return response.json()


def publish_media(access_token, instagram_user_id, creation_id):
    url = f"https://graph.facebook.com/v19.0/{instagram_user_id}/media_publish"
    payload = {
        'creation_id': creation_id,
        'access_token': access_token
    }
    response = requests.post(url, data=payload)
    return response.json()


def upload_video(video_path, video_text, video_tags, language):
    fr_access_token = 'Enter French account access token'
    fr_instagram_user_id = 'Enter your French account page id'

    en_access_token = 'Enter English account access token'
    en_instagram_user_id = 'Enter your English account page id'

    if language == 'en':
        access_token = en_access_token
        instagram_user_id = en_instagram_user_id
    else:
        access_token = fr_access_token
        instagram_user_id = fr_instagram_user_id

    # Create the media container
    container_response = create_media_container(access_token, instagram_user_id, video_path, video_text, video_tags)
    if 'id' in container_response:
        creation_id = container_response['id']
        # Publish the media
        publish_response = publish_media(access_token, instagram_user_id, creation_id)
        return publish_response
    else:
        return container_response

