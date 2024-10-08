from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "john": generate_password_hash("hello"),
    "susan": generate_password_hash("bye"),
    "alice": generate_password_hash("password123"),
    "bob": generate_password_hash("secret"),
    "charlie": generate_password_hash("12345"),
}

for key, password in users.items():
    print({key}, {password})
