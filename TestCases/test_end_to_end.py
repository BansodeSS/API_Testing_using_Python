import requests
import json
import jsonpath
#url

def test_Add_new_student():

    url = 'http://www.thetestingworldapi.com/api/studentsDetails'
    file = open('C:\\Users\\Sangfroid Solutions\\PycharmProjects\\API_Testing_using_Python\\TestCases\\createUser.json','r')
    request_json = json.loads(file.read())
    print(request_json)
    response = requests.post(url,request_json)
    print(response.content)
    id = jsonpath.jsonpath(response.json(),'id')
    print(id[0])

    technical_detilas_url = 'http://www.thetestingworldapi.com/api/technicalskills'
    file = open('C:\\Users\\Sangfroid Solutions\\PycharmProjects\\API_Testing_using_Python\\TestCases\\technical_data.json','r')
    request_json = json.loads(file.read())
    request_json['id']=int(id[0])
    request_json['st_id'] = id[0]
    response = requests.post(technical_detilas_url,request_json)
    print(response.text)


    address_detilas_url = 'http://www.thetestingworldapi.com/api/addresses'
    file = open('C:\\Users\\Sangfroid Solutions\\PycharmProjects\\API_Testing_using_Python\\TestCases\\address_data.json','r')
    request_json = json.loads(file.read())

    request_json['stId'] = id[0]

    response = requests.post(address_detilas_url,request_json)
    print(response.text)

    final_details = 'http://www.thetestingworldapi.com/api/FinalStudentDetails/'+str(id[0])
    response = requests.get(final_details)
    print(response.text)


test_Add_new_student()