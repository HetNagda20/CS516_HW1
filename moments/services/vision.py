import os
import requests
from typing import List, Tuple

API = os.getenv("VISION_API", "azure")
KEY = os.getenv("VISION_KEY")
ENDPOINT = os.getenv("VISION_ENDPOINT")

def describe_and_label(image_path: str) -> Tuple[str, List[str]]:
    if not (API and KEY and ENDPOINT):
        return "", []

    with open(image_path, "rb") as f:
        data = f.read()

    if API == "azure":
        url = (
            f"{ENDPOINT}/computervision/imageanalysis:analyze"
            f"?api-version=2024-02-01&features=caption,tags"
        )
        headers = {
            "Ocp-Apim-Subscription-Key": KEY,
            "Content-Type": "application/octet-stream",
        }
        r = requests.post(url, headers=headers, data=data, timeout=20)
        r.raise_for_status()
        j = r.json()
        caption = (j.get("captionResult") or {}).get("text") or ""
        tags = [t["name"] for t in (j.get("tagsResult") or {}).get("values", [])]
        return caption, tags

    return "", []
