import requests
import random
from winotify import Notification, audio
import time


def get_online_quote():
    response = requests.get("https://type.fit/api/quotes", timeout=10)
    response.raise_for_status()
    quotes = response.json()
    quote = random.choice(quotes)
    return quote.get("text", "Keep pushing forward!")


def show_notification(message):
    toast = Notification(
        app_id="Daily Motivation Assistant",
        title="Daily Motivation",
        msg=message,
        icon=None,       # optional icon path
        duration="long"  # 'long' ensures it stays visible
    )
    toast.set_audio(audio.Default, loop=False)
    toast.show()
    print(message)


# For testing: 3 alerts, 10-second interval
alerts_per_day = 3
interval_seconds = 10

for _ in range(alerts_per_day):
    message = get_online_quote()
    show_notification(message)
    time.sleep(interval_seconds)
