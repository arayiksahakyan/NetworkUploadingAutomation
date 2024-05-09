import requests
import json

def upload_video_to_facebook(video_path, video_text, video_tags, language):
    """
    Uploads a video to Facebook with the specified parameters.

    Args:
    access_token (str): Access token for the Facebook API.
    page_id (str): The ID of the Facebook page where the video will be uploaded.
    video_path (str): Path to the video file.
    video_text (str): Text to be included with the video.
    video_tags (list): Tags to be included with the video.

    Returns:
    dict: Response from the Facebook API.
    """
    fr_access_token = 'Enter French account access token'
    fr_page_id = 'Enter your French account page id'

    en_access_token = 'Enter English account access token'
    en_page_id = 'Enter your English account page id'

    if language == 'en':
        access_token = en_access_token
        page_id = en_page_id
    else:
        access_token = fr_access_token
        page_id = fr_page_id


    url = f"https://graph.facebook.com/v19.0/{page_id}/videos"
    payload = {
        'description': video_text,
        'access_token': access_token
    }
    tags = ','.join(video_tags)
    files = {
        'source': (video_path, open(video_path, 'rb')),
        'tags': (None, tags),
    }

    response = requests.post(url, data=payload, files=files)
    return response.json()

if __name__ == "__main__":
    # Example usage:
    access_token = 'YOUR_ACCESS_TOKEN'
    page_id = 'YOUR_PAGE_ID'
    video_path = 'path/to/your/video.mp4'
    video_text = 'Check out our new video!'
    video_tags = ['tag1', 'tag2']

    result = upload_video_to_facebook(access_token, page_id, video_path, video_text, video_tags)
    print(json.dumps(result, indent=4))
