#Group: Better_Buys
#cash_on_hand.py

import csv
def process_cash_on_hand(file_path):
    cash_data = []
    
    #read csv file
    # with open("CASH ON HAND.csv") as csv_file
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            # print(row)
            # Key for Day column could be corrupted.
            cash_data.append({'day': int(row['ï»¿Day']), 'amount': float(row['Cash On Hand'])}) 

     # calculate the difference in cash-on-hand
    deficit_row = []
    for i in range(1, len(cash_data)):
        difference = cash_data[i]["amount"] - cash_data[i - 1]["amount"]
        if (difference < 0):
            deficit_row.append({"day": cash_data[i]["day"], "cash_deficit": abs(difference)})

    return deficit_row
