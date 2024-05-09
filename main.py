import sched
import time
import datetime
import facebook_utils
import instagram_utils
import whatsapp_utils
import threads_utils
import tiktok_utils
import snapchat_utils
import twitter_utils

scheduler = sched.scheduler(time.time, time.sleep)

def start_upload(video_path, video_text, video_tags, language):
    print(f"Uploading video: {video_text} at {datetime.datetime.now()}")
    facebook_utils.upload_video_to_facebook(video_path, video_text, video_tags, language)
    instagram_utils.upload_video(video_path, video_text, video_tags, language)
    whatsapp_utils.send_video_to_group(video_path, video_text, language)
    threads_utils.upload_video(video_path, video_text, video_tags, language)
    tiktok_utils.upload_video(video_path, video_text, video_tags, language)
    snapchat_utils.upload_video_to_snapchat(video_path, video_text, video_tags, language)
    twitter_utils.upload_video(video_path, video_text, video_tags, language)

def schedule_video_uploads(video_list):
    for video in video_list:
        video_time = datetime.datetime.fromisoformat(video['date'].rstrip('Z')).timestamp()
        current_time = time.time()
        delay = video_time - current_time
        if delay > 0:  # Schedule future uploads only
            scheduler.enter(delay, 1, start_upload, argument=(video['video_path'], video['video_text'], video['video_tags'], video['date'], video['language']))

def get_video_list_input(list_name, language):
    video_list = []
    num_videos = int(input(f"Enter the number of videos for {list_name}: "))
    for i in range(num_videos):
        print(f"Entering details for video {i+1} of {list_name}")
        video_path = input("Enter video path: ")
        video_text = input("Enter video text: ")
        video_tags = input("Enter video tags: ")
        date_input = input("Enter the date for the video (YYYY-MM-DD): ")
        date = datetime.datetime.strptime(date_input, '%Y-%m-%d').isoformat() + 'Z'  # Formatting date in ISO 8601 format
        video_dict = {
            'video_path': video_path,
            'video_text': video_text,
            'video_tags': video_tags,
            'date': date,
            'language': language
        }
        video_list.append(video_dict)
    return video_list

def create_global_list(en_list, fr_list):
    global_list = en_list + fr_list
    return global_list

def sort_videos_by_date(video_list):
    # Sort the videos by date in ascending order
    return sorted(video_list, key=lambda x: datetime.datetime.fromisoformat(x['date'].rstrip('Z')))

# Get user input for each list
en_list = get_video_list_input("English account", 'en')
fr_list = get_video_list_input("French account", 'fr')

# Create and sort the global list
global_list = create_global_list(en_list, fr_list)
sorted_global_list = sort_videos_by_date(global_list)

# Schedule the video uploads
schedule_video_uploads(sorted_global_list)
scheduler.run()  # Start the scheduler to execute scheduled uploads
