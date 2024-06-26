import requests
import time
import logging
import json
import os

TELEGRAM_BOT_TOKEN = "7187014370:AAGsyhz2qwrQ1sLTIpgR23domyxD7rcG6kU"
CHAT_ID = "-1001693900569"
CHANNEL_INFO = {
    # "UCNhaliLwhGH9wX3pe9bFTbA": "LifeofShazzam",
    "UC6-BgjsBa5R3PZQ_kZ8hKPg": "LLOUD Official",
    # "UC9MQp8a5uhaIosZPHaoqEXQ": "CallMeShazzam Vines",
    # "UC9I8DWhqm5q7U_4fhfDwZIw": "Arjyou",
    # "UC3IZKseVpdzPSBaWxBxundA": "HYBE LABELS",
}
YOUTUBE_API_KEY = "AIzaSyDDwH9vMenML_wZPtYssNAZ9n2jAwl_g0I"
POLLING_INTERVAL = 60
LAST_VIDEO_FILE = "ytnotifier/last_video_ids.json"
LOG_FILE = "ytnotifier/youtube_notifier.log"

print("Starting script...")
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

logging.basicConfig(
    filename="ytnotifier/youtube_notifier.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def load_last_video_ids():
    if os.path.exists(LAST_VIDEO_FILE):
        with open(LAST_VIDEO_FILE, "r") as file:
            return json.load(file)
    return {}


def save_last_video_ids(last_video_ids):
    with open(LAST_VIDEO_FILE, "w") as file:
        json.dump(last_video_ids, file)


def get_latest_video(channel_id):
    url = f"https://www.googleapis.com/youtube/v3/search?key={YOUTUBE_API_KEY}&channelId={channel_id}&part=snippet,id&order=date&maxResults=1"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data["items"]:
            vid_id = data["items"][0]["id"]["videoId"]
            vid_title = data["items"][0]["snippet"]["title"]
            return vid_id, vid_title
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching latest video: {e}")
    return None, None


def send_telegram_message(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": msg}
    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error sending message: {e}")


def countdown_timer(interval):
    for remaining in range(interval, 0, -1):
        print(f"Next check in {remaining} seconds...", end="\r")
        time.sleep(1)
    print("Checking for new videos...")


def main():
    last_video_ids = load_last_video_ids()
    logging.info("Starting main loop...")

    while True:
        logging.info("Loop iteration started.")
        for channel_id, channel_name in CHANNEL_INFO.items():
            logging.info(f"Checking channel: {channel_name} (ID: {channel_id})")
            latest_video_id, latest_video_title = get_latest_video(channel_id)
            if latest_video_id:
                logging.info(
                    f"Latest video found: {latest_video_title} (ID: {latest_video_id})"
                )
                if (
                    channel_id not in last_video_ids
                    or last_video_ids[channel_id] != latest_video_id
                ):
                    notify_msg = f"New video from {channel_name}: {latest_video_title}\nhttps://www.youtube.com/watch?v={latest_video_id}"
                    logging.info(f"Sending notification: {notify_msg}")
                    send_telegram_message(notify_msg)
                    last_video_ids[channel_id] = latest_video_id
                    save_last_video_ids(last_video_ids)

        logging.info(f"Sleeping for {POLLING_INTERVAL} seconds...")
        countdown_timer(POLLING_INTERVAL)


if __name__ == "__main__":
    logging.info("Script initialization complete.")
    main()
