import os
import subprocess
from datetime import datetime
from glob import glob

import yt_dlp


def create_url(platform: str, platform_ident: str):
    dictt = {
        "youtube": "https://www.youtube.com/watch?v=" + platform_ident,
        "soundcloud": "https://on.soundcloud.com/" + platform_ident
    }
    return dictt[platform]


client_certificate = os.path.dirname(__file__) + "/certificates/proxy.pem"


def download_audio(platform: str, playform_ident: str, metadata: dict, target_dir: str = "output"):
    start_time = datetime.now()
    outtmpl = os.path.join(target_dir, playform_ident)
    ydl_opts = {
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio"
            }
        ],
        "youtube_include_dash_manifest": False,
        "youtube_include_hls_manifest": False,
        "format_sort": ["+size", "+br"],
        "outtmpl": outtmpl,
        # "proxy": "https://brd-customer-hl_1d628cbd-zone-static:drnhbn9ov1wl@brd.superproxy.io:22225",
        # "client_certificate": client_certificate,
        "max_filesize": 52428800
    }
    url = create_url(platform, playform_ident)

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    metadata["download_timing"] = (datetime.now() - start_time).total_seconds()
    return glob(outtmpl + ".*")[0], metadata


def resample_audio(source_file: str, target_file: str, metadata: dict):
    start_time = datetime.now()
    command = "ffmpeg -i {source_file} -b:a 32000 -progress - -v error -y {target_file}"
    command = command.format(source_file=source_file,
                             target_file=target_file)
    result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
    for line in result.stdout.splitlines():
        key, value = line.split('=', 1)
        metadata[key] = value.strip()

    metadata["resampling_time"] = (datetime.now() - start_time).total_seconds()
    return target_file, metadata


def download_and_resample_audio(platform: str, platform_ident: str, metadata: dict, target_dir: str = "output"):
    filepath, metadata = download_audio(platform, platform_ident, metadata, target_dir)
    target_file = os.path.join(target_dir, platform_ident + ".32k.opus")
    return resample_audio(filepath, target_file, metadata)
