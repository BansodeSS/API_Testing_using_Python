import requests
import json
import jsonpath
#url

def test_create_user():

    url = 'https://reqres.in/api/users'

    file = open('TestCases/createUser.json')
    json_input = file.read()
    request_json = json.loads(json_input)


    #send the reuest
    response = requests.post(url,request_json)

    print(response.content)

    print(response.status_code)

    print(response.headers.get('Content-Length'))

    assert  response.status_code == 201

    #print responce into json format

    responce_json = json.loads(response.text)

    #pick id from responce_json

    id = jsonpath.jsonpath(responce_json,'id')
    print(id[0])