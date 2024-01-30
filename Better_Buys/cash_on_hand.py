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

    #calculate the difference in cash-on-hand
    cash_diff = []
    for i in range(1, len(cash_data)):
        cash_diff.append(cash_data[i]['amount'] - cash_data[i-1]['amount'])

    cash_diff = [cash_data[i]['amount'] - cash_data[i-1]['amount'] for i in range(1, len(cash_data))]

    #find the day and amount of the highest increment and decrement
    highest_increment = max(cash_diff)
    highest_decrement = min(cash_diff)

    increment_day = cash_diff.index(highest_increment) + 2
    decrement_day = cash_diff.index(highest_decrement) + 2

    result = {
        'highest_increment': {'day': increment_day, 'amount': highest_increment},
        'highest_decrement': {'day': decrement_day, 'amount': highest_decrement},
    }

    #write results to a text file
    with open("cash_on_hand_summary.txt","w") as summary_file:
        summary_file.write("Cash-on-Hand Results:\n")
        summary_file.write(f"Highest Increment: Day {result['highest_increment']['day']}, Amount {result['highest_increment']['amount']}\n")
        summary_file.write(f"Highest Decrement: Day {result['highest_decrement']['day']}, Amount {result['highest_decrement']['amount']}\n")

        return result
