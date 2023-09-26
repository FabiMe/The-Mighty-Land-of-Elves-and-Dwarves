import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Initialize Google Sheets API
scope = ["https://www.googleapis.com/auth/spreadsheets"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)

# Open the spreadsheet
spreadsheet = client.open("Your Spreadsheet Name")
worksheet = spreadsheet.sheet1
