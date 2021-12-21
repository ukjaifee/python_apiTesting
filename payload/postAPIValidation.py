import requests
import json
import configparser
from payload.addBookPaylod import addBookPayload, buildPayLoadFormDB
from utilities.configuration import getConfig
from utilities.resources import Resources

config = configparser.ConfigParser()

config.read('utilities/properties.ini')
url = getConfig()['API']['endpoint'] + Resources.addBook
headers = {'Content-Type': 'application/json;charset=UTF-8'}


def getID():
    query = 'select * from customerinfo'
    resp = requests.post(url, json=buildPayLoadFormDB(query), headers=headers)
    print(resp.json())
    print(type(resp.json()))
    dic = resp.json()
    print(dic['ID'])
    id = dic['ID']
    print(id)
    return id


# Delete Book

print(getID())
