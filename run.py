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

data = sales.get_all_values() # pulss values from sales worksheet

print(data)