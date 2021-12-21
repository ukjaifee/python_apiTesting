import requests
import json
from addBookPaylod import *

from payload.postAPIValidation import getID
from utilities.configuration import getConfig
from utilities.resources import Resources

url = getConfig()['API']['endpoint'] + Resources.deleteBook
headers = {'Content-Type': 'application/json'}
deleteResp = requests.post(url, json={"ID": getID()}, headers=headers, )
dl = deleteResp.json()
print(dl['msg'])
