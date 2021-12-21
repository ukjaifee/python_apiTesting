import json

import requests
import json
url = 'https://petstore.swagger.io/v2/pet/9843217/uploadImage'
file = {'file': open('C:\\Users\\Umesh_Kumar\\Documents\\test.txt', 'rb')}

req = requests.post(url, files=file)
print(req.text)
print(req.json())
#datta=json.loads(req.txt)
#print(type(datta))