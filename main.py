from facebook_utils import *
import instagram
import Snapchat
import TikTok
import twitter
import whatsapp

video_path_English = input("Input video path for English account: ")
time_English = input("Input schedule time in this format YYYY-MM-DD HH:MM:SS: ")
scheduled_time_English = int(time.mktime(time.strptime(time_English, "%Y-%m-%d %H:%M:%S")))
description_English = input("Type your description: ")


# video_path_French = input("Input video path for French account: ")
# time_France = input("Input schedule time in this format YYYY-MM-DD HH:MM:SS: ")
# scheduled_time_French = int(time.mktime(time.strptime(time_France, "%Y-%m-%d %H:%M:%S")))
# description_French = input("Type your description: ")

facebook_utils.upload_video_to_facebook(description=description_English, scheduled_time=scheduled_time_English)
