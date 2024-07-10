import json
import uuid

from dotenv import load_dotenv

from notefornote import post_analysis_task_result

load_dotenv()

f = open('./fixtures/anlysis.fixture.json')
data = json.load(f)

post_analysis_task_result(str(uuid.uuid4()), data, {
    'download_timing': 12312,
    'analyse_timing': 12312,
    'download_size': 12312
})
