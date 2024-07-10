import hashlib
import os

import requests


# https://www.backblaze.com/apidocs/b2-upload-file


def upload_file(upload_url, authorization, filepath, service):
    headers = {
        'Authorization': authorization,
        "Content-Type": "audio/opus",
        "Content-Length": os.path.getsize(filepath).to_bytes(4, 'big'),
        "X-Bz-Content-Sha1": get_digest(filepath),
        "X-Bz-File-Name": service + "/" + os.path.basename(filepath),
    }

    with open(filepath, 'rb') as payload:
        response = requests.post(upload_url, headers=headers, data=payload)
        return response.json()


def get_digest(file_path):
    h = hashlib.sha1()

    with open(file_path, 'rb') as file:
        while True:
            # Reading is buffered, so we can read smaller chunks.
            chunk = file.read(h.block_size)
            if not chunk:
                break
            h.update(chunk)

    return h.hexdigest()
