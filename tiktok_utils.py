import requests

def upload_video(video_path, video_text, video_tags, language):
    """
    Uploads a video to TikTok with the specified text and tags.

    Args:
    video_path (str): Path to the video file.
    video_text (str): Text to accompany the video.
    video_tags (list of str): List of tags for the video.
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
        "Authorization":  access_token,
        "Content-Type": content_type
    }
    data = {
        'text': video_text,
        'tags': ','.join(video_tags)
    }
    files = {
        'video': open(video_path, 'rb')
    }

    response = requests.post(url, headers=headers, files=files, data=data)
    if response.status_code == 200:
        print("Video uploaded successfully!")
        return response.json()
    else:
        print(f"Failed to upload video: {response.text}")
        return None

if __name__ == "__main__":
    # Example usage:
    video_path = "path_to_your_video.mp4"
    video_text = "Check out my new video!"
    video_tags = ["tag1", "tag2"]
    upload_video(video_path, video_text, video_tags)
