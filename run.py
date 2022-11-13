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

"""
income_august_22 = SHEET.worksheet("income_august_22")
income_september_22 = SHEET.worksheet("income_september_22")
income_october_22 = SHEET.worksheet("income_october_22")

august_data = income_august_22.get_all_values()
september_data = income_september_22.get_all_values()
october_data = income_october_22.get_all_values()

print(august_data)
print(september_data)
print(october_data)
"""

def get_august_data():
    """
    Get income data from the user
    """
    print("Please enter your last income")
    print("Data should be 3 numbers, separated by commas.")
    print("Example: 80, 90, 100\n")

    data_str = input("Enter your income here: ")

    august_data = data_str.split(",")
    validate_data(august_data)

    #print(f"Income you have provided is {data_str}")


def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 3 values.
    """
    try:
        [int(value) for value in values]
        if len(values) !=3:
            raise ValueError(
                f"exactly 3 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")




get_august_data()