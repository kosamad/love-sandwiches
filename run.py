import gspread # imports all of gspread library 
from google.oauth2.service_account import Credentials #imports just the credentials class req for this project
from pprint import pprint


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
    Get sales figures input from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of 6 numbers separated
    by commas. The loop will repeatedly request data, until it is valid.
    """

    while True:
        print('Please enter sales data from the last market.') # instructions for user
        print("Data should be six numbers, separated by commas.")
        print("Example: 10,20,30,40,50,60\n") #\n puts a space between lines

        data_str = input('Enter your data here:') # where user inputs data ( output a string)
        # print(f"The data provided is {data_str}") # checks values are assinged. this is removed once we know the code is valid
    
        # convert string value into a list, (req to insert values into spreadsheet)
        sales_data = data_str.split(',') # break up at commas and remove commas
        # print(sales_data)
        
        # CHECKING DATA IS VALID
        if validate_data(sales_data):
            print("Data is valid!")
            break
    return sales_data # (make sure there is somnewhere for these return values to go (at bottom where function was called))

    # while loop to repeat request for data until valid data is inputed (prevent a user having to go back to the start)

 
def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    # print(values)

    try: 
        [int(value) for value in values] #convert strings into integers (checks if a number has been entered.) instead of a for loop have used list comprehension
        if len(values) != 6:
            raise ValueError(
                f'Exactly 6 values required, you provided {len(values)}'
            )
    except ValueError as e: #python shorthand for error (e)
        print(f"Invalid data: {e}, please try again.\n")
        return False
    
    return True # this helps us determine if the data was valid and links to while loop in get_data function



def update_sales_worksheet(data):
    """
    Update sales worksheet, add new row with the list data provided
    """
    print('updating sales worksheet...\n') # gives user feedback and helps narrow down bugs.
    sales_worksheet = SHEET.worksheet('sales') #accessing sales worksheet
    sales_worksheet.append_row(data) # using a append_row method to insert our data into the sheet.
    print("Sales worksheet updated successfully.\n")

def update_surplus_worksheet(data):
    """
    Update surplus worksheet, add new row with the data caluculated
    """
    print('updating surplus worksheet...\n') # gives user feedback and helps narrow down bugs.
    surplus_worksheet = SHEET.worksheet('surplus') #accessing sales worksheet
    surplus_worksheet.append_row(data) # using a append_row method to insert our data into the sheet.
    print("Surplus worksheet updated successfully.\n")

def calculate_surplus_data(sales_row):
    """
    Compare sales with stock and calculate the surplus for each item type.

    The surplus is defined as the sales figure subtracted from the stock:
    - Positive surplus indicates waste
    - Negative surplus indicates extra made when stock was sold out.
    """
    print("Calculating surplus data...\n")
    stock = SHEET.worksheet('stock').get_all_values()
    # pprint(stock)
    stock_row = stock[-1] # this slice method will get the final item from a list and return the variable


    surplus_data = [] #empty list for data below

    for stock, sales in zip(stock_row, sales_row): #see notes on zip method, allows you to move through two lists at once.
        surplus = int(stock) - sales # int method here converts straight away. Saves a line of code doing separatly.
        surplus_data.append(surplus)
    
    return surplus_data

# common practise to wrap all main function calls in a function called main (before this they were just at the bottom of the page)
def main():
    """
    Run all program functions
    """
    data = get_sales_data() # call function
    sales_data = [int(num) for num in data] #convert strings into integers 
    update_sales_worksheet(sales_data)
    new_surplus_data = calculate_surplus_data(sales_data)
    update_surplus_worksheet(new_surplus_data)

print("Welcome to Love Sandwiches Data Automation")
main()
    