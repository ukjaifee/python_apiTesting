import requests
from behave import *

from utilities.resources import Resources


@given(u'I have the github Auth cedentails')
def step_impl(context):
    context.se = requests.session()
    # context.se.auth = auth = (getConfig()['CredCredentials']['userName'], getConfig()['CredCredentials']['password'])
    context.se.auth = auth = ('ukjaifee@gmail.com', 'dhiman741@@')


@when('I hit the gitRep API of GITHUB')
def step_impl(context):
    context.response = context.se.get(Resources.giturl)


@then('status code of response should be {statusCode:d}')  # for integer give the colon d
def step_impl(context, statusCode):
    print(context.response.json().status_code)
    assert context.response.json().status_code == statusCode
