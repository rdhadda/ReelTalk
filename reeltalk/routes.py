import os
import requests
from flask import render_template, request, redirect, url_for
from reeltalk import app, db



@app.route("/")
def home():
    return render_template("index.html")

@app.route('/search_movies', methods=['GET', 'POST'])
def search_movies():
    if request.method == 'POST':
        search_query = request.form['search_query']
        api_key = os.environ.get("API_KEY")
        url = 'https://api.themoviedb.org/3/search/movie'
        params = {'api_key': api_key, 'query': search_query}
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            movies = data['results']
            return render_template('search_results.html', movies=movies, search_query=search_query)
        else:
            return 'Error: Failed to fetch data from TMDb API'
    return render_template('search_movies.html')

@app.route('/movie/<int:movie_id>', methods=['GET'])
def movie_details(movie_id):
    api_key = os.environ.get("API_KEY")
    url = f'https://api.themoviedb.org/3/movie/{movie_id}'
    params = {'api_key': api_key}
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        movie = response.json()
        return render_template('review_form.html', movie=movie)
    else:
        return 'Error: Failed to fetch movie details from TMDb API'