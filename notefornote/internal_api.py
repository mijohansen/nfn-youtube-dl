import logging
import os

import requests

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def get_auth_header():
    token = os.getenv("CLIENT_TOKEN")
    return {'Authorization': 'Bearer ' + token}


def make_analysis_service_url(path):
    analysis_server = os.getenv("ANALYSIS_SERVER")
    return analysis_server + path


def fetch_download_task():
    url = make_analysis_service_url("/media-analysis-service/process/next-download-task")
    response = requests.post(url, headers=get_auth_header())
    if response.status_code != 200:
        raise Exception("Can't fetch next download task.", response, url)
    task = response.json()
    logger.info(msg="Fetched new task: {}".format(task))
    return task


def post_download_task_result(task_id, data, metadata):
    url = make_analysis_service_url("/media-analysis-service/download-task/:taskId/complete").replace(":taskId", task_id)
    print({"url": url, "metadata": metadata})
    response = requests.post(url, json=dict(data=data, metadata=metadata), headers=get_auth_header())
    print({"response": response})
    return response.json()


def fetch_analysis_task():
    url = make_analysis_service_url("/media-analysis-service/process/next-analysis-task")
    response = requests.post(url, headers=get_auth_header())
    if response.status_code != 200:
        raise Exception("Can't fetch analysis task.", response, url)
    task = response.json()
    logger.info(msg="Fetched new task: {}".format(task))
    return task


def post_analysis_task_result(task_id, data, metadata):
    url = make_analysis_service_url("/media-analysis-service/analysis-task/:taskId/complete").replace(":taskId", task_id)
    print({"url": url, "metadata": metadata})
    response = requests.post(url, json=dict(data=data, metadata=metadata), headers=get_auth_header())
    print({"response": response})
    return response.json()


