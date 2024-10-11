from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
from werkzeug.security import generate_password_hash, check_password_hash
import json

app = Flask(__name__)
auth = HTTPBasicAuth()
jwt = JWTManager(app)

app.config['JWT_SECRET_KEY'] = "test"
app.config['SECRET_KEY'] = 'x93\x9b1\x1c\x8fg1\xe5\xfcd\xec]'

# username : username | password : crypted_password | role : user role
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("adminpass"), "role": "admin"}
}

@auth.verify_password  # Décorateur pour indiqué que la fonction sert à vérifier les identifiants de l'utilisateur
def verify_password(username, password):
    if username in users:  # Vérifie si le nom d'utilisateur existe dans le dictionnaire "users"
        # Si l'utilisateur existe, on vérifie si le mot de passe donné correspond avec le mot de passe crypté du dictionnaire, si oui True est retourné
        return check_password_hash(users[username]['password'], password)
    return False  # Sinon False est retourné || Check au cas ou (remplacer par None)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()  # recupère les données JSON du payload
    username = data.get("username")
    password = data.get("password")

    # Vérifie les infos d'identification
    if username in users and check_password_hash(users[username]['password'], password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200

@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    return jsonify({"msg": "JWT Auth: Access Granted"}), 200

@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    jwt_data = get_jwt_identity()
    user_role = jwt_data.get('role')
    
    if user_role == 'admin':
        return jsonify({"msg": "Admin Access: Granted"})

if __name__ == '__main__':
    app.run(debug=True)
