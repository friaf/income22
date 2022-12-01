# Income calculator program

## How to use


### Description
This program is inspired by mom, as she loves counting daily, monthly and yearly incomes. 
She has a lot of differenet incomes that come during the month on random days so income calculator is done for her or people like her to ease life.
Program is updating data in work sheets, calculating monthly income per type and monthly total.


![screens]()

## Features
 
### Existing features

-	Header
     - Header shows to user from the first sign that this is a game Rock, Paper, Scissors.

![screens](/assets/)

-	Message section
     - Has a welcoming message explaining what user/player should do to start the game. During the game message in the field changes depending on game results. Messages are: It’s a win! (if player wins), It’s a draw! (if player and computer chose the same element) or Computer wins!  (if user losses). Every message is supported with sound that represents win, lose or draw.

![screens](/assets/images/message.png)

-	The game result
     - It’s a score area with 0 for computer and for player. When player wins score changes to +1 if computer wins the same, if it’s a draw no one gets a point, and the score stays the same.

![screens](/assets/images/score.png)

-	The game options
     - User and computer have 3 options to choose from, it is button with a hand that shows rock, paper or scissors.  When user chose button to play, computer starts thinking his option for couple of seconds, during these seconds computer’s buttons blink one after another. When the choice is done for both parties, buttons are highlighted with yellow color.

![screens](/assets/images/choice.png)

-	Rules button and popup.
     - When user presses on the button game page is becoming black and a popup windows pops in the middle of the screen with the rules of the game. After closing this window, user returns to game.

![screens](/assets/images/rules-toggle.png)
![screens](/assets/images/rules-popup.png)

### Features to implement
- In the future game should have more of casino and gambling features like a money bag        with amount on it for computer and user where coins fall after each win and add a score scheme where if its a win 2 times in a row, double amount is added to money bag.

## Testing

- I tested playing this game in different browsers: Chrome, Firefox.
- I confirmed that the game results are always correct
- I confirmed that header, message area, score area, options and rules button work correctly, easy to understand and navigate.
- I confirmed that colors and fonts chosen are easy to read and accessible by running it through lighthouse in devtools.

![screens](/assets/images/testing.png)

- I confirmed that this project is responsive, looks good and functions on all standard screen sizes using the devtools device toolbar.

### Bugs

Game did not look good on my phone after i have checked deployed link for the game, i have added @media screen and (max-width: 380px) and it looked great. 


### Validator Testing
- HTML 
    - no errors were returned when passing through the oficial W3C validator.
- CSS 
    - no errors were found when passing through the official (Jigsaw) validator.
- JS hint
    - 14 worning saying (use 'esversion: 6'), but not mistakes.


### Unfixed bugs

14 worning saying (use 'esversion: 6')  on JS hint


## Deployment
The site was deployed to GitHub pages. The steps to deploy are as followes.

- In the GitHub repository navigate to the settings tab
- From the source section drop-down menu, select the Master Branch
- Once the master branch has been selected, the page provided the link to the complit website.


## Credits

### Content
- Toggle modal for rules button - https://www.youtube.com/watch?v=KX0NR5HtQ1Q
- Keyboard navigation - https://christianheilmann.com/2016/08/15/better-keyboard-navigation-with-progressive-enhancement/
- Blink effect for computer;s choice - https://www.w3docs.com/snippets/css/how-to-create-a-blinking-effect-with-css3-animations.html
- Sound effects - https://www.w3schools.com/graphics/game_sound.asp
- Idea on switch statement for game - https://alexabotello.medium.com/javascript-rock-paper-scissors-game-5c7dbb10038a
- Compuer thinking on his move (timer) - https://www.freecodecamp.org/news/javascript-settimeout-how-to-set-a-timer-in-javascript-or-sleep-for-n-seconds/#:~:text=The%20JavaScript%20setTimeout()%20method,to%20pass%20one%20thousand%20milliseconds%20.

### Media

- Icon for restart button - https://fontawesome.com/
- Icons for choices - https://www.pinterest.com/
- Sound - https://www.zapsplat.com/
- Favicon - https://favicon.io/





















![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome friaf,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!