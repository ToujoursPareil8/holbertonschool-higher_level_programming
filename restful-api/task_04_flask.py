from flask import Flask, jsonify, request

# Initialize the Flask application
# __name__ helps Flask determine the root path for the application
app = Flask(__name__)

# A simple in-memory dictionary to act as our database
# Note: In a real app, this data is lost when the server restarts. 
users = {}

# --- Endpoint: Root URL ---
# The @app.route decorator maps the URL "/" to the home() function.
# By default, routes only respond to GET requests.
@app.route("/")
def home():
    return "Welcome to the Flask API!"

# --- Endpoint: Get All Usernames ---
@app.route("/data")
def get_data():
    # jsonify() automatically converts Python lists/dictionaries into JSON format
    # and sets the appropriate "Content-Type: application/json" header.
    return jsonify(list(users.keys()))

# --- Endpoint: Health Check ---
@app.route("/status")
def status():
    return "OK"

# --- Endpoint: Get Specific User ---
# <username> is a dynamic URL parameter. Flask passes it to the function as an argument.
@app.route("/users/<username>")
def get_user(username):
    # Try to fetch the user from our dictionary
    user = users.get(username)
    
    # If the user exists, return their data (defaults to HTTP 200 OK)
    if user:
        return jsonify(user)
    
    # If the user doesn't exist, return an error message and a 404 Not Found status code
    return jsonify({"error": "User not found"}), 404

# --- Endpoint: Add a New User ---
# Explicitly set methods=["POST"] so this endpoint only accepts data submission
@app.route("/add_user", methods=["POST"])
def add_user():
    # request.get_json() parses the incoming JSON payload into a Python dictionary
    user_data = request.get_json()
    
    # Validation: Ensure the request actually contained JSON data
    if not user_data:
        return jsonify({"error": "Invalid JSON"}), 400 # 400 Bad Request
    
    # Validation: Ensure the JSON includes a 'username' key
    username = user_data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    
    # Validation: Check for duplicates to prevent overwriting existing users
    if username in users:
        return jsonify({"error": "Username already exists"}), 409 # 409 Conflict
    
    # If all validations pass, save the user to our "database"
    users[username] = user_data

    # Return a success message, the saved data, and a 201 Created status code
    return jsonify({
        "message": "User added",
        "user": user_data
    }), 201

# Start the development server
if __name__ == "__main__":
    # app.run() starts the server on http://127.0.0.1:5000/ by default
    app.run()
