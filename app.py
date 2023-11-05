from flask import Flask, render_template, url_for, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'Hello World! The App is Working!'

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {'message': 'JSON is working'}
    return jsonify(data)

if __name__ == "__main__":
    app.run()



