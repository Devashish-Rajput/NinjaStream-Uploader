################### NinjaStream Uploader #################
import os

import requests
import json

url = "https://api.ninjastream.to/api/file/upload/generate"

path='Your path to files' # add path your video files
filepaths = [os.path.join(path, file) for file in os.listdir(path)]
data = { 'apiId' : "Your Apid ",
         'apiSecretId' : "Your apisecretid"
        }

r = requests.post(url,data=data)
print(r)
resp = json.loads(r.text)
print(resp)
x=resp['result']

for z in filepaths:
    file = { 'file':open(z, 'rb') }

    r = requests.post(x, files=file,data=data)
    resp = json.loads(r.text)
    print(resp)
