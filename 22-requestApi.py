import requests

base_url = 'https://www.jikenext.com'

def get_request(name):
    url = base_url + name
    response = requests.get(url)
    data = response.content.decode('utf-8')
    print(data)
    print(response)


get_request('/course')