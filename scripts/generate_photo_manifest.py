#!/usr/bin/env python3

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
PHOTO_DIR = ROOT / "images" / "photograpy"
OUTPUT = PHOTO_DIR / "photos.json"
IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png", ".webp", ".JPG", ".JPEG", ".PNG", ".WEBP"}


def prettify_token(token: str) -> str:
    mapping = {
        "uae": "UAE",
    }
    return mapping.get(token.lower(), token.replace("-", " "))


def parse_metadata(path: Path) -> dict:
    stem_parts = path.stem.split("_")
    if (
        len(stem_parts) >= 4
        and stem_parts[-1].isdigit()
        and stem_parts[-2].isdigit()
        and len(stem_parts[-2]) == 4
    ):
        stem_parts = stem_parts[:-1]

    if len(stem_parts) < 3:
        raise ValueError(f"Unsupported photo filename format: {path.name}")

    year = stem_parts[-1]
    country = prettify_token(stem_parts[-2])
    location = " ".join(prettify_token(part) for part in stem_parts[:-2])
    caption = f"{location}, {country} · {year}"

    return {
        "src": f"images/photograpy/{path.name}",
        "alt": caption,
        "caption": caption,
        "year": int(year),
        "location": location,
    }


def main() -> None:
    photos = []
    for path in sorted(PHOTO_DIR.iterdir()):
        if path.suffix not in IMAGE_SUFFIXES:
            continue
        photos.append(parse_metadata(path))

    photos.sort(key=lambda item: (-item["year"], item["location"], item["src"]))

    for item in photos:
        item.pop("year", None)
        item.pop("location", None)

    OUTPUT.write_text(json.dumps(photos, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
