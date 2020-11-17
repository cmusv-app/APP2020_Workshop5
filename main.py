from flask import Flask
from flask_restful import Api
from database.db import initialize_db
from resources.Questions import Questions
from utils.JSONEncoder import MongoEngineJSONEncoder
from authentication.jwt import initialize_jwt
from resources.Users import Users
from resources.UserRegistration import UserRegistration
from resources.UserLogin import UserLogin


app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'workshop5',
    'host': 'mongodb://localhost:27017/workshop5'
}

app.config['JWT_SECRET_KEY'] = 'phil-is-a-coding-god'  # Change this!

initialize_db(app)
jwt = initialize_jwt(app)
app.json_encoder = MongoEngineJSONEncoder
api = Api(app)

api.add_resource(Questions,
                 '/questions',
                 '/questions/<string:q_id>')

api.add_resource(UserRegistration, '/register')
api.add_resource(Users, '/users/<string:u_id>')
api.add_resource(UserLogin, '/login')

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
