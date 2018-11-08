import json
import requests
import random, string

URL = 'http://localhost:5000'
LOGINP = '/login'
RESTAURANTP = '/favorite_restaurants'
H = {'Content-type': 'application/json'}
RANDOM = ''.join(random.choice(string.ascii_uppercase) for _ in range(8))
RESTAURANT_UPDATE = {"restaurant":"Tocaya","rating":5}
NEW_RESTAURANT = {"restaurant": RANDOM, "rating":5}
VALID_USER = {'username': 'AdventurousEater', 'password': '1234'}
REGEX_TOKEN = '\{\n.*"token":\s\".{64}\"\n\}'
LOGIN_POST = requests.post(URL+ '/login', headers=H, json=VALID_USER)
RESTAURANTS_GET = requests.get(URL + '/favorite_restaurants')
GET = "GET"
POST = "POST"
PUT = "PUT"
DELETE = "DELETE"
ERROR_MSG_POST = {'error': 'Method not allowed. Make a POST request with a valid username and password'}
ERROR_MSG_UNAUT = {'error': 'Unauthorized'}

def api_call(endpoint, method, data, token):
    headers = {"Content-Type": "application/json", "x-chownow-auth-token": token,
               'username': 'AdventurousEater', 'password': '1234'}
    r = None
    if method is POST:
        r = requests.post(URL + endpoint, data=json.dumps(data), headers=headers)
        print("\n Verified POST request, after add should be :", get_restauraunts())
    elif method is DELETE:
        r = requests.delete(URL + endpoint, params=data, headers=headers)
        print("\n Verified DELETE request, after delete should be :", get_restauraunts())
    elif method is PUT:
        r = requests.put(URL + endpoint, json=data, headers=headers)
        print("\n Verified PUT request, after update should be :", get_restauraunts())
    elif method is GET:
        r = requests.get(URL + endpoint, headers=headers)
    assert r.status_code == 200 or 201
    print("\n Verified "+ method +" request return status code :", r.status_code)
    return r

def api_call_errors(endpoint, method, data, token, password):
    headers = {"Content-Type": "application/json", "x-chownow-auth-token": token,
               'username': 'AdventurousEater', 'password': password}
    r = None
    if method is POST:
        r = requests.post(URL + endpoint, data=json.dumps(data), headers=headers)
        print("\n Verified Error MSG after POST request, after add should be :", r.json())
    elif method is DELETE:
        r = requests.delete(URL + endpoint, params=data, headers=headers)
        print("\n Verified Error MSG after DELETE request, after delete should be :", r.json())
    elif method is PUT:
        r = requests.put(URL + endpoint, json=data, headers=headers)
        print("\n Verified Error MSG after PUT request, after update should be :", r.json())
    elif method is GET:
        r = requests.get(URL + endpoint, headers=headers)
    print("\n Verified Error MSG after "+ method +" request return status code :", r.status_code)
    return r

def merge_two_dicts(x, y):
    z = x.copy()
    z.update(y)
    return z

def get_token():
    tok = LOGIN_POST.json()
    token = tok["token"]
    print("\n Created token :", token)
    return token

def get_restauraunts():
    r = requests.get(URL + RESTAURANTP)
    return r.json()

def get_url_status_code(endpoint):
    r = requests.get(URL + endpoint)
    return r.status_code

def get_url_json(endpoint):
    r = requests.get(URL + endpoint)
    return r.json()

def first_restauraunts():
    restaurants = get_restauraunts()
    r = next(iter(restaurants.keys()))
    restaurant_delete = {'restaurant': ''}
    restaurant_delete.update({'restaurant': r})
    print("\n First restaurant is :", restaurant_delete)
    return restaurant_delete


