import tweepy
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler


def twitter_auth():
    """Authenticate with the Twitter API."""
    consumer_key = 'YOUR_CONSUMER_KEY'
    consumer_secret = 'YOUR_CONSUMER_SECRET'
    access_token = 'YOUR_ACCESS_TOKEN'
    access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    return api


def upload_video(api, file_path):
    """Upload video to Twitter."""
    media = api.media_upload(file_path, media_category='tweet_video')
    return media.media_id


def create_tweet(api, media_id, text):
    """Create a tweet with video."""
    tweet = api.update_status(status=text, media_ids=[media_id])
    return tweet


def schedule_tweet(api, file_path, text, schedule_time):
    """Schedule the tweet to be posted at a specific time."""
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        lambda: tweet_video(api, file_path, text),
        'date',
        run_date=schedule_time
    )
    scheduler.start()
    print(f"Tweet scheduled at {schedule_time}")


def tweet_video(api, file_path, text):
    """Helper function to handle the tweet process."""
    media_id = upload_video(api, file_path)
    tweet = create_tweet(api, media_id, text)
    print(f"Tweet posted: {tweet.id}")


# Example usage
api = twitter_auth()
file_path = 'path/to/your/video.mp4'
text = 'Here is my new video!'
schedule_time = datetime.strptime('2024-05-01 15:00:00', '%Y-%m-%d %H:%M:%S')

# Schedule the video tweet
schedule_tweet(api, file_path, text, schedule_time)
