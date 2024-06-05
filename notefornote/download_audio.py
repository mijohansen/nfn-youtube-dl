import yt_dlp
import os


def create_url(service: str, asset_id: str):
    dictt = {
        "youtube": "https://www.youtube.com/watch?v=" + asset_id,
        "soundcloud": "https://on.soundcloud.com/" + asset_id
    }
    return dictt[service]


def download_audio(service: str, asset_id: str, target_dir: str = "output"):
    outtmpl = os.path.join(target_dir, asset_id)
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
        "outtmpl": outtmpl,
        "max_filesize": 52428800
        # "keepvideo": True,
    }
    url = create_url(service, asset_id)

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return outtmpl + ".m4a"
