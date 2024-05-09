import requests


def upload_video(video_path, video_text, video_tags, language):
    """
    Uploads a video to Threads API with accompanying text and tags.

    Args:
    video_path (str): The file path of the video to upload.
    video_text (str): The text to accompany the video.
    video_tags (list): A list of tags to include with the video.

    Returns:
    dict: A response from the server.
    """
    fr_url = 'Enter your French account Placeholder URL'
    fr_access_token = 'Enter your French account Bearer access token'
    fr_content_type = 'Enter your content type for French account'

    en_url = 'Enter your English account Placeholder URL'
    en_access_token = 'Enter your English account Bearer access token'
    en_content_type = 'Enter your content type for English account'

    if language == 'en':
        url = en_url
        access_token = en_access_token
        content_type = en_content_type
    else:
        url = fr_url
        access_token = fr_access_token
        content_type = fr_content_type

    headers = {
        "Authorization": access_token,
        "Content-Type": content_type
    }

    # Prepare tags as a string if required by the API
    tags_string = ",".join(video_tags)

    # Open the video file in binary mode
    with open(video_path, 'rb') as video_file:
        files = {
            'video': (video_path, video_file),
            'text': (None, video_text),
            'tags': (None, tags_string)
        }

        # Make the POST request to upload the video
        response = requests.post(url, headers=headers, files=files)

    # Check for request success and handle response
    if response.status_code == 200:
        return response.json()  # Or appropriate response handling
    else:
        response.raise_for_status()  # Raise an error if unsuccessful

# Example usage (this line should be in the calling script, not here):
# upload_video("path/to/video.mp4", "Check out this great video!", ["fun", "threads"])
