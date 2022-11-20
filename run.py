from datetime import datetime
from pprint import pprint
import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("income_22")


income_august_22 = SHEET.worksheet("income_august_22")
income_september_22 = SHEET.worksheet("income_september_22")
income_october_22 = SHEET.worksheet("income_october_22")
income_november_22 = SHEET.worksheet("income_november_22")
income_december_22 = SHEET.worksheet("income_december_22")
income_january_23 = SHEET.worksheet("income_january_23")
income_fabruary_23 = SHEET.worksheet("income_fabruary_23")
income_march_23 = SHEET.worksheet("income_march_23")
income_april_23 = SHEET.worksheet("income_april_23")
income_may_23 = SHEET.worksheet("income_may_23")
income_june_23 = SHEET.worksheet("income_june_23")
income_july_23 = SHEET.worksheet("income_july_23")


def get_data():
    """
    Get income data from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of 3 numbers separated by
    commas. The loop will repeatedly request data, until it is valid.

    """
    while True:
        print("Please enter your last income")
        print("Data should be 3 numbers, separated by commas.")
        print("Example: 80, 90, 100\n")
        date_now = datetime.now().strftime('%B %d, %Y')
        data_str = input(f"Enter your income for {date_now} here: ")
        new_data = data_str.split(",")
        if validate_data(new_data):
            print("Data is valid!\n")
            break
    return new_data


def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 3 values.
    """
    try:
        [int(value) for value in values]
        if len(values) != 3:
            raise ValueError(
                f"exactly 3 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def update_income_worksheet(data):
    """
    Update income worksheets depending on current
    month, add new row with provided income.
    """
    print("Updating income worksheet...\n")
    date_now = datetime.now().strftime('%B')
    if date_now == "August":
        income_august_22.append_row(data)
    elif date_now == "September":
        income_september_22.append_row(data)
    elif date_now == "October":
        income_october_22.append_row(data)
    elif date_now == "November":
        income_november_22.append_row(data)
    elif date_now == "December":
        income_december_22.append_row(data)
    elif date_now == "January":
        income_january_23.append_row(data)
    elif date_now == "Fabruary":
        income_fabruary_23.append_row(data)
    elif date_now == "March":
        income_march_23.append_row(data)
    elif date_now == "April":
        income_april_23.append_row(data)
    elif date_now == "May":
        income_may_23.append_row(data)
    elif date_now == "June":
        income_june_23.append_row(data)
    elif date_now == "July":
        income_july_23.append_row(data)
    print("Income is updated successfully.\n")
   

def convert_str(data):
    """
    Remove string header to change all string income data to
    integers in order to sum up collumns of different incomes.
    """
    all_values = income_october_22.get_all_values()
    check_values = ['income 1', 'income 2', 'income 3']
    num = list(filter(lambda row: not any(
        el in row for el in check_values), all_values))
    integer_num = num 
    integer_num = [list(map(int, i)) for i in integer_num]
    return integer_num


def main():
    """
    Run all program functions.
    """
    data = get_data()
    new_data = [int(num) for num in data]
    update_income_worksheet(new_data)
    convert_str(data)
   
     
print("Welcome to income analyzing program\n")
main()
