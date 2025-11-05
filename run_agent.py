import subprocess

subprocess.run(["python", "scripts/scrape_deals.py"])
subprocess.run(["python", "scripts/generate_captions.py"])
subprocess.run(["python", "scripts/create_images.py"])
subprocess.run(["python", "scripts/create_reels.py"])
subprocess.run(["python", "scripts/post_content.py"])
