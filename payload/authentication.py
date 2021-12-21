import requests


def loginGit():
    se=requests.session()
    se.auth=auth=('ukjaifee@gmail.com', 'dhiman741@@')
    request = se.get('https://api.github.com/user')
    print(request.status_code)
    print()

loginGit()



