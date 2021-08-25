import requests

#url
url = 'https://reqres.in/api/users/2'

#send the reuest
response = requests.delete(url)

print(response.status_code)

assert  response.status_code == 204