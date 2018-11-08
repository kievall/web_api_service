from flask_restful import reqparse, Api, Resource
from flask import request

from faker import Faker

fake = Faker()
parser = reqparse.RequestParser()
parser.add_argument('username', type=str)
parser.add_argument('password', type=str)
parser.add_argument('restaurant', type=str)
parser.add_argument('rating', type=int)
parser.add_argument('token', type=str)

favorite_restaurants = {'Tocaya': 4, 'Hash': 3, 'Homestate': 5}

valid_users = [{'username': 'AdventurousEater', 'password': '1234'}, {'username': 'PickyEater', 'password': 'secret'}]

tokens = []


class LoginAPI(Resource):
    """The endpoint through which the user can log into the application."""
    def get(self):
        return {'error': 'Method not allowed. Make a POST request with a valid username and password'}, 405

    def post(self):
        content = request.json
        
        if "username" not in content or "password" not in content:
            return {'error': 'Bad request. Username and password are required'}, 400
            
        username = content["username"]
        password = content["password"]
        
        for valid_user in valid_users:
            if username == valid_user['username'] and password == valid_user['password']:
                token = fake.sha256()
                tokens.append(token)
                return {'token': token}, 200
        return {'error': 'Unauthorized'}, 401


class FavoriteRestaurantsAPI(Resource):
    """An endpoint through which the user can get, edit, add to and remove from their list of favorite restaurants."""

    def get(self):
        """Returns a list of favorite restaurants and their ratings."""
        return favorite_restaurants, 200

    def put(self):
        """Updates the rating for an existing restaurant."""
        if not self.is_authorized(request):
            return {'error': 'Unauthorized'}, 401

        content = request.json

        if 'restaurant' not in content or 'rating' not in content:
            return {'error': 'Invalid payload'}, 400

        restaurant = content['restaurant']
        rating = content['rating']

        if restaurant not in favorite_restaurants:
            return {'error': 'Invalid restaurant selected.'}, 409

        favorite_restaurants[restaurant] = rating

        return {}, 200

    def post(self):
        """Add a new favorite restaurant to the list with its rating."""
        if not self.is_authorized(request):
            return {'error': 'Unauthorized'}, 401

        content = request.json

        if 'restaurant' not in content or 'rating' not in content:
            return {'error': 'Invalid payload'}, 400

        restaurant = content['restaurant']
        rating = content['rating']

        if restaurant in favorite_restaurants:
            return {'error': 'Restaurant is already in the list. Choose a new restaurant.'}, 409

        favorite_restaurants[restaurant] = rating

        return {}, 201

    def delete(self):
        """Removes a restaurant from your list of favorites."""
        if not self.is_authorized(request):
            return {'error': 'Unauthorized'}, 401

        if 'restaurant' not in request.args:
            return {'error': 'Invalid request'}, 400

        restaurant = request.args.get('restaurant')

        if restaurant not in favorite_restaurants:
            return {'error': 'Invalid restaurant selected.'}, 409

        favorite_restaurants.pop(restaurant)

        return {}, 200

    def is_authorized(self, request):
        """Makes sure the user is logged in."""
        headers = request.headers
        
        return 'x-chownow-auth-token' in headers and headers['x-chownow-auth-token'] in tokens
