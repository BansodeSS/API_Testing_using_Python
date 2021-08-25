import requests
import json
import jsonpath
#url
url = 'https://reqres.in/api/users?page=2'

#send the reuest
response = requests.get(url)

json_responce = json.loads(response.text)

#print(json_responce)

pages = jsonpath.jsonpath(json_responce,"total_pages")
#print(pages)

assert  pages[0] == 4