import os
import requests
from flask import render_template, request, redirect, url_for, flash, abort
from reeltalk import app, db
from reeltalk.models import User, Movie, Review
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash


@app.route("/login", methods=['GET', 'POST'])
def login():
    """
    login function to allow a user to login into the website.
    with error handling for incorrect password and if the
    users email doesn't exist.

    """
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        # check to see if the user exists in the database
        user = User.query.filter_by(email=email).first()
        if user:
            # if the user exists.
            # check if the entered password matches the password in the db
            if check_password_hash(user.password, password):
                flash('Successful Login', category='success')
                login_user(user, remember=True)
                # after a succesful login, user is taken to the my reviews page
                return redirect(url_for('my_reviews'))
            else:
                flash('Incorrect Password', category='error')
        else:
            flash('Email doesn\'t exist', category='error')

    return render_template("login.html")


@app.route("/")
def home():
    """
    homepage function which shows this weeks
    top 12 trending movies.

    """
    # fetch api key from env.py
    api_key = os.environ.get("API_KEY")
    url = 'https://api.themoviedb.org/3/trending/movie/week?'
    params = {'api_key': api_key, 'include_adult': False}
    response = requests.get(url, params=params)
    # fetch trending movies from TMDB
    if response.status_code == 200:
        tmdb_data = response.json()
        trending_movies = tmdb_data['results']
        # if there are no movies found a flash message is displayed
        if not trending_movies:
            flash(f'No movies found', category='error')
            return redirect(url_for('search_movies'))
        return render_template('home.html', movies=trending_movies)
    else:
        flash('Error: Failed to fetch movie details from TMDb API',
              category='error')
        return redirect(url_for('home'))


@app.route('/search_movies', methods=['GET', 'POST'])
@login_required
def search_movies():
    """
    search movies function allows a user to search
    for a movie using the TMDB API.

    """
    if request.method == 'POST':
        # Fetch movie details from TMDb API
        search_query = request.form['search_query']
        api_key = os.environ.get("API_KEY")
        url = 'https://api.themoviedb.org/3/search/movie'
        params = {
            'api_key': api_key, 'query': search_query, 'include_adult': False
            }
        response = requests.get(url, params=params)
        # Gathers search results from the API if the connection is successful
        if response.status_code == 200:
            data = response.json()
            movies = data['results']
            # If there is no movie which matches the users search,
            # a flash message is displayed
            if not movies:
                flash(
                    f'No movies found for "{search_query}"', category='error'
                    )
                return redirect(url_for('search_movies'))
            return render_template(
                'search_results.html', movies=movies,
                search_query=search_query,
                active_page='search_movies'
                )
        else:
            # If there is no connection to the API,
            # a flash message is displayed.
            flash(
                'Error: Failed to fetch movie details from TMDb API',
                category='error'
                )
            return redirect(url_for('search_movies'))
    return render_template('search_movies.html', active_page='search_movies')


@app.route('/movie/<int:movie_id>', methods=['GET', 'POST'])
@login_required
def movie_details(movie_id):
    """
    movie details function allows a user to create a review
    against their chosen movie. The movie details are added to
    the database if it doesn't exist already. The user can then
    post a review if they haven't posted one previously for the
    movie in question.

    """
    # Fetch movie details from TMDb API
    api_key = os.environ.get("API_KEY")
    url = f'https://api.themoviedb.org/3/movie/{movie_id}'
    params = {'api_key': api_key}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        movie_data = response.json()
    else:
        flash(
            'Error: Failed to fetch movie details from TMDb API',
            category='error'
        )
        return redirect(url_for('home'))
    # Handle POST request for submitting a review
    if request.method == 'POST':
        review_text = request.form.get('review_text')
        if not review_text:
            flash('Review text cannot be empty', category='error')
        else:
            # Check if the movie already exists in the database
            movie = Movie.query.filter_by(tmdb_id=movie_id).first()
            if not movie:
                try:
                    # If movie does not exist in the database,
                    # create a new Movie object
                    movie = Movie(
                        tmdb_id=movie_data['id'],
                        title=movie_data['title'],
                        overview=movie_data['overview'],
                        release_date=movie_data['release_date'],
                        backdrop_path=movie_data['backdrop_path']
                    )
                    db.session.add(movie)
                    db.session.commit()
                except Exception as e:
                    # Rollback the session to the state before the add & commit
                    db.session.rollback()
                    # log the error to the console
                    print(f"An error occurred while adding the movie: {e}")
                    # Redirect to the 500 error page
                    abort(500)

            # Check if the user has already posted a review in the database.
            # movie_id=movie.id uses the id of the movie from the movie object
            # created/fetched in/from the database
            existing_review = Review.query.filter_by(
                user_id=current_user.id, movie_id=movie.id).first()
            if existing_review:
                flash(
                    'You\'ve already posted a review for this movie',
                    category='error'
                    )
            else:
                try:
                    # Create a new Review object
                    # and associate it with the current user and movie
                    new_review = Review(
                        user_id=current_user.id, movie_id=movie.id,
                        review_text=review_text
                            )
                    db.session.add(new_review)
                    db.session.commit()
                    flash('Review Submitted', category='success')
                except Exception as e:
                    # Rollback the session to the state before the add & commit
                    db.session.rollback()
                    # log the error to the console
                    print(f"An error occurred while adding the movie: {e}")
                    # Redirect to the 500 error page
                    abort(500)

            # Redirect to the my_reviews page to avoid resubmission on refresh
            return redirect(url_for('my_reviews', movie_id=movie_id))
    # Render the movie details page with movie data and review form
    return render_template(
        'review_form.html', movie=movie_data, active_page='search_movies'
        )


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    """
    sign up function allows a user to create an account for
    the website. Their details are then saved in the database.

    """
    if request.method == 'POST':
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        email_exists = User.query.filter_by(email=email).first()
        if len(first_name) < 2:
            flash(
                'First name must be more than two characters long',
                category='error'
                )
        elif len(email) < 4:
            flash(
                'Email must be more than 4 characters long',
                category='error'
                )
        elif password1 != password2:
            flash('Passwords do not match', category='error')
        elif len(password1) < 7 or len(password1) > 20:
            flash('Password doesn\'t match the right criteria',
                  category='error'
                  )
        elif email_exists:
            flash('Account Already Exists', category='error')
        else:
            try:
                new_user = User(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=generate_password_hash(password1,
                                                    method='sha256'))
                db.session.add(new_user)
                db.session.commit()
                flash('User Created!')
                return redirect(url_for('home'))
            except Exception as e:
                # Rollback the session to the state before the add & commit
                db.session.rollback()
                # log the error to the console
                print(f"An error occurred while adding the movie: {e}")
                # Redirect to the 500 error page
                abort(500)

    return render_template('sign_up.html')


