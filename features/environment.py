from utilities.configuration import getConfig
from utilities.resources import Resources
import requests


def after_scenario(context, scenario):
    if "library" in scenario.tags:  # to skip other test cases
        url = getConfig()['API']['endpoint'] + Resources.deleteBook
        headers = {'Content-Type': 'application/json'}
        delresp = requests.post(url, json={"ID": context.id}, headers=headers, )
        dl = delresp.json()
        print("The delete message is:", dl)


def before_scenario(context, scenario):
    print("I am running before scenarios")
