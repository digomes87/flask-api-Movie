from flask import Flask, escape, request, render_template
from os import environ
import json
import os
import requests


API_KEY = environ.get('API_KEY')
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__name__':
    app.run()


@app.route('/favorites')
def favorites():
    """Read out favorited movies"""
    filename = os.path.join('data.json')
    with open(filename) as data_file:
        data = json.load(data_file)
        return data


@app.route('/favorites')
def favoritess():
    """if query params are passed, write movie to json file."""
    return render_template('favorites.html')


@app.route('/search', methods=['POST'])
def search():
    """if POST, query movie api for data and return results."""
    query = request.form['title']
    print(query)
    api = "http://www.omdbapi.com/?apikey="+API_KEY+"&s="+query
    print(api)
    response = requests.get(api)
    response_json = response.json()
    print(response_json)
    return f'Hello, {response_json}!'


@app.route('/movie/<movie_oid>')
def movie_detail():
    """if fetch data from movie database by oid and display info."""
    qs_name = request.args.get('name', '')
    qs_oid = request.args.get('oid', '')
    return f'Hello, {escape(name)}!'


print(API_KEY)

app.run(debug=True, port=8085)
