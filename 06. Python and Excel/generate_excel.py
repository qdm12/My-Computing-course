from openpyxl import Workbook
from openpyxl.styles import Font
from os.path import isfile
from datetime import datetime, timedelta
from random import randint
from operator import itemgetter

def convert_string_datetime(date_string):
    date_list = map(int, date_string.split('/'))
    date = datetime(date_list[2], date_list[1], date_list[0])
    return date

def convert_datetime_string(date_datetime):
    date = date_datetime.strftime('%d/%m/%Y')
    return date

def generate_random_time():
    time = randint(0, 86399)
    return time, str(timedelta(seconds = time))


def generate_transactions():
    if isfile("transactions.xlsx"):
        raise Exception("Transactions excel file already exists, aborting !")
    legend = ["Date", "Time", "Client", "Trees bought", "Gnomes bought", "Chocolates bought", "Balls bought"]
    clients = ["John", "Mike", "Alberto", "Suzy", "Yonnis", "Barbara", "Jennifer", "James"]
    today = datetime.today()
    year_start = datetime(2017, 01, 01)
    
    transactions = []
    date = year_start
    for _ in range((today - year_start).days):
        date_str = convert_datetime_string(date)
        day_transactions = []
        for _ in range(randint(0,40)): #random number of transactions
            time, time_str = generate_random_time()
            client = clients[randint(0, len(clients) - 1)]
            tx = [time, date_str, time_str, client, randint(0,4), randint(0,7), randint(0,30), randint(0,35)]
            day_transactions.append(tx)
        day_transactions = sorted(day_transactions, key=itemgetter(0))
        for tx in day_transactions:
            transactions.append(tx[1:])
        date += timedelta(days=1)
    
    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = "Transactions"
    
    worksheet.append(legend)
    for cell in worksheet['1']:
        cell.font = Font(bold=True)
        
    for tx in transactions:
        worksheet.append(tx)
    
    workbook.save("transactions.xlsx")
    
if __name__ == "__main__":
    generate_transactions()