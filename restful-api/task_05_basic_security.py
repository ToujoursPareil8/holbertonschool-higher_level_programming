from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)

# --- Configuration ---
# Secret keys are crucial. They are used to cryptographically sign session cookies and JWTs.
# In a real production app, NEVER hardcode these. Load them from environment variables.
app.config["SECRET_KEY"] = "a9f3k2p8x1n7q4m6r0s5t3u2v8w1y4z9"
app.config["JWT_SECRET_KEY"] = "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0"

# Initialize our authentication managers
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# --- Mock Database ---
# Passwords must be hashed. If the database is compromised, hackers won't see plain text.
# generate_password_hash uses a secure algorithm (like PBKDF2 with SHA256) by default.
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

# ==========================================
# METHOD 1: HTTP Basic Authentication
# ==========================================

# This callback function tells BasicAuth how to verify a username and password.
# It automatically intercepts requests to routes protected by @auth.login_required.
@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    # check_password_hash securely compares the plain text password with the stored hash
    if user and check_password_hash(user["password"], password):
        return user # Returning the user object grants access

# Endpoint protected by Basic Auth. 
# The client must send an "Authorization: Basic <base64_encoded_credentials>" header.
@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


# ==========================================
# METHOD 2: JWT (JSON Web Token) Authentication
# ==========================================

# Step 1 of JWT: The Login Route
# The user exchanges their credentials for a temporary, signed token.
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid credentials"}), 401 # 401 Unauthorized
    
    username = data.get("username")
    password = data.get("password")
    user = users.get(username)
    
    # Verify the user exists and the password is correct
    if user and check_password_hash(user["password"], password):
        # Generate the JWT. 'identity' is the payload stored inside the token (usually the user ID or username).
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    
    return jsonify({"error": "Invalid credentials"}), 401

# Step 2 of JWT: Accessing a Protected Route
# The client must send the token in the header: "Authorization: Bearer <token>"
@app.route("/jwt-protected", methods=["GET"])
@jwt_required() # This decorator enforces that a valid JWT must be present
def jwt_protected():
    return "JWT Auth: Access Granted"

# JWT with Role-Based Access Control (RBAC)
@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    # Extract the 'identity' (username) that we packed into the token during login
    current_username = get_jwt_identity()
    user = users.get(current_username)
    
    # Check if the user exists AND has the specific 'admin' role
    if not user or user["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403 # 403 Forbidden
    
    return "Admin Access: Granted"


# ==========================================
# JWT Error Handling Callbacks
# ==========================================
# These callbacks catch specific JWT errors and return clean JSON responses 
# instead of ugly HTML error pages.

@jwt.unauthorized_loader
def handle_unauthorized_error(_):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(_):
    # Triggers if the token format is wrong or if it was tampered with (signature fails)
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(_, __):
    # Triggers if the token's lifespan has passed
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(_, __):
    # Triggers if the token has been explicitly invalidated (e.g., user logged out)
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(_, __):
    # Triggers if an endpoint requires a "fresh" token (e.g., for sensitive actions like changing a password)
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
