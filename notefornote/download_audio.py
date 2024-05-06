import yt_dlp
import os
import tempfile


def create_url(service: str, asset_id: str):
    dictt = {
        "youtube": "https://www.youtube.com/watch?v=" + asset_id,
        "soundcloud": "https://on.soundcloud.com/" + asset_id
    }
    return dictt[service]


def download_audio(service: str, asset_id: str):
    temp_dir = tempfile.TemporaryDirectory()
    outtmpl = os.path.join(temp_dir.name, asset_id)
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
        # "keepvideo": True,
    }
    url = create_url(service, asset_id)

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return outtmpl + ".m4a"
