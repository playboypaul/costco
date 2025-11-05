import json
from transformers import pipeline

generator = pipeline("text-generation", model="gpt4all-lora-quantized.bin")

with open("../data/deals.json") as f:
    deals = json.load(f)["deals"]

posts = []
for deal in deals[:5]:
    prompt = f"Create an Instagram caption for this Costco deal: {deal['title']} at {deal['price']}. Include 10 relevant hashtags."
    caption = generator(prompt, max_length=100)[0]['generated_text']
    posts.append({"deal": deal, "caption": caption})

with open("../data/posts.json", "w") as f:
    json.dump(posts, f, indent=2)
print("Generated captions for top deals")
