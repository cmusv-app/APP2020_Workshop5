# Workshop 5

This workshop extends the code of Workshop 4 by adding user authentication through the use [JWT tokens](https://dzone.com/articles/what-is-jwt-token). 

## New library
[Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/en/stable/)

## New Code Additions
1. authentication/jwt.py
2. models/User.py
3. resources/UserLogin.py
4. resources/UserRegistration.py
5. resources/Users.py
6. services/UserService.py

## Modified
1. main.py - supports new routes and JWT initialization
2. resources/Questions.py - only authenticated users can POST/PATCH

