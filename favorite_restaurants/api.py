from flask_restful import Api

from views import FavoriteRestaurantsAPI, LoginAPI
from app import app

api = Api(app)

##
## Actually setup the Api resource routing here
##
api.add_resource(LoginAPI, '/login')
api.add_resource(FavoriteRestaurantsAPI, '/favorite_restaurants')



if __name__ == '__main__':
    app.run(debug=True)
