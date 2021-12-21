from behave import *
import requests
import json
from payload.addBookPaylod import buildPayLoadFormDB, addBookPayload
from utilities.configuration import getConfig, get_query
from utilities.resources import Resources


@given(u'The books details which needs to be added')
def step_impl(context):
    context.headers = {'Content-Type': 'application/json;charset=UTF-8'}
    context.url = getConfig()['API']['endpoint'] + Resources.addBook
    print('The url is' + context.url)


@when('We execute the AddBook PostAPI method')
def step_impl(context):
    query = 'select * from apidevelop.Books'
    context.response = requests.post(context.url, json=addBookPayload("271211345", "27134456"), headers=context.headers, )
    print(context.response)


@then('Book is successfully Added')
def step_impl(context):
    context.res = json.loads(context.response.text)
    print("The status code when running without parameter", context.response.status_code)
    # print("The data is ", context.response['ID'])
    print("The data is ", context.res)
    context.id = context.res['ID']
    # assert id == 'bnid34955'


@when('We execute the AddBook PostAPI with {isbn} and {aisle}')
def step_impl(context, isbn, aisle):
    query = 'select * from apidevelop.Books'
    context.response = requests.post(context.url, json=addBookPayload(isbn, aisle), headers=context.headers, )
    print("The response is", context.response.status_code)


@then('status code of response should be {statusCode:d}')  # for integer give the colon d
def step_impl(context, statusCode):
    print(context.response.status_code)
    assert context.response.status_code == statusCode
