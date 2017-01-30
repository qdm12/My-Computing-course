from calculations import Transaction, find_total_sales, find_participation, find_client_max_spent
# The line above uses what we have worked on previously

def read_transactions(worksheet):   
    legend = worksheet['1']
    #["Date", "Time", "Client", "Trees bought", "Gnomes bought", "Chocolates bought", "Balls bought"]
    transactions = []
    number_transactions = len(worksheet['A']) - 1 #-1 for legend
    for row in range(2, number_transactions):
        date = worksheet.cell(row = row, col = 1)
        time = worksheet.cell(row = row, col = 2)
        client = worksheet.cell(row = row, col = 3)
        trees = worksheet.cell(row = row, col = 4)
        gnomes = worksheet.cell(row = row, col = 5)
        chocolates = worksheet.cell(row = row, col = 6)
        balls = worksheet.cell(row = row, col = 7)
        transaction = Transaction(date, time, client, trees, gnomes, chocolates, balls)
        transactions.append(transaction)
    return transactions  
                
if __name__ == "__main__":
    # This is where the main code is ran if you run this file
    # we use that weird __name__ thingy so that you can IMPORT that file elsewhere
    workbook = load_workbook("transactions.xlsx")
    worksheet = workbook['Transactions']
    transactions = read_transactions(worksheet)
    print "First transaction: "+str(transactions[0])
    print "Last transaction: "+str(transactions[-1])
    
    # Adding something to the worksheet
    worksheet.cell(row = 1, col = 8, value = "Trolling Hard") # Writes at the end of the legend row
    workbook.save("transactions.xlsx") #You need to save back your changes