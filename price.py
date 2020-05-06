import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)

client = gspread.authorize(creds)

sheet = client.open("Restock").sheet1

#stuff = sheet.get_all_records()
#print(stuff)

emailList = sheet.col_values(1)[1:]
urlList = sheet.col_values(2)[1:]

print(emailList)
print(urlList)




