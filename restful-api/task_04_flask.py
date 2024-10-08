from flask import Flask, request
from flask import jsonify


app = Flask(__name__)
users = {
    "jane":
        {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john":
        {"username": "john", "name": "John", "age": 30, "city": "New York"}
        }


@app.route("/")
def home():
    return "<p>Welcome to the Flask API!<p>"


@app.route("/data")
def get_username():
    return jsonify(list(users.keys()))


@app.route("/status")
def get_OK():
    return 'OK'


@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return {"error": "User not found"}


@app.route("/add_user", methods=['POST'])
def add_user():
    # si la requète est en JSON
    if request.is_json:
        # Extraire les données JSON envoyé et les stockent dans une variable
        user_data = request.get_json()

        # Vérifier si le champ 'username' est présent et s'il existe déja
        username = user_data.get('username')
        if username in users:
            return jsonify({"message": "User already exists"})

        # Ajouter l'utilisateur au dictionnaire
        users[username] = user_data

        # Retourner le message de confirmation
        return jsonify({
            "message": "User added",
            "user": user_data
        })
