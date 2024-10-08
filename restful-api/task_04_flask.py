from flask import Flask, request
from flask import jsonify


app = Flask(__name__)

users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    return 'OK'


@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=['POST'])
def add_user():
    # si la requète est en JSON
    if request.is_json:
        # Extraire les données JSON envoyé et les stockent dans une variable
        user_data = request.get_json()

        # Vérifier si le champ 'username' est présent et s'il existe déja
        username = user_data.get('username')

        if not username:
            return jsonify({"error": "Username is required"}), 400

        # Ajouter l'utilisateur au dictionnaire
        users[username] = user_data

        # Retourner le message de confirmation
        return jsonify({
            "message": "User added",
            "user": user_data
        }), 201


if __name__ == "__main__":
    app.run()
