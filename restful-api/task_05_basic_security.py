from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
from werkzeug.security import generate_password_hash, check_password_hash
import json

app = Flask(__name__)
auth = HTTPBasicAuth()
jwt = JWTManager(app)

app.config['JWT_SECRET_KEY'] = "x93\x9b1\x1c\x8fg1\xe5\xfcd\xec]"

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

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return jsonify({"message": "Basic Auth: Access Granted"})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()  # recupère les données JSON du payload
    username = data.get("username")
    password = data.get("password")

    # Vérifie les infos d'identification
    if username in users and check_password_hash(users[username]['password'], password):
        # Si infos valide stock le nom d'utilisateur et son rôle
        user_info = {"username": username, "role": users[username]['role']}
        #  Génère un token qui contient les infos de user_info
        access_token = create_access_token(identity=user_info)
        return jsonify(access_token=access_token), 200
    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    return jsonify({"msg": "JWT Auth: Access Granted"}), 200

@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    jwt_data = get_jwt_identity()
    if jwt_data['role'] == 'admin':
        return jsonify({"msg": "Admin Access: Granted"})
    else:
        return jsonify({"error": "Admin access required"}), 403

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == '__main__':
    app.run(debug=True)
