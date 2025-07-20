from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, CI Pipeline by Afshan!"

if __name__ == '__main__':
    app.run(debug=True)

# This is a simple Flask application that returns a greeting message.
# It is designed to be run in a CI pipeline environment.
