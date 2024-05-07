import tweepy
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler


def twitter_auth():
    """Authenticate with the Twitter API."""
    consumer_key = 'mikkro7qtjGh6KW2174LoBjD8'
    consumer_secret = 'ttpOn0ZMGQyq3GEET2Co93ifnHB8rBov9bNF0xZ08pLNdCvWuS'
    access_token = '1787956662562701312-A3GvrXwcTazOe8cbpTWZE6GKh23lVn'
    access_token_secret = 'uXbWA1myLUjbWtxNC25FGsP0j5NFLUEWpR05GhD63E5mK'

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
file_path = '../VideoDirectory/TestVideo.mp4'
text = 'Here is my new video!'
schedule_time = datetime.strptime('2024-08-05 01:52:00', '%Y-%m-%d %H:%M:%S')

# Schedule the video tweet
schedule_tweet(api, file_path, text, schedule_time)
