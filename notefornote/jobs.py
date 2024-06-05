import json
import tempfile

from notefornote import get_next_analysis_task, download_audio, analyze_audio, post_analysis_result


def do_complete_task():
    task = get_next_analysis_task()
    target_dir = tempfile.TemporaryDirectory()
    filepath = download_audio(task["platform"],  task["platform_ident"], target_dir.name)
    genres = analyze_audio(filepath)
    return post_analysis_result(task["id"], genres)

