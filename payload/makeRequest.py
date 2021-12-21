import requests
import json


class requestMaker:

    def make_request(self, request_type, url, headers, body=None):
        res = self.http_reqest(request_type,url, headers)
        return res

    def http_reqest(self, request_type, url, headers, body):
        if request_type == 'GET':
            respose = requests.get(url, params=None, timeout=10, verify=False, header=header)
        elif request_type == 'POST':
            reponse = requests.post(url, headers=headers, json=body)
        return reponse
