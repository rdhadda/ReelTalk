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

## Testing

Testing was continuous throughout the website build. I used Chrome developer tools to identify and address any issues as they arose.

- My automated testing consisted of using W3C Validator, JSHint, Lighthouse, Wave and the CI Linter python.
- I then manually tested the user stories along with the functionality of the website.

## Automated Testing

### W3C Validator

W3C validator was used to validate the HTML on all pages of the website. It was also used to validate CSS in the style.css file.


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



### JavaScript Validator

[JSHint](https://jshint.com/) was used to validate the JavaScript.

- [Script.js](reeltalk/static/documents/jshint-script.js.png)


### Lighthouse Testing

I took the opportunity to utilize Lighthouse within Chrome Developer Tools. This allowed me to test for performance, accessibility, best practices and the SEO (search engine optimization) of the website.

#### Desktop Testing

<details>
<summary>Lighthouse Desktop Testing</summary>

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
 
 ![500 Page](reeltalk/static/documents/lighthouse-desktop-404.png)

</details>

#### Mobile Testing

<details>
<summary>Lighthouse Mobile Testing</summary>

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
 
 ![500 Page](reeltalk/static/documents/lighthouse-mobile-404.png)

</details>

### Wave Testing

- [Index Page HTML](documentation/wave-index.html.png)
- [Game Page HTML](documentation/wave.game.html.png)
- [Score Page HTML](documentation/wave-score.html.png)
- [404 Page HTML](documentation/wave-404.html.png)

#### CI Python Linter



### Manual Testing

### Testing User Stories

#### First Time Visitors

| Goals                                                        | How are they achieved?                                                                                                         |
| :----------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------- |
| I want to be able to play quiz online.                       | ReelTalk is a web-based quiz, which accessible across desktop, tablet and mobile devices.                                    |
| I want to be able to navigate through the website with ease. | The website uses a series of buttons to allow the player to easily navigate the website. ![buttons](documentation/buttons.png) |
| I want to be able to enter my name.                          | There is an input field on the home page which allows the user to enter their name.                                            |
| I want the website to be responsive across varying devices.  | Media queries have been used in order to make ReelTalk responsive across a variety of devices.                               |

#### Returning Visitors and Frequent Visitors

| Goals                                                                    | How are they achieved?                                                                                                                                                              |
| :----------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I want a variety of questions across different subjects.                 | There are a variety of questions which are randomly selected each time the game is played.                                                                                          |
| I want to be able to select the difficulty of the questions being asked. | On the game page of ReelTalk, the player is presented with three difficulty level buttons. Once selected the questions being asked will be determined on the difficulty selected. |

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

#### Home Page

| Feature                                            | Expected Outcome                                                       | Testing Performed                  | Result                                                      | Pass/Fail |
| -------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------- | ----------------------------------------------------------- | --------- |
| The Sites title                                    | Link directs the user back to the home page                            | Clicked title                      | Home page reloads                                           | Pass      |
| Enter Your Name Input                              | Allows Player to Enter their name                                      | Entered name                       | Name is displayed                                           | Pass      |
| Start Game button becomes is initially unavailable | Button becomes available to click once a player has entered their name | Entered name                       | Button becomes available to click                           | Pass      |
| Start Game                                         | Directs the user to the game page                                      | Clicked on button                  | Game page opens to display the questions                    | Pass      |
| How to play button                                 | Opens the accordion with the instructions on how to play the game      | Clicked on button                  | accordion with instructions on how to play opens            | Pass      |
| All buttons - hover effect                         | All purple buttons should highlight with a blue neon effect background | Hover over each button on the page | Each button displayed the correct styling when hovered over | Pass      |

#### Game Page

| Feature                                                            | Expected Outcome                                                                                                                                | Testing Performed                                              | Result                                                                                                   | Pass/Fail |
| ------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | --------- |
| The Sites title                                                    | Link directs the user back to the home page                                                                                                     | Clicked title                                                  | Home page reloads                                                                                        | Pass      |
| Easy Button                                                        | Easy questions are displayed                                                                                                                    | Click easy button                                              | Easy questions are displayed                                                                             | Pass      |
| Medium Button                                                      | Medium questions are displayed                                                                                                                  | Click easy button                                              | Medium questions are displayed                                                                           | Pass      |
| Hard Button                                                        | Hard questions are displayed                                                                                                                    | Click easy button                                              | Hard questions are displayed                                                                             | Pass      |
| Easy/Medium/Hard Button Disabled                                   | Once one of the buttons are clicked all three buttons become un-clickable                                                                       | Click easy/medium/hard button                                  | All buttons become un-clickable                                                                          | Pass      |
| Choice boxes disabled until player selects difficulty of questions | Choice boxes are disabled                                                                                                                       | Click easy/medium/hard button                                  | Choice boxes are no longer disabled and are clickable                                                    | Pass      |
| All buttons - hover effect                                         | All purple buttons should highlight with a blue neon effect background                                                                          | Hover over each button on the page                             | Each button displayed the correct styling when hovered over                                              | Pass      |
| Question populated                                                 | The question from available questions array is correctly pulled from question.js                                                                | Started a new game                                             | The question is displaying                                                                               | Pass      |
| Answers populated                                                  | The answers from available questions array is correctly pulled from question.js                                                                 | Started a new game                                             | The four answer choices are displaying correctly                                                         | Pass      |
| Unable to change answer selection                                  | Once a player has selected an answer, they're unable to change their selection                                                                  | Tried to select a different answer from the original selection | Unable to select alternate answer                                                                        | Pass      |
| Correct answer                                                     | When a correct answer is clicked the box around the answer should display green with a tick                                                     | Clicked on a correct answer                                    | box displayed green with a tick                                                                          | Pass      |
| Incorrect answer                                                   | When an incorrect answer is clicked the answer should highlight red with a cross and the correct answer should be highlighted green with a tick | Clicked incorrect answer                                       | incorrect answer is highlighted red with a cross and the correct answer is highlighted green with a tick | Pass      |
| Progress bar                                                       | When a question has been answered the progress bar should increment by one                                                                      | Clicked answer box                                             | Progress bar is incremented by 1                                                                         | Pass      |

#### Score Page

| Feature                                       | Expected Outcome                                                                              | Testing Performed                  | Result                                                      | Pass/Fail |
| --------------------------------------------- | --------------------------------------------------------------------------------------------- | ---------------------------------- | ----------------------------------------------------------- | --------- |
| The Sites title                               | Link directs the user back to the home page                                                   | Clicked title                      | Home page reloads                                           | Pass      |
| Score appears with a comment and players name | Once the player has successfully completed a game a message appears with their name and score | Completed a game                   | Message appears with name and score                         | Pass      |
| All buttons - hover effect                    | All purple buttons should highlight with a blue neon effect background                        | Hover over each button on the page | Each button displayed the correct styling when hovered over | Pass      |
| Play Again - Button                           | Directs the user to the game page                                                             | Clicked on button                  | Game page opens to display the questions                    | Pass      |

#### 404 Page

| Feature                    | Expected Outcome                                                       | Testing Performed                  | Result                                                      | Pass/Fail |
| -------------------------- | ---------------------------------------------------------------------- | ---------------------------------- | ----------------------------------------------------------- | --------- |
| The Sites title            | Link directs the user back to the home page                            | Clicked title                      | Home page reloads                                           | Pass      |
| All buttons - hover effect | All purple buttons should highlight with a blue neon effect background | Hover over each button on the page | Each button displayed the correct styling when hovered over | Pass      |
| Take Me Home - Button      | Directs the user to the homepage page                                  | Clicked on button                  | Homepage is displayed                                       | Pass      |
