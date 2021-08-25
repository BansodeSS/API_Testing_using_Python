import requests

#url
url = 'https://reqres.in/api/users?page=2'

#send the reuest
response = requests.get(url)

print(response.content)

