################### NinjaStream Uploader #################
import os

import requests
import json

url = "https://api.ninjastream.to/api/file/upload/generate"

path='/content/drive/MyDrive/myBot1/'
filepaths = [os.path.join(path, file) for file in os.listdir(path)]
data = { 'apiId' : "vhkK7NrGb2NYlFv3QgLHDhA6w2rDq6U6KEhgqNAMnCXxKHUAOt",
         'apiSecretId' : "vH9wTA5lkXtoGDEkFpwPCar85VL4t5JN8XeafVav1WsYCYASLj"
        }

r = requests.post(url,data=data)
print(r)
resp = json.loads(r.text)
print(resp)
x=resp['result']

for z in filepaths:
  if z.find('.ipynb')==-1:
    file = { 'file':open(z, 'rb') }

    r = requests.post(x, files=file,data=data)
    resp = json.loads(r.text)
    print(resp)