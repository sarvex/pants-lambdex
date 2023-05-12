import hashlib

import requests


def handler(event, context):
    url = event["url"]
    print(f"{url} sha256:{hashlib.sha256(requests.get(url).content).hexdigest()}")


def other_handler(event, context):
    print("Other handler invoked")
