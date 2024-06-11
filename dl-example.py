import os
from datetime import datetime

from notefornote import download_audio

# Youtube
# afrobeat dj settet: j-FKO0ZGBHw
# psykedelic indie rock: 8QrzHqmWgwQ
# koffee: 0Cmzn8BIOdA
# music influencer: siHfCV6vuSc
# download_audio("youtube", "siHfCV6vuSc")

# SoundCloud: https://on.soundcloud.com/zZeY7rWqdncdKq8d7

start_time = datetime.now()
filepath = download_audio("soundcloud", "zZeY7rWqdncdKq8d7")
download_filesize = os.path.getsize(filepath)
print({"download_filesize": download_filesize})
print({"download_filepath": filepath})
print({"timing": datetime.now() - start_time})
