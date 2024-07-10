import os
import subprocess
from datetime import datetime
from glob import glob

import yt_dlp


def create_url(service: str, asset_id: str):
    dictt = {
        "youtube": "https://www.youtube.com/watch?v=" + asset_id,
        "soundcloud": "https://on.soundcloud.com/" + asset_id
    }
    return dictt[service]


client_certificate = os.path.dirname(__file__) + "/certificates/proxy.pem"


def download_audio(service: str, asset_id: str, target_dir: str = "output"):
    outtmpl = os.path.join(target_dir, asset_id)
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
    url = create_url(service, asset_id)

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return glob(outtmpl + ".*")[0]


def resample_audio(source_file: str, target_file: str):
    start_time = datetime.now()
    command = "ffmpeg -i {source_file} -b:a 32000 -progress - -v error -y {target_file}"
    command = command.format(source_file=source_file,
                             target_file=target_file)
    metadata = {"source_filepath": source_file, "target_filepath": target_file}
    result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
    for line in result.stdout.splitlines():
        key, value = line.split('=', 1)
        metadata[key] = value.strip()
    resampled_timing = datetime.now() - start_time
    metadata["resampling_time"] = resampled_timing.total_seconds()
    return metadata


def download_and_resample_audio(service: str, asset_id: str, target_dir: str = "output"):
    filepath = download_audio(service, asset_id, target_dir)
    target_file = os.path.join(target_dir, asset_id + ".32k.opus")
    return resample_audio(filepath, target_file)
