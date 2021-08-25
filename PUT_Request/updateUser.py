import requests
import json
import jsonpath
#url
url = 'https://reqres.in/api/users/2'

file = open('UpdatedData.json')
json_input = file.read()
request_json = json.loads(json_input)


#send the reuest
response = requests.put(url,request_json)

print(response.content)

#print(response.status_code)

#print(response.headers.get('Content-Length'))

assert  response.status_code == 202

#print responce into json format

response_json = json.loads(response.text)

#pick id from responce_json
print(response_json)

updated = jsonpath.jsonpath(response_json,'updatedAt')
print(updated)