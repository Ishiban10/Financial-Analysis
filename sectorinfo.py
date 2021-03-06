import requests
import json

# I will change the symbol and run this script for all the top stocks I have written for each sector and add
# all their information for the balance sheet, income statement, and cash flow in different json files, this way
# I don't have to access the api and instead can access my own json files

symbol = 'COP'  # ticker goes here

url_income_statement = f"https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={symbol}&apikey=KJHOTYX4RQYVFABB"
url_balance_sheet = f"https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={symbol}&apikey=KJHOTYX4RQYVFABB"
url_cash_flow = f"https://www.alphavantage.co/query?function=CASH_FLOW&symbol={symbol}&apikey=KJHOTYX4RQYVFABB"

income_statement = requests.get(url_income_statement)
balance_sheet = requests.get(url_balance_sheet)
cash_flow = requests.get(url_cash_flow)

income_statement_data = income_statement.json()
balance_sheet_data = balance_sheet.json()
cash_flow_data = cash_flow.json()

json_object_balance = json.dumps(balance_sheet_data)
json_object_cash = json.dumps(cash_flow_data)
json_object_income = json.dumps(income_statement_data)

with open(f'SectorFinAnalysisJson/{symbol}Json/{symbol}income.json', 'w') as f:
    f.write(json_object_income)

with open(f'SectorFinAnalysisJson/{symbol}Json/{symbol}cash.json', 'w') as c:
    c.write(json_object_cash)

with open(f'SectorFinAnalysisJson/{symbol}Json/{symbol}balance.json', 'w') as b:
    b.write(json_object_balance)

