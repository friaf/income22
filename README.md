# Income calculator program

## How to use


### Description
Income calculator is dedicated to my mather, person that loves counting numbers especially if its income numbers :-)
Calculator is useful for anyone who is keeping track of personal income or family income. Program updates income data, calculates monthly total and total for each income type based on input data.


![screens](/images/responsive.png)

## Features
 
### Existing features

-	Welcome message
     - Explains what functions program does with the input data.

![screens](/images/welcome_msg.png)

-	Input section
     - In this section program requires input of daily income from the user. Example of input data is provided for the user. 

![screens](/images/request_for_data.png)

-	
     - User inputs data that is requested and program validates it, so it passes requirements.
     - If data is incorrect program comes back to Input section to try again, ot loops until user inputs valid data. 

![screens](/images/input_of_data_and_validation.png)
![screens](/images/invaliddata.png)

-	Updating daily income to work sheet
     - If user inputs valid data, this data is updated and stored in the work sheet
     - Program chooses work sheet to update depending on the current month.
     Example: if its November program updates work sheet for November, etc.

![screens](/images/updating_sheet.png)

-	Calculating monthly total by type section.
     - This function runs by the program monthly, calculating total for each type of income for previouse month on the 1 day of current month and updating work sheet with calculated sum.

![screens](/images/updating_and_calculating_types.png)

-	Calculating monthly total
     - This function runs by the program monthly, calculating monthly total for the previouse month on the first day of current month and updates new work sheet for the total_permonth.

![screens](/images/updating_and_calculating_monthly_income.png)

### Features to implement
- In future i will add calculation of yearly total and what month and type of income was most profitable.

## Testing

I have manually tested this project by doing the following
- Passed the code through a PEP8 linter and confirmed there are no problems
- Given invalid inputs: like strings and more numbers to see if it validtes correctly. No problems where found
- Checked if google sheets are updated correctly and if it updates on correct days.No problems where found
- Tested in my local terminal and the Code Institute Heroku terminal


### Bugs

 Found bugs

 ![screens](/images/error1.png)
 
 Fixed bugs

 ![screens](/images/fixed_error1.png)

 - When i wrote project function total_by_column didnt work becouse i couldnt use veriable stored in the other function, but i have inserted one function to another integer_num = convert_str(data) so i could use its variables stored in there. After this function worked correctly.



### Remaining Bugs

- No bugs remaining

### Validator testing

- No bugs 


## Deployment
This project was deployed using Code Institute's mock terminal for heroku

Steps for deployment:
- Fork or clone this repository
- Create a new heroku app
- Set the buildbacks to Python and NodeJS in that order
- Set the buildbacks to PORT and 8000
- Link the Heroku app to the repository
- Click on --> Deploy


## Credits

- Code institute for the deployment terminal
- My mother for inspiration and income data
- Walk through project3 "Love Sandwiches" for idea
- Google Sheets






























