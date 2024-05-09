import requests

def upload_video_to_snapchat(video_path, video_text, video_tags, language):
    """
    Uploads a video to Snapchat with specified text and tags.

    Parameters:
    - video_path: str. The file path to the video.
    - video_text: str. Text to accompany the video.
    - video_tags: list. Tags associated with the video.

    Returns:
    - response: Requests response object.
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
        'Authorization': access_token,  # Replace with your actual access token
        'Content-Type': content_type
    }

    # Prepare the data payload, attach video file, text, and tags
    data = {
        'text': video_text,
        'tags': ','.join(video_tags)  # Convert list of tags into a comma-separated string
    }

    # Read the video file in binary mode
    with open(video_path, 'rb') as video_file:
        files = {
            'video': video_file
        }
        response = requests.post(url, headers=headers, files=files, data=data)

    return response

# Example usage
if __name__ == "__main__":
    video_path = "path/to/your/video.mp4"
    video_text = "Check out this cool video!"
    video_tags = ["fun", "snapchat", "video"]

    response = upload_video_to_snapchat(video_path, video_text, video_tags)
    print(response.status_code, response.json())
