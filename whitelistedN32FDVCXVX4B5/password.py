from flask import Flask, request, jsonify, render_template_string
from passlib.hash import bcrypt_sha256

app = Flask(__name__)

# Simulated user data store (replace this with a proper database in production)
users = {
    'user1': {
        'username': 'user1',
        'password_hash': bcrypt_sha256.hash('password123'),
    },
    # Add more users here
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({'message': 'Username and password are required.'}), 400

        user = users.get(username)
        if user and bcrypt_sha256.verify(password, user['password_hash']):
            return jsonify({'message': 'Login successful!'}), 200
        else:
            return jsonify({'message': 'Invalid username or password.'}), 401
    else:
        # Render the index.html template
        return render_template_string(open('index.html', 'r').read())

if __name__ == '__main__':
    app.run(debug=True)  # For local testing only
