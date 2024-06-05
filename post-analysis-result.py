from notefornote import post_analysis_result
import json
import uuid

f = open('./fixtures/anlysis.fixture.json')
data = json.load(f)

post_analysis_result(str(uuid.uuid4()), data)
