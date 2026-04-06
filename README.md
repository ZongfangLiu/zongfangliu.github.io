Personal homepage for Zongfang Liu.

Photography gallery:

- Put photos in `images/photograpy/`.
- Use filenames in the format `Location_Country_Year.jpg`.
- If you have multiple photos from the same place/time, use `Location_Country_Year_1.jpg`, `Location_Country_Year_2.jpg`, etc. The suffix is ignored in captions.
- After adding or renaming photos, run:

```bash
python scripts/generate_photo_manifest.py
```

This updates `images/photograpy/photos.json`, which is used by the website to render the rolling gallery automatically.
