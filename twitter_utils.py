import tweepy


def upload_video(video_path, video_text, video_tags, language):
    # Twitter credentials
    fr_api_key = 'Enter your French account API key'
    fr_api_secret_key = 'Enter your French account API secret key'
    fr_access_token = 'Enter your French account access token'
    fr_access_token_secret = 'Enter your French account access token secret'

    en_api_key = 'Enter your English account API key'
    en_api_secret_key = 'Enter your English account API secret key'
    en_access_token = 'Enter your English account access token'
    en_access_token_secret = 'Enter your English account access token secret'

    if language == 'en':
        API_KEY = en_api_key
        API_SECRET_KEY = en_api_secret_key
        ACCESS_TOKEN = en_access_token
        ACCESS_TOKEN_SECRET = en_access_token_secret
    else:
        API_KEY = fr_api_key
        API_SECRET_KEY = fr_api_secret_key
        ACCESS_TOKEN = fr_access_token
        ACCESS_TOKEN_SECRET = fr_access_token_secret


    # Authenticate to Twitter
    auth = tweepy.OAuth1UserHandler(
        API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
    )
    api = tweepy.API(auth)

    # Upload the video
    media = api.media_upload(video_path, media_category='tweet_video')

    # Create the status with tags
    hashtags = ' '.join(f'#{tag}' for tag in video_tags)
    status = f"{video_text} {hashtags}"

    # Post tweet with video
    api.update_status(status=status, media_ids=[media.media_id])

# Example usage (you'll usually call this from another script)
if __name__ == "__main__":
    video_path = "path_to_your_video.mp4"
    video_text = "Check out this great video!"
    video_tags = ["tag1", "tag2"]
    upload_video(video_path, video_text, video_tags)
