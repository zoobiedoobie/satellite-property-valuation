import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

MAPBOX_TOKEN = os.getenv("MAPBOX_TOKEN")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
IMAGE_DIR = os.path.join(BASE_DIR, "images")


def download_images(split="train", zoom=16, size="256x256"):
    """
    split: 'train' or 'test'
    Downloads satellite images for each row
    """
    assert split in ["train", "test"]

    df = pd.read_csv(os.path.join(DATA_DIR, f"{split}.csv"))

    out_dir = os.path.join(IMAGE_DIR, split)
    os.makedirs(out_dir, exist_ok=True)

    for idx, row in df.iterrows():
        lat = row["lat"]
        lon = row["long"]

        url = (
            f"https://api.mapbox.com/styles/v1/mapbox/satellite-v9/static/"
            f"{lon},{lat},{zoom}/"
            f"{size}?access_token={MAPBOX_TOKEN}"
        )

        file_path = os.path.join(out_dir, f"{idx}.png")

        if os.path.exists(file_path):
            continue

        response = requests.get(url)
        if response.status_code == 200:
            with open(file_path, "wb") as f:
                f.write(response.content)
        else:
            print(f"Failed at index {idx}")

    print(f"Downloaded images for {split} set")
     response = requests.get(url, timeout=10)
    if idx % 50 == 0:
    print(f"Downloaded {idx}/{len(df)} images")