@app.route('/my_reviews')
@login_required
def my_reviews():
    """
    my reviews function displays all the reviews
    created by the logged in user.

    """
    # Query the database to show reviews for the logged in user
    user_reviews = current_user.reviews  # Access reviews via backref
    return render_template(
        'my_reviews.html', reviews=user_reviews, active_page='my_reviews')


@app.route('/movie_reviews')
@login_required
def movie_reviews():
    """
    movie reviews function displays all the reviews
    created by all users.

    """
    # Query the database to show all movie reviews
    all_reviews = Review.query.all()
    return render_template(
        'movie_reviews.html',
        all_reviews=all_reviews,
        active_page='movie_reviews'
        )


@app.route('/edit_review/<int:review_id>', methods=["GET", "POST"])
@login_required
def edit_review(review_id):
    """
    edit reviews function allows a user to edit a previously
    created review.

    """
    # check to see if the review exists in the database
    user_review = Review.query.filter_by(id=review_id).first()
    if not user_review:
        flash('Review does not exist', category='error')
    # check if the current user's id matches the id of the logged in user
    elif current_user.id != user_review.user_id:
        # If the current user doesn\'t match the id
        # of the user who created the review
        # the user is redirected to a 403 page
        flash(
            'You do not have permission to edit this review', category='error'
        )
        abort(403)
    else:
        if request.method == 'POST':
            review_text = request.form.get('review_text')
            if not review_text:
                flash('Review text cannot be empty', category='error')
            else:
                try:
                    user_review.review_text = review_text
                    db.session.commit()
                    flash('Review successfully updated', category='success')
                    return (redirect(url_for('my_reviews')))
                except Exception as e:
                    # Rollback the session to the state before the commit
                    db.session.rollback()
                    # log the error to the console
                    print(f"An error occurred while adding the movie: {e}")
                    # Redirect to the 500 error page
                    abort(500)
    return render_template('edit_review.html', review=user_review)


@app.route('/delete_review/<int:review_id>', methods=["GET", "POST"])
@login_required
def delete_review(review_id):
    """
    delete reviews function allows a user to delete a review.

    """
    # check to see if the review exists in the database
    user_review = Review.query.filter_by(id=review_id).first()
    if not user_review:
        flash('Review does not exist', category == 'error')
    # check if the current user's id matches the id of the logged in user
    elif current_user.id != user_review.user_id:
        # If the current user doesn\'t match the id
        # of the user who created the review
        # the user is redirected to a 403 page
        flash(
            'You do not have permission to delete this review',
            category='error'
            )
        abort(403)
    else:
        try:
            db.session.delete(user_review)
            db.session.commit()
            flash('Review successfully deleted', category='success')
        except Exception as e:
            # Rollback the session to the state before the commit
            db.session.rollback()
            # log the error to the console
            print(f"An error occurred while adding the movie: {e}")
            # Redirect to the 500 error page
            abort(500)
    return (redirect(url_for('my_reviews')))


@app.route('/logout')
@login_required
def logout():
    """
    logout function allows a user
    to logout of the website.

    """
    logout_user()
    return redirect(url_for('home'))


# 404 error handling taken from:
# https://www.geeksforgeeks.org/python-404-error-handling-in-flask/
@app.errorhandler(404)
def page_not_found(e):
    """
    page not found redirects a user to a 404 page.

    """
    return render_template('404.html')


# 403 error handling
@app.errorhandler(403)
def page_not_found(e):
    """
    page not found redirects a user to a 403 page.

    """
    return render_template('403.html')


# 500 error handling taken from flask.palletsprojects
@app.errorhandler(500)
def internal_server_error(e):
    """
    internal server error redirects a user to a 500 page.

    """
    return render_template('500.html'), 500
