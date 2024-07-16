from datetime import datetime

from notefornote import download_and_resample_audio, print_json

# Youtube
# afrobeat dj settet: j-FKO0ZGBHw
# psykedelic indie rock: 8QrzHqmWgwQ
# koffee: 0Cmzn8BIOdA
# music influencer: siHfCV6vuSc
# download_audio("youtube", "siHfCV6vuSc")

# SoundCloud: https://on.soundcloud.com/zZeY7rWqdncdKq8d7

start_time = datetime.now()
metadata = download_and_resample_audio("soundcloud", "zZeY7rWqdncdKq8d7", {})
# metadata = download_audio("youtube", "0Cmzn8BIOdA")

print_json(metadata)

print({"timing": (datetime.now() - start_time).total_seconds()})
