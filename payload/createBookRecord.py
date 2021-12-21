import json

import requests

from payload.addBookPaylod import buildPayLoadFormDB, addBookPayload
from payload.makeRequest import requestMaker

from utilities.configuration import getConfig
from utilities.resources import Resources


def create_Book():
    headers = {'Content-Type': 'application/json;charset=UTF-8'}
    url = getConfig()['API']['endpoint'] + Resources.addBook
    print('The url is' + url)
    query = 'select * from Books'
    re = requests.post(url, json=buildPayLoadFormDB(query), headers=headers,)
    print(re.text)
    data = json.loads(re.text)
    #print(data['ID'])


#create_Book()


