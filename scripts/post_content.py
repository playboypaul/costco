from instagrapi import Client
import json

cl = Client()
cl.login("YOUR_USERNAME", "YOUR_PASSWORD")

with open("../data/posts.json") as f:
    posts = json.load(f)

for i, post in enumerate(posts):
    cl.photo_upload(
        f"../images/generated/{i}_final.png",
        post['caption']
    )
print("Posts uploaded to Instagram")
