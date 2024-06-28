import os
import requests
from flask import render_template, request, redirect, url_for, flash
from reeltalk import app, db
from reeltalk.models import User, Movie, Review
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Successful Login', category='success')
                login_user(user, remember=True)
                return redirect(url_for('my_reviews'))
            else:
                flash('Incorrect Password', category='error')
        else:
            flash('Email doesn\'t exist', category='error')

    return render_template("login.html")

@app.route("/")
def home():
        api_key = os.environ.get("API_KEY")
        url = 'https://api.themoviedb.org/3/trending/movie/week?'
        params = {'api_key': api_key, 'include_adult': False}
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            tmdb_data = response.json()
            trending_movies = tmdb_data['results']            
            if not trending_movies: 
                flash(f'No movies found', category='error')
                return redirect(url_for('search_movies'))
            return render_template('home.html', movies=trending_movies)
        else:
            flash('Error: Failed to fetch movie details from TMDb API', category='error')
            return redirect(url_for('home'))


@app.route('/search_movies', methods=['GET', 'POST'])
@login_required
def search_movies():
    if request.method == 'POST':
        search_query = request.form['search_query']
        api_key = os.environ.get("API_KEY")
        url = 'https://api.themoviedb.org/3/search/movie'
        params = {'api_key': api_key, 'query': search_query, 'include_adult': False}
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            movies = data['results']
            if not movies: 
                flash(f'No movies found for "{search_query}"', category='error')
                return redirect(url_for('search_movies'))
            return render_template('search_results.html', movies=movies, search_query=search_query, active_page='search_movies')
        else:
            flash('Error: Failed to fetch movie details from TMDb API', category='error')
            return redirect(url_for('search_movies'))
    return render_template('search_movies.html', active_page='search_movies')

@app.route('/movie/<int:movie_id>', methods=['GET', 'POST'])
@login_required
def movie_details(movie_id):
    # Fetch movie details from TMDb API
    api_key = os.environ.get("API_KEY")
    url = f'https://api.themoviedb.org/3/movie/{movie_id}'
    params = {'api_key': api_key}
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        movie_data = response.json()
    else:
        flash('Error: Failed to fetch movie details from TMDb API', category='error')
        return redirect(url_for('home'))  # Redirect to home or another page on error
    
    # Handle POST request for submitting a review
    if request.method == 'POST':
        review_text = request.form.get('review_text')

        if not review_text:
            flash('Review text cannot be empty', category='error')
        else:
            # Check if the movie already exists in the database
            movie = Movie.query.filter_by(tmdb_id=movie_id).first()

            if not movie:
                # If movie does not exist in the database, create a new Movie object
                movie = Movie(
                    tmdb_id=movie_data['id'],
                    title=movie_data['title'],
                    overview=movie_data['overview'],
                    release_date=movie_data['release_date'],
                    backdrop_path=movie_data['backdrop_path']
                )
                db.session.add(movie)
                db.session.commit()

            # Check if the user has already posted a review in the database. movie_id=movie.id uses the id of the movie from the movie object created/fetched in/from the database
            existing_review = Review.query.filter_by(user_id=current_user.id, movie_id=movie.id).first()
            
            if existing_review:
                flash('You\'ve already posted a review for this movie', category='error')  
            else:
                # Create a new Review object and associate it with the current user and movie
                new_review = Review(user_id=current_user.id, movie_id=movie.id, review_text=review_text)
                db.session.add(new_review)
                db.session.commit()
                flash('Review Submitted', category='success')

            # Redirect to the my_reviews page to avoid resubmission on refresh
            return redirect(url_for('my_reviews', movie_id=movie_id))

    # Render the movie details page with movie data and review form
    return render_template('review_form.html', movie=movie_data, active_page='search_movies')
    
         

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
    
        email_exists = User.query.filter_by(email=email).first()

        if len(first_name) < 2:
            flash('First name must be more than two characters long', category='error')
        elif len(email) < 4:
            flash('Email must be more than 4 characters long', category='error')
        elif password1 != password2:
            flash('Passwords do not match', category='error')
        elif len(password1) < 7 or len(password1) > 20:
            flash('Password doesn\'t match the right criteria', category='error')            
        elif email_exists:
            flash('Account Already Exists', category='error')
        else:
            new_user = User(first_name=first_name, last_name=last_name, email=email, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('User Created!')
            return redirect(url_for('home'))                        
    return render_template('sign_up.html')


@app.route('/my_reviews')
@login_required
def my_reviews():
    user_reviews = current_user.reviews  # Access reviews via backref
    return render_template('my_reviews.html', reviews=user_reviews, active_page='my_reviews')

@app.route('/movie_reviews')
@login_required
def movie_reviews():
    all_reviews = Review.query.all()
    return render_template('movie_reviews.html', all_reviews=all_reviews, active_page='movie_reviews')

@app.route('/edit_review/<int:review_id>', methods=["GET", "POST"])
@login_required
def edit_review(review_id):
    user_review = Review.query.filter_by(id=review_id).first()

    if not user_review:
        flash('Review does not exist', category='error')
    elif current_user.id != user_review.user_id:
        flash('You do not have permission to edit this review', category='error')
    else:
        if request.method == 'POST':
            review_text = request.form.get('review_text')
            if review_text:
                user_review.review_text = review_text            
                db.session.commit()
                flash('Review successfully updated', category='success')
                return(redirect(url_for('my_reviews')))
            else:
                flash('Review text cannot be empty', category='error')

    return render_template('edit_review.html' , review=user_review)

@app.route('/delete_review/<int:review_id>', methods=["GET", "POST"])
@login_required
def delete_review(review_id):
    user_review = Review.query.filter_by(id=review_id).first()

    if not user_review:
        flash('Review does not exist', category=='error')
    elif current_user.id != user_review.user_id:
        flash('You do not have permission to delete this review', category='error')
    else:
        db.session.delete(user_review)
        db.session.commit()
        flash('Review successfully deleted', category='success')
    return(redirect(url_for('my_reviews')))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


# 404 error handling taken from: https://www.geeksforgeeks.org/python-404-error-handling-in-flask/
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')