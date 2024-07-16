import os
import tempfile
from datetime import datetime
from logging import getLogger

from notefornote import post_download_task_result, fetch_download_task, download_and_resample_audio, fetch_analysis_task
from notefornote.upload import upload_file_to_b2

logger = getLogger(__name__)


def perform_download_task():
    task = fetch_download_task()
    target_dir = tempfile.TemporaryDirectory()
    filepath, metadata = download_and_resample_audio(task["platform"], task["platform_ident"], {}, target_dir.name)
    started = datetime.now()
    upload_data = upload_file_to_b2(upload_url=task["upload_url"],
                                    authorization=task["authorization"],
                                    platform=task["platform"],
                                    filepath=filepath)

    metadata['upload_timing'] = (datetime.now() - started).total_seconds()
    metadata['download_size'] = os.path.getsize(filepath)

    post_download_task_result(task["task_id"], upload_data, metadata)


def perform_analysis_task():
    task = fetch_analysis_task()

    analysis_data = perform_analysis(task["platform"], task["platform_ident"], {})
    metadata = {}
    post_analysis_task_result(task["task_id"], analysis_data, metadata)
