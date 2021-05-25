import requests
from requests.auth import HTTPBasicAuth
import json

class Test_CAW:

    def test_get_method(self):
        url='https://reqres.in/api/users?page=2'
        response = requests.get(url)
        assert response.status_code==200, 'failed to get users data'

    def test_post_method(self):
        url = 'https://reqres.in/api/users'
        new_user={
            "name": "manoj reddy alluri",
            "job": "Automation tester"
        }
        response = requests.post(url, new_user)
        assert response.status_code == 201, 'Failed to register with reqres'

    def test_put_method(self):
        url='https://reqres.in/api/users/2'
        updated_user={
            "name": "morpheus",
            "job": "zion resident"
            }
        response = requests.put(url, updated_user)
        assert response.status_code == 200, 'Failed to register with reqres'

    def test_delete_method(self):
        url='https://reqres.in/api/users/2'
        response=requests.delete(url)
        assert response.status_code==204, 'failed to delete user 2'

    def test_basic_authenctication(self):
        url='https://reqres.in/api/register'
        user_data={
                "email": "eve.holt@reqres.in",
                "password": "cityslicka"
            }
        response=requests.post(url, user_data)
        assert response.status_code==200, 'Failed to register with reqres'
        token=json.loads(response.text)['token']
        response=requests.get('https://reqres.in/api/login', auth=HTTPBasicAuth(token, ''))
        assert response.status_code == 200, 'Failed to login with reqres'

    def test_404_resource_not_found(self):
        url='https://reqres.in/api/users/23'
        response = requests.get(url)
        assert response.status_code==404, 'resource was not found'

    def test_400_authenication(self):
        url='https://reqres.in/api/register'
        register_details={
            "email": "sydney@fife"
            }
        response = requests.post(url, register_details)
        assert response.status_code==200, response.text

    def test_401_status_code(self):
        url='https://api.github.com/user'
        response = requests.get(url)
        assert response.status_code == 200, response.text
