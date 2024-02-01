#Group: Better_Buys
#profit_loss.py

import csv
def process_profit_loss(file_path):
    profit_data = []

    #read csv file
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            # Key Day column may be corrupted
            profit_data.append({'day':int(row['ï»¿Day']),'net_profit': float(row['Net Profit'])})

 #calculate the difference in the net profit
    profit_deficit = []
    for i in range(1, len(profit_data)):
        difference = profit_data[i]["net_profit"] - profit_data[i-1]["net_profit"]
        if (difference < 0):
            profit_deficit.append({"day": profit_data[i]["day"], "profit_deficit": abs(difference)})

    return profit_deficit