import instaloader
from datetime import datetime
import os

loader = instaloader.Instaloader()

loader.dirname_pattern = "{target}"
loader.download_pictures = True
loader.download_videos = True
loader.download_video_thumbnails = False
loader.save_metadata = False
loader.download_geotags = False
# loader.post_metadata_txt_pattern = "{caption}"
loader.save_captions = False

username = "goblinxalgo999"
password = "!$1RalwcAq"
loader.login(username, password)

target_users = ["lalalalisa_m", "wearelloud", "jennierubyjane"]

start_date = datetime(2024, 9, 1)
user_paths = {
    "lalalalisa_m": "/run/media/sreeramp96/MAIN/SREERAM/BACKUP CODES/4K Stogram/lalalalisa_m",
    "wearelloud": "/run/media/sreeramp96/MAIN/SREERAM/BACKUP CODES/4K Stogram/wearelloud",
    "jennierubyjane": "/run/media/sreeramp96/MAIN/SREERAM/BACKUP CODES/4K Stogram/jennierubyjane",
    # "sreeramp96": "/home/sreeramp96/Downloads"
}

for target_user, user_directory in user_paths.items():
    print(f"Downloading for {target_user}")

    if not os.path.exists(user_directory):
        os.makedirs(user_directory)

    profile = instaloader.Profile.from_username(loader.context, target_user)

    loader.dirname_pattern = user_directory
    for post in profile.get_posts():
        if post.date >= start_date:
            loader.download_post(post, target_user)

    if profile.has_public_story:
        for story in loader.get_stories(userids=[profile.userid]):
            for item in story.get_items():
                if item.date_utc >= start_date:
                    loader.download_storyitem(item, target_user)

print("Download complete for all users!")
