from moviepy.editor import *

# Load the two video files
clip1 = VideoFileClip("video/reddit/test1.mp4")
clip2 = VideoFileClip("video/relax/test1.mp4").subclip(10).without_audio()

# Set the duration of the final video to the longer of the two videos
# lowest_duration = min([clip1.duration, clip2.duration])


# Set the size of the final video to the width of the first video and the height of both videos combined
final_size = (clip1.size[0], clip1.size[1] + clip2.size[1])


# Create a CompositeVideoClip by stacking the two video clips and the black background
final_clip = CompositeVideoClip([clip1,  clip2.set_position((0, clip1.size[1]))], size=final_size)

# Set the duration of the final video to the longer of the two videos
if clip1.duration> clip2.duration:
    final_clip.duration = clip2.duration
if clip1.duration< clip2.duration:
    final_clip.duration = clip1.duration
else:
    print("Something went wrong")

final_clip = CompositeVideoClip([clip1,  clip2.set_position((0, clip1.size[1]))], size=final_size)

# Export the final video to a file
final_clip.write_videofile("video/final_video/finally.mp4", fps=30)

# clip_duration = 60

# # Get the total duration of the final video in seconds
# total_duration = final_clip.duration

# # Calculate the number of clips needed to cover the entire duration of the video
# num_clips = int(total_duration // clip_duration) + 1

# # Loop through each clip and export it to a separate video file
# for i in range(num_clips):
#     start_time = i * clip_duration
#     end_time = min((i + 1) * clip_duration, total_duration)
#     clip = final_clip.subclip(start_time, end_time)
#     clip.write_videofile(f"clip_{i}.mp4", fps=30)
