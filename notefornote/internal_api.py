import logging
import os

import requests

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def get_auth_header():
    token = os.getenv("CLIENT_TOKEN")
    return {'Authorization': 'Bearer ' + token}


def create_analysis_task():
    analysis_server = os.getenv("ANALYSIS_SERVER")
    url = analysis_server + "/media-analysis-service/create-analysis-task"
    response = requests.post(url, headers=get_auth_header())
    if response.status_code != 200:
        raise Exception("Can't create analysis task", response, url)
    task = response.json()
    logger.info(msg="Created new task: {}".format(task))
    return task


def post_analysis_result(media_id, data, metadata):
    analysis_server = os.getenv("ANALYSIS_SERVER")
    url = analysis_server + "/media-analysis-service/media/:mediaId/analysis-data".replace(":mediaId", media_id)
    print({"url": url, "metadata": metadata})
    response = requests.post(url, json=dict(data=data, metadata=metadata), headers=get_auth_header())
    print({"response": response})
    return response.json()
