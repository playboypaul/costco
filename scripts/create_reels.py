import json
from moviepy.editor import ImageClip, concatenate_videoclips, TextClip

with open("../data/posts.json") as f:
    posts = json.load(f)

clips = []
for i, post in enumerate(posts):
    img_path = f"../images/generated/{i}_final.png"
    clip = ImageClip(img_path).set_duration(3)
    text = TextClip(post['deal']['title'], fontsize=24, color='white').set_position('bottom').set_duration(3)
    clips.append(clip)

video = concatenate_videoclips(clips, method="compose")
video.write_videofile("../reels/generated/reel.mp4", fps=24)
print("Reel generated")
