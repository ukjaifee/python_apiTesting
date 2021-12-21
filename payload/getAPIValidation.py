
import requests
import json
from utilities.configuration import getConfig
from utilities.resources import Resources

url=getConfig()['API']['endpoint']+Resources.getBook
print("The url is,", url)
response = requests.get(url, params={'AuthorName': 'Rahul Shetty2'}, )
print(response.status_code)
data = json.loads(response.text) #get data in dictonary

print(type(data))
print(data[0])
for books in data:
    if books['isbn'] == 'abcd':
        print(books['isbn'])

        break

epectedResult = {"book_name": "Devops", "isbn": "abcd", "aisle": "75"}
assert books == epectedResult
# We can convert to json using request.json method as well

rep = response.json()
print(rep[0]['isbn'])
assert response.status_code == 200
assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'
