# Income calculator program

## How to use


### Description
This program is inspired by my mather, as she loves counting daily, monthly and yearly incomes. 
She has a lot of differenet incomes that come during the month on random days so income calculator is done for her or people like her to ease life.
Program is updating data in work sheets, calculating monthly income per type and monthly total.


![screens](/images/responsive.png)

## Features
 
### Existing features

-	Welcome message
     - Header shows to user from the first sign that this is a game Rock, Paper, Scissors.

![screens](/images/welcome_msg.png)

-	Message section
     - Has a welcoming message explaining what user/player should do to start the game. During the game message in the field changes depending on game results. Messages are: It’s a win! (if player wins), It’s a draw! (if player and computer chose the same element) or Computer wins!  (if user losses). Every message is supported with sound that represents win, lose or draw.

![screens](/images/request_for_data.png)

-	The game result
     - It’s a score area with 0 for computer and for player. When player wins score changes to +1 if computer wins the same, if it’s a draw no one gets a point, and the score stays the same.

![screens](/images/input_of_data_and_validation.png)

-	The game options
     - User and computer have 3 options to choose from, it is button with a hand that shows rock, paper or scissors.  When user chose button to play, computer starts thinking his option for couple of seconds, during these seconds computer’s buttons blink one after another. When the choice is done for both parties, buttons are highlighted with yellow color.

![screens](/images/updating_sheet.png)

-	Rules button and popup.
     - When user presses on the button game page is becoming black and a popup windows pops in the middle of the screen with the rules of the game. After closing this window, user returns to game.

![screens](/images/updating_and_calculating_types.png)

-	Rules button and popup.
     - When user presses on the button game page is becoming black and a popup windows pops in the middle of the screen with the rules of the game. After closing this window, user returns to game.

![screens](/images/updating_and_calculating_monthly_income.png)

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


### Media

- Icon for restart button - https://fontawesome.com/
- Icons for choices - https://www.pinterest.com/
- Sound - https://www.zapsplat.com/
- Favicon - https://favicon.io/





















