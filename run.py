import gspread # imports all of gspread library 
from google.oauth2.service_account import Credentials #imports just the credentials class req for this project

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ] # The scope lists the APIs that the  program should access in order to run.

CREDS = Credentials.from_service_account_file('creds.json')

SCOPED_CREDS = CREDS.with_scopes(SCOPE) # creation of a new constant variable, passed the scope variable
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS) #client with a gspread.authorize method
SHEET = GSPREAD_CLIENT.open('love_sandwiches') # access love sandwiches sheet using open method on the client object. 

sales = SHEET.worksheet('sales') # corresponds to name ('sales' of the worksheet in love_sandwiches sheet.

# data = sales.get_all_values() # pulls values from sales worksheet (checks if API working, not requird once done)
# print(data)

# note normally sales data would be collected with an API between Python program and love sandwiches uers but for this project, a user is required to imput data into the terminal 

#csv = comma-separated values, a file type to give table structured format
# first function to collect sales data from user

def get_sales_data():
    """
    Get sales figures input from the user
    """
    print('Please enter sales data from the last market.') # instructions for user
    print("Data should be six numbers, separated by commas.")
    print("Example: 10,20,30,40,50,60\n") #\n puts a space between lines

    data_str = input('Enter your data here:') # where user inputs data ( output a string)
    print(f"The data provided is {data_str}") # checks values are assinged

get_sales_data() # call function



