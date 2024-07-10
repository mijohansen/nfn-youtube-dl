from notefornote import upload_file

token = {
    "authorizationToken": '4_003e286d105c2fe0000000001_01b51cd0_2313b4_upld_rNJDg38mvDoLwsEUjbL5Jo3ZFMM=',
    "bucketId": '4ef25836cd8100259c020f1e',
    "uploadUrl": 'https://pod-031-2006-13.backblaze.com/b2api/v3/b2_upload_file/4ef25836cd8100259c020f1e/c003_v0312006_t0009'
}


test_filepath = "../output/zZeY7rWqdncdKq8d7.32k.opus"


result = upload_file(token["uploadUrl"], token["authorizationToken"], test_filepath, "soundcloud")

print(result)
