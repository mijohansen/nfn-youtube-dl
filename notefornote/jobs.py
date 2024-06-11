import os
import tempfile
from datetime import datetime
from logging import getLogger

from notefornote import create_analysis_task, download_audio, analyze_audio, post_analysis_result

logger = getLogger(__name__)


def do_complete_task():
    task = create_analysis_task()
    download_started = datetime.now()
    target_dir = tempfile.TemporaryDirectory()
    filepath = download_audio(task["platform"],  task["platform_ident"], target_dir.name)
    download_finished = datetime.now()
    genres = analyze_audio(filepath)
    metadata = dict({
        'download_timing': download_finished - download_started,
        'analyse_timing': datetime.now() - download_finished,
        'download_size': os.path.getsize(filepath)
    })
    print(metadata)
    post_analysis_result(task["id"], genres, metadata)

