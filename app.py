from flask import Flask, render_template, url_for, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import requests
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

YELP_API_KEY = os.environ.get('YELP_API_KEY')
YELP_API_BASE_URL = "https://api.yelp.com/v3"

@app.route('/')
def home():
    return 'Hello World! The App is Working!'


@app.route('/api/data', methods=['GET'])
def get_data():
    data = {'message': 'JSON is working'}
    return jsonify(data)

@app.route('/api/restaurants', methods=['GET'])
def get_restaurants():
    location = request.args.get('location', 'New York')
    term = request.args.get('term', 'restaurants')

    headers = {
        'Authorization': f'Bearer {YELP_API_KEY}'
    }

    params = {
        'location': location,
        'term': term,
        'limit': 20
    }

    response = requests.get(f"{YELP_API_BASE_URL}/businesses/search", headers=headers, params=params)

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        # Print the response from Yelp API to the console for debugging
        print('Failed to fetch data from Yelp API:')
        print('Status Code:', response.status_code)
        print('Response:', response.text)
        return jsonify({'error': 'Failed to fetch data from Yelp'}), response.status_code


    

if __name__ == "__main__":
    app.run(debug=True)



