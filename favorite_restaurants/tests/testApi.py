import unittest
import re
from common import apiUtility as api
import getpass
import time

class TestGetAPI(unittest.TestCase):

    def test_01_adding_new_restaurant(self):
        token = api.get_token()
        api.api_call(api.RESTAURANTP, api.POST, api.NEW_RESTAURANT, token)

    def test_02_update_rating(self):
        token = api.get_token()
        api.api_call(api.RESTAURANTP, api.PUT, api.RESTAURANT_UPDATE, token)

    def test_03_delete_first_restaurant(self):
        token = api.get_token()
        restaurant_delete = api.first_restauraunts()
        api.api_call(api.RESTAURANTP, api.DELETE, restaurant_delete, token)

    def test_04_get_restaurants_url_code(self):
        assert api.get_url_status_code(api.RESTAURANTP) == 200
        print("\n Verified GET request return status code for restaurants:", api.get_url_status_code(api.RESTAURANTP))

    def test_05_get_login_error_code(self):
        assert api.get_url_status_code(api.LOGINP) == 405
        print("\n Verified GET request return status code for " + api.LOGINP + ":", api.get_url_status_code(api.LOGINP))

    def test_06_get_error_message(self):
        assert api.get_url_json(api.LOGINP) == api.ERROR_MSG_POST
        print("\n Verified GET request return error message for login:", api.get_url_json(api.LOGINP))

    def test_07_put_empty_restaurant_error_msg(self):
        assert api.api_call_errors(api.RESTAURANTP, api.PUT, '', '', '').json() == api.ERROR_MSG_UNAUT

    def test_08_put_empty_restaurant_error_code(self):
        assert api.api_call_errors(api.RESTAURANTP, api.PUT, '', '', '').status_code == 401

    def test_09_post_error_msg(self):
        assert api.api_call_errors(api.RESTAURANTP, api.POST, '', '', '').json() == api.ERROR_MSG_UNAUT

    def test_10_post_error_code(self):
        assert api.api_call_errors(api.RESTAURANTP, api.POST, '', '', '').status_code == 401

    def test_11_delete_error_msg(self):
        assert api.api_call_errors(api.RESTAURANTP, api.DELETE, '', '', '').json() == api.ERROR_MSG_UNAUT

    def test_12_delete_error_code(self):
        assert api.api_call_errors(api.RESTAURANTP, api.POST, '', '', '').status_code == 401

    def test_13_post_msg_login(self):
        assert re.match(api.REGEX_TOKEN, api.LOGIN_POST.text)
        print("\n Verified POST request return message for login :", api.LOGIN_POST.json())

    def test_14_post_code_login(self):
        assert api.LOGIN_POST.status_code == 200
        print("\n Verified POST request return status code for login:", api.LOGIN_POST.status_code)

if __name__ == '__main__':
   test_results = '/Users/' + getpass.getuser() + '/Desktop/' + time.strftime("%d%m%Y") + '_Test_results.txt'
   f = open(test_results, "w")
   suite = unittest.TestLoader().loadTestsFromTestCase(TestGetAPI)
   unittest.TextTestRunner(f, verbosity=2).run(suite)
   f.close()
