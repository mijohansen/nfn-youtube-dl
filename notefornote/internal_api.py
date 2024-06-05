import requests


def get_next_analysis_task():
    url = "http://localhost:3453/media-analysis-service/next-analysis-task"
    response = requests.get(url)
    return response.json()


def post_analysis_result(media_id, data):
    url = "http://localhost:3453/media-analysis-service/media/:mediaId/analysis-data".replace(":mediaId", media_id)
    print(url)
    response = requests.post(url, json=data)
    print(response)
    return response.json()
