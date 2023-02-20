from TikTokApi import TikTokApi

# Initialize the TikTok API object
api = TikTokApi()

# Log in to your TikTok account
username = "your_username"
password = "your_password"
api.login(username, password)

# Set the video file path, caption, and hashtags
video_file = "path/to/your/video.mp4"
caption = "This is my TikTok video uploaded via Python!"
hashtags = ["python", "tiktok", "coding"]

# Upload the video
video_data = api.upload_video(video_file)
response = api.post_video(video_data["upload_id"], caption=caption, hashtags=hashtags)

# Check if the video was uploaded successfully
if response["status_code"] == 0:
    print("Video uploaded successfully!")
else:
    print(f"Error uploading video: {response['status_msg']}")
