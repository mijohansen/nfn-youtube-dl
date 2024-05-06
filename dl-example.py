import yt_dlp
from datetime import datetime

def create_url(service: str, asset_id: str):
    dictt = {
        "youtube": "https://www.youtube.com/watch?v=" + asset_id,
    }
    return dictt[service]


def download_audio(service: str, asset_id: str):
    ydl_opts = {
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "m4a",
            }
        ],
        "youtube_include_dash_manifest": False,
        "youtube_include_hls_manifest": False,
        "format_sort": ["+size", "+br"],
        "outtmpl": "output/test",
    }
    url = create_url(service, asset_id)

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


start_time = datetime.now()
download_audio("youtube", "j-FKO0ZGBHw")
print(datetime.now() - start_time)
