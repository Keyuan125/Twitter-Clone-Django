from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User

LOGIN_URL = '/api/accounts/login/'
LOGOUT_URL = '/api/accounts/logout/'
LOGIN_STATUS_URL = '/api/accounts/login_status/'
SIGNUP_URL = '/api/accounts/signup/'
TEST_USERNAME = 'admin111'
TEST_PASSWORD = 'randomtest'
TEST_EMAIL = 'huangkeyuan125@gmail.com'

class AccountApiTests(TestCase):
    def setUp(self):
        # This funciton will be called each time the test function runs
        self.client = APIClient()
        self.user = self.createUser(
            username = TEST_USERNAME,
            email = TEST_EMAIL,
            password = TEST_PASSWORD,
        )

    # This is just a helper function so that we don't need to 
    # write create_user each time
    def createUser(self, username, email, password):
        return User.objects.create_user(username, email, password)

    # Test login
    def test_login(self):
        # Every test function should be started with 'test_', otherwise
        # it won't run automatically 

        # 1. Must be POST request, otherwise return status code 405
        response = self.client.get(LOGIN_URL, {
            'username': self.user.username,
            'password': TEST_PASSWORD
        })

        self.assertEqual(response.status_code, 405)

        # 2-1. Check empty, if any of the field is empty, 
        #    return status code 400
        response = self.client.post(LOGIN_URL, {
            'username': '',
            'password': self.user.password
        })

        self.assertEqual(response.status_code, 400)

        # 2-2. 
        response = self.client.post(LOGIN_URL, {
            'username': self.user.password,
            'password': ''
        })

        self.assertEqual(response.status_code, 400)

        # 3. Login with correct password, should return 200
        response = self.client.post(LOGIN_URL, {
            'username': self.user.username,
            # Cannot do self.user.password here because it's a encrypted value
            'password': TEST_PASSWORD
        })
        # print(self.user.password)
        # print("error code", response.data)
        self.assertEqual(response.status_code, 200)


        # 4. Login with correct username but random password
        #    should return 400
        response = self.client.post(LOGIN_URL, {
            'username': TEST_USERNAME,
            'password': 'some random pw'
        })
        self.assertEqual(response.status_code, 400)


    def test_logout(self):
        # 1. Test with GET method, will give 405
        response = self.client.get(LOGOUT_URL, {
            'username': TEST_USERNAME
        })

        self.assertEqual(response.status_code, 405)


        # 2. Test with random username, logout api will always return 200
        response = self.client.post(LOGOUT_URL, {
            'username': 'random user name'
        })

        self.assertEqual(response.status_code, 200)
        
        # 3. Test with login and logout, first login, check login status, 
        #    then logout, and check login status
        self.client.post(LOGIN_URL, {
            'username': TEST_USERNAME,
            'password': TEST_PASSWORD
        })

        is_login = self.client.get(LOGIN_STATUS_URL, {
            'username': TEST_USERNAME
        }).data['has_logged_in']

        self.assertEqual(is_login, True)

        self.client.post(LOGOUT_URL, {
            'username': TEST_USERNAME,
        })

        is_login = self.client.get(LOGIN_STATUS_URL, {
            'username': TEST_USERNAME
        }).data['has_logged_in']

        self.assertEqual(is_login, False)








    def test_login_status(self):
        response = self.client.get(LOGIN_STATUS_URL, {
            'username': TEST_USERNAME
        })
        # print(response.data)
        self.assertEqual(response.data['has_logged_in'], False)

        # ------ Log in with password ------
        response = self.client.post(LOGIN_URL, {
            'username': self.user.username,
            'password': TEST_PASSWORD
        })

        response = self.client.get(LOGIN_STATUS_URL, {
            'username': TEST_USERNAME
        })
        # print(response.data)
        self.assertEqual(response.data['has_logged_in'], True)
