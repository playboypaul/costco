import os
import json
import requests
from PIL import Image, ImageDraw, ImageFont

os.makedirs("../images/generated", exist_ok=True)

with open("../data/posts.json") as f:
    posts = json.load(f)

for i, post in enumerate(posts):
    img_data = requests.get(post['deal']['img']).content
    img_path = f"../images/generated/{i}.png"
    with open(img_path, 'wb') as f_out:
        f_out.write(img_data)

    img = Image.open(img_path)
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    draw.text((10, 10), f"{post['deal']['title']} - {post['deal']['price']}", font=font, fill="white")
    img.save(f"../images/generated/{i}_final.png")
print("Images generated with text overlay")
