import requests

se = requests.session()
se.cookies.update({'visit-month': 'Jan'})
cookies = {'visit-year': '2022'}
requests = se.get('https://httpbin.org/cookies', cookies=cookies)
res = requests.json()
print(res)

# Redirection/timeout -Incase API takes time to redirection
se.cookies.update({'visit-month': 'Jan'})
cookie = {'visit-year': '2022'}
response = requests.get('http://rahulshettyacademy.com/', allow_redirects=False, cookies=cookie, timeout=1)
print(response.history)
print(response.status_code)
