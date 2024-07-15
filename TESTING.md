# ReelTalk - Testing

![ReelTalk. Screenshot of website](reeltalk/static/documents/reeltalk-am-i-responsive.png)

[View ReelTalk on Heroku](https://reeltalk-rd-86df5744ce6e.herokuapp.com/)

## CONTENTS

- [Automated Testing](#Automated-Testing)
  - [W3C Validator](#W3C-Validator)
  - [JavaScript Validator](#JavaScript-Validator)
  - [Lighthouse Testing](#Lighthouse-Testing)
  - [Wave Testing](#Wave-Testing)
  - [CI Python Linter](#ci-python-linter)
- [Manual Testing](#Manual-Testing)
  - [Testing User Stories](#Testing-User-Stories)
  - [Full Testing](#Full-Testing)
- [Bugs](#bugs)
  - [Solved Bugs](#solved-bugs)
  - [Known Bugs](#known-bugs)

## Testing

Testing was continuous throughout the website build. I used Chrome developer tools to identify and address any issues as they arose.

- My automated testing consisted of using W3C Validator, JSHint, Lighthouse, Wave and the CI Linter Python.
- I then manually tested the user stories along with the functionality of the website.

## Automated Testing

### W3C Validator

W3C validator was used to validate the HTML on all pages of the website. It was also used to validate CSS in the style.css file.

- All pages pass the W3C validator.


- [Home Page](reeltalk/static/documents/w3-homepage.png)
- [Login Page](reeltalk/static/documents/w3-login.png)
- [Sign Up Page](reeltalk/static/documents/w3-sign-up.png)
- [Search Page](reeltalk/static/documents/w3-search-movies.png)
- [Search Results Page](reeltalk/static/documents/w3-search-results.png)
- [Add Review Page](reeltalk/static/documents/w3-review.png)
- [Edit Review Page](reeltalk/static/documents/w3-edit-review.png)
- [My Reviews Page](reeltalk/static/documents/w3-my-reviews.png)
- [Movie Reviews Page](reeltalk/static/documents/w3-movie-reviews.png)
- [404 Page](reeltalk/static/documents/w3-404-page.png)
- [500 Page](reeltalk/static/documents/w3-500-page.png)
- [403 Page](reeltalk/static/documents/w3-403-page.png)
- [CSS](reeltalk/static/documents/reeltalk-w3-css.png)



### JavaScript Validator

[JSHint](https://jshint.com/) was used to validate the JavaScript.

- [Script.js](reeltalk/static/documents/jshint-script.js.png)

- All pages pass the JSHint validator.


### Lighthouse Testing

I took the opportunity to utilize Lighthouse within Chrome Developer Tools. This allowed me to test for performance, accessibility, best practices and the SEO (search engine optimization) of the website.

- All pages pass Googles lighthouse tests for Desktop and Mobile.

#### Desktop Testing

<details>
<summary>Lighthouse Desktop Testing Screen Shots</summary>

  #### Home Page

![Home Page](reeltalk/static/documents/lighthouse-desktop-home-page.png)

  #### Login Page

 ![Login Page](reeltalk/static/documents/lighthouse-desktop-login.png)

 #### Sign Up Page

 ![Sign Up Page](reeltalk/static/documents/lighthouse-desktop-sign-up.png)
 
 #### Search Page
 
 ![Search Page](reeltalk/static/documents/lighthouse-desktop-search-movies.png)
 
  #### Add Review Page
 
 ![Add Review Page](reeltalk/static/documents/lighthouse-desktop-review.png)
 
 #### Edit Review Page
 
 ![Edit Review Page](reeltalk/static/documents/lighthouse-desktop-edit-review.png)
 
 #### My Reviews Page
 
 ![My Reviews Page](reeltalk/static/documents/lighthouse-desktop-my-reviews.png)
 
 #### Movie Reviews Page
 
 ![Movie Reviews Page](reeltalk/static/documents/lighthouse-desktop-movie-reviews.png)
 
 #### 404 Page
 
 ![404 Page](reeltalk/static/documents/lighthouse-desktop-404.png)
 
 #### 500 Page
 
 ![500 Page](reeltalk/static/documents/lighthouse-desktop-500-page.png)

 #### 403 Page
 
 ![403 Page](reeltalk/static/documents/lighthouse-desktop-403.png)

</details>

#### Mobile Testing

<details>
<summary>Lighthouse Mobile Testing Screen Shots</summary>

  #### Home Page

![Home Page](reeltalk/static/documents/lighthouse-mobile-home-page.png)

  #### Login Page

 ![Login Page](reeltalk/static/documents/lighthouse-mobile-login.png)

 #### Sign Up Page

 ![Sign Up Page](reeltalk/static/documents/lighthouse-mobile-sign-up.png)
 
 #### Search Page
 
 ![Search Page](reeltalk/static/documents/lighthouse-mobile-search-movies.png)
 
  #### Add Review Page
 
 ![Add Review Page](reeltalk/static/documents/lighthouse-mobile-review.png)
 
 #### Edit Review Page
 
 ![Edit Review Page](reeltalk/static/documents/lighthouse-mobile-edit-review.png)
 
 #### My Reviews Page
 
 ![My Reviews Page](reeltalk/static/documents/lighthouse-mobile-my-reviews.png)
 
 #### Movie Reviews Page
 
 ![Movie Reviews Page](reeltalk/static/documents/lighthouse-mobile-movie-reviews.png)
 
 #### 404 Page
 
 ![404 Page](reeltalk/static/documents/lighthouse-mobile-404.png)
 
 #### 500 Page
 
 ![500 Page](reeltalk/static/documents/lighthouse-mobile-500-page.png)

  #### 403 Page
 
 ![403 Page](reeltalk/static/documents/lighthouse-mobile-403.png)

</details>

### Wave Testing

<details>
<summary>Wave Testing Screen Shots</summary>

- All pages pass the Wave validator.

  #### Home Page

![Home Page](reeltalk/static/documents/wave-home-page.png)

  #### Login Page

 ![Login Page](reeltalk/static/documents/wave-login-page.png)

 #### Sign Up Page

 ![Sign Up Page](reeltalk/static/documents/wave-sign-up-page.png)
 
 #### Search Page
 
 ![Search Page](reeltalk/static/documents/wave-search-movies.png)
 
  #### Add Review Page
 
 ![Add Review Page](reeltalk/static/documents/wave-review.png)
 
 #### Edit Review Page
 
 ![Edit Review Page](reeltalk/static/documents/wave-edit-review.png)

 #### Delete Review Page
 
 ![Delete Review Page](reeltalk/static/documents//wave-delete-review.png)
  
 #### My Reviews Page
 
 ![My Reviews Page](reeltalk/static/documents/wave-my-reviews-page.png)
 
 #### Movie Reviews Page
 
 ![Movie Reviews Page](reeltalk/static/documents/wave-movie-reviews-page.png)
 
 #### 404 Page
 
 ![404 Page](reeltalk/static/documents/wave-404.png)
 
 #### 500 Page
 
 ![500 Page](reeltalk/static/documents/wave-500-page.png)

  #### 403 Page
 
 ![403 Page](reeltalk/static/documents/wave-403.png)

</details>

### CI Python Linter

- All Python code is consistent in style and conforms to the PEP8 style guide. The CI Python Linter has been used to check that the code conforms to PEP8 standard. This includes indentation, comments, trailing white spaces, maximum line length etc. 

All pages have passed the CI Python Linter.

### __init__.py

![init.py](reeltalk/static/documents/linter-init.py.png)

### models.py

![models.py](reeltalk/static/documents/linter-models.py.png)

### routes.py

![routes.py](reeltalk/static/documents/linter-routes.py.png)


### Manual Testing

### Testing User Stories

#### First Time Visitors

| Goals                                                        | How are they achieved?                                                                                                         |
| :----------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------- |
| Register for an account                                    | There is a sign up link on the home page which encourages a user to create an account.
| Search for movies | Once a user has signed up to an account. They can search for a movie by clicking the 'Review A Movie' nav link.
| Understand what the site is for and easily navigate their way around                          |   A description of what the site is is included on the home page.                                         |
| I want the website to be responsive across varying devices.  | Bootstrap has been used in order to make ReelTalk responsive across a variety of devices.                               |

#### Returning Visitors and Frequent Visitors

| Goals                                                                    | How are they achieved?                                                                                                                                                              |
| :----------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Log into created account.                 |  If a user is not logged into an account, a login link is provided on the navbar and home page.                                              |
|Create, edit and delete my own reviews. | A user has access to all of their reviews on the 'My Reviews Page' from here the user can edit and delete any existing reviews. They can create a new review by clicking on the 'Review A Movie' link. This allows a user to search for a movie and create a review.  |
|Read other users reviews. | All reviews for all reviewed movies are displayed on the 'Movie Review' page. |

### Full Testing

Full testing was performed on the following devices:

- Laptop:

  - Macbook Pro 2015 13 inch screen

- Mobile Devices:
  - iPhone 15 pro.
  - iPhone 12 pro.
  - iPhone 11 pro.
  - Phone X.

Each device tested the site using the following browsers:

- Google Chrome
- Safari

#### Nav Bar

| Feature                                            | Expected Outcome                                                       | Testing Performed                  | Result                                                      | Pass/Fail |
| -------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------- | ----------------------------------------------------------- | --------- |
| ReelTalk Logo                                   | Link directs the user back to the home page                            | Clicked title                      | Home page reloads                                           | Pass      |
| Login link (only shown if user is not logged in)                             | Directs user to the login page                                      | Clicked link                       | Redirected to the login page                                           | Pass      |
| Movie reviews link (logged in users only) | Directs user to the movie reviews page | Clicked link                       | Redirected to the movie reviews page                           | Pass      |
| My reviews link (logged in users only) | Directs user to the my reviews page | Clicked link                       | Redirected to the my reviews page                           | Pass      |
| Review a movie link (logged in users only) | Directs user to the Review a movie page | Clicked link                       | Redirected to the Review a movie page                           | Pass      |
| Logout link (logged in users only) | Directs user to the home page | Clicked link                       | Redirected to the home page                           | Pass      |

### Footer

| Feature                                            | Expected Outcome                                                       | Testing Performed                  | Result                                                      | Pass/Fail |
| -------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------- | ----------------------------------------------------------- | --------- |
| Facebook link                                   | Directs the user to Facebooks webpage in a new tab                             | Clicked logo                      | New tab opens on Facebooks webpage.                                           | Pass      |
| Twitter link                                   | Directs the user to Twitters webpage in a new tab                             | Clicked logo                      | New tab opens on Twitters webpage.                                           | Pass      |
| Instagram link                                   | Directs the user to Instagrams webpage in a new tab                             | Clicked logo                      | New tab opens on Instagrams webpage.                                           | Pass      |


#### Home Page

| Feature                                            | Expected Outcome                                                       | Testing Performed                  | Result                                                      | Pass/Fail |
| -------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------- | ----------------------------------------------------------- | --------- |
| Sign up button (logged out users only)                                    | Link directs the user to the sign up page                            | Clicked sign up button                      | Redirected to the sign up page                                           | Pass      |
| Login link (only shown if user is not logged in)                             | Directs user to the login page                                      | Clicked link                       | Redirected to the login page                                           | Pass      |
| Trending movied | The weeks top 12 trending movied are displayed | Loaded home page                       | Movie cards are dispplayed                           | Pass      |

#### Sign Up Page

| Feature                                            | Expected Outcome                                                       | Testing Performed                  | Result                                                      | Pass/Fail |
| -------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------- | ----------------------------------------------------------- | --------- |
| First name input                                    | The users first name should be more than 2 characters long                            | Entered first name less than 2 characters long                      | Flash message alerts the user they have not entered enough characters                                           | Pass      |
| Last name input                                    | The users should enter their last name                            | Entered last name                       |                                            | Pass      |
| Email input                                    | The users email should be more than 4 characters long                            | Entered email less than 4 characters long                      | Flash message alerts the user they have not entered enough characters                                           | Pass      |
| Email input (already in use)                                    | The users email must be unique                            | Entered email which already exists in the database                     | Flash message alerts the user that the email is already in use characters                                           | Pass      |
| Password input                                    | The users password should be between 8 and 20 characters long                            | Entered password less than 8 and more than 20 characters long                      | Flash message alerts the user they have not matched the correct criteria                                          | Pass      |
| Confirm password input                                    | The users password should match the password input field                            | Entered password which differs from the password input field                      | Flash message alerts the user that the passwords do not match                                          | Pass      |
| Sign up button                                    | Link directs the user to the home page and displayed a message indicating the user has been created                            | Clicked sign up button                      | Redirected to the home page. Flash message displayed                                           | Pass      |

#### Login Page

| Feature                                            | Expected Outcome                                                       | Testing Performed                  | Result                                                      | Pass/Fail |
| -------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------- | ----------------------------------------------------------- | --------- |
| Email input                                    | User to enter e-mail address                            | Enter email address                     | Flash message alerts the user if the email doesn't exist in the database                                           | Pass      |
| Password input                                    | User to enter password                            | Enter password                     | Flash message alerts the user if the password is incorrect                                           | Pass      |
| Login button                                    | Directs the user to the 'My Reviews' page and a flash message appears with 'Successful Login'                            | Click button                     | Redirected to the 'My Reviews' page                                           | Pass      |

#### My Reviews Page

| Feature                                            | Expected Outcome                                                       | Testing Performed                  | Result                                                      | Pass/Fail |
| -------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------- | ----------------------------------------------------------- | --------- |
| Edit button                                    | User directed to the edit review page                           | Click edit button                     | Redirected to the edit review page                                           | Pass      |
| Delete button                                    | Modal appears confirming if the user wants to delete the review                           | Clicked delete button                     | Modal appears with  a delete and close button                                           | Pass      |
| Delete button on modal                                    | Once clicked the review will be deleted and a message displayed confirming that the review has been deleted                           | Clicked delete button                     | Review is deleted and message displayed                                           | Pass      |
| Close button on modal                                    | Once clicked the modal will close                         | Clicked close button                     | Modal is closed                                           | Pass      |
| No Reviews                                    | If the user has not posted any reviews a message is displayed stating now reviews have been made yet                         | No reviews created                    | Message displayed stating no reviews made                                           | Pass      |

#### Edit Review Page

| Feature                                            | Expected Outcome                                                       | Testing Performed                  | Result                                                      | Pass/Fail |
| -------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------- | ----------------------------------------------------------- | --------- |
| Text input                                  | Users review is displayed ready to edit                           | Review editied                     | Review saved to the database with a flash message of success                                         | Pass      |
| Update review button                                  | User is directed to their 'My Reviews' page and a sucess message is displayed                           | Clicked update review button                     |  User redirected to the 'My Reviews' page and success message displayed                                       | Pass      |
| Back button                                  | User is directed to their 'My Reviews' page                           | Clicked back button                     |  User redirected to the 'My Reviews' page                                        | Pass      |


#### Movie Reviews Page

| Feature                                            | Expected Outcome                                                       | Testing Performed                  | Result                                                      | Pass/Fail |
| -------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------- | ----------------------------------------------------------- | --------- |
| On page load                                   | All user reviews are displayed                           | Loaded page                     | All reviews are shown                                         | Pass      |
| On page load                                   | If there are no reviews, then a message is displayed stating there are no reviews                            | Loaded page                     | No reviews message is displayed                                         | Pass      |

#### Search Movies Page

| Feature                                            | Expected Outcome                                                       | Testing Performed                  | Result                                                      | Pass/Fail |
| -------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------- | ----------------------------------------------------------- | --------- |
| Search input                                  | User to enter a movie title                           | Movie title entered                     | The search returns the movie title                                         | Pass      |
| Search input (No result)                                  | User to enter a movie title                           | Movie title entered                     | Flash message indicates there is no such movie title                                         | Pass      |
| Search button                                  | Directs user to search results page                           | Clicked button                     | Redircted to the search results page                                        | Pass      |

#### Search Results Page

| Feature                                            | Expected Outcome                                                       | Testing Performed                  | Result                                                      | Pass/Fail |
| -------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------- | ----------------------------------------------------------- | --------- |
| Movie card                                  | Once clicked directs the user to the review page                           | Clicked movie card                     | Redircted to the reviews page                                         | Pass      |
| Movie card image                                  | If no image is returned from the TMDB API a stock image is displayed                           | Searched for movie with no image                     | Stock TMDB image displayed                                         | Pass      |

#### Review Page

| Feature                                            | Expected Outcome                                                       | Testing Performed                  | Result                                                      | Pass/Fail |
| -------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------- | ----------------------------------------------------------- | --------- |
| Text input                                  | User to enter their review (this is a required field)                           | Review entered                     | Review saved to the database with a flash message of success                                         | Pass      |
| Submit review button                                  | User is directed to their 'My Reviews' page and a sucess message is displayed                           | Clicked submit review button                     |  User redirected to the 'My Reviews' page and success message displayed                                       | Pass      |

#### 403 & 404 Pages

| Feature                                            | Expected Outcome                                                       | Testing Performed                  | Result                                                      | Pass/Fail |
| -------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------- | ----------------------------------------------------------- | --------- |
| 403 - User tries to access another users reviews to edit/delete review                                  | 403 page is displayed                           | Tried to access another users reviews via the URL address                     | 403 page displayed along with a flash message                                         | Pass      |
| 404 - User tries to access a page which doesn't exist on the website                               | 404 page is displayed                           | Tried to access a webpage which doesnt exist on the website                     | 404 page displayed                                          | Pass      |


## Bugs

### Solved Bugs

| # | Bug | How I solved the issue |
| :--- | :--- | :--- |
| 1 | I was having an issue when deploying my project to Heroku. I was getting an error message `ModuleNotFoundError: No module named 'requests`     | I reached out to support to help diagnose the issue. It turns out that requests isn't a built in python module but is installed in gitpod by default. I added requests==2.28.1 to my requirements.txt file. Saved the changes and pushed to github and redeployed Reeltalk. These steps successfully resolved the issue  |
| 2 | When displaying the movie titles within the bootstrap cards on the movie and my reviews pages. Some of the titles returned from the API were particulary long which caused the cards to no longer display as a grid on the screen| I resolved this by implementing and if statement. The if statement determined whether the movie title was over 30 characters if the title was over 30 characters then the movie title would only show the first 30 characters and when hovered over would show the full title. If the title was less than 30 characters then the title would be displayed as normal. This resolved the isse and all cards were displayed as a grid  |

### Known Bugs

| # | Bug | 
| :--- | :--- | 
| 1 | The release date for each movie returned from the API is in US format. The date is used on each of the movie cards across the website. Eventually I would like to rectify the issue by converting the dates to UK format to match the review created date |
