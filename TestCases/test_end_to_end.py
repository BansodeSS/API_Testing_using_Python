import requests
import json
import jsonpath
#url

def test_Add_new_student():

    url = 'https://reqres.in/api/users'

    file = open('TestCases/createUser.json')
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url,json_input)
    id = jsonpath.jsonpath(response.json(),'id')
    print(id)
