import json

# load method parse json string and return a dictionary
learning_course = '{"name": "Umesh","languages": ["Java", "Python"]}'
courses = json.loads(learning_course)
# print(type(courses))
# print(courses['name'])
list_lang = courses["languages"]
# print(type(list_lang))
# print(list_lang[0])

with open("C:\\Users\\Umesh_Kumar\\Documents\\Json\\courses.json") as f:
    dataJ = json.load(f)
    # print(dataJ)
    dictory = {}
    print(dataJ['courses'][1]['title'])
    print(dataJ['dashboard']['website'])
    listdat = dataJ['courses']
    print(type(listdat))
    for i in listdat:
        # print(i['title'])
        if i['title'] == 'RPA':
            print("found the required course")
            print(i['price'])
            break

with open("C:\\Users\\Umesh_Kumar\\Documents\\Json\\courses.json") as f1:
    dataJ1 = json.load(f1)
    print(dataJ == dataJ1)
    assert dataJ == dataJ1
