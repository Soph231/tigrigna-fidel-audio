import os
import unicodedata

# This script runs in your local repo directory
def sanitize_filename(filename):
    name, ext = os.path.splitext(filename)
    safe_name = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore').decode('ascii')
    return f"{safe_name}{ext}"

for filename in os.listdir('.'):
    if filename.endswith(".mp3"):
        safe_name = sanitize_filename(filename)
        if filename != safe_name:
            os.rename(filename, safe_name)
            print(f"Renamed: {filename} → {safe_name}")
