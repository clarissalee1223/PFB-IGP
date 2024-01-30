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
    profit_diff = [profit_data[i]['net_profit'] - profit_data[i-1]['net_profit'] for i in range(1,len(profit_data))]

    #check if net profit is always increasing or decreasing 
    if all(i >= 0 for i in profit_diff):
        #net profit is always increasing 
        highest_increment = max(profit_diff)
        increment_day = profit_diff.index(highest_increment) + 2
        result = {'highest_increment': {'day': increment_day, 'amount': highest_increment}}


    elif all(i <= 0 for i in profit_diff):
        #net profit is always decreasing
        highest_decrement = min(profit_diff)
        decrement_day = profit_diff.index(highest_decrement) + 2
        result = {'highest_decrement': {'day': decrement_day, 'amount': highest_decrement}}

    else:
        # net profit fluctuates
        deficit_days_amounts = []
        for i in range(len(profit_diff)):
            deficit_days_amounts.append({'day': i+2, 'amount': -profit_diff[i]})

        #sort the deficit days by amount
        for i in range(len(deficit_days_amounts)):
            for j in range(i+1, len(deficit_days_amounts)):
                if deficit_days_amounts[i]['amount'] < deficit_days_amounts[j]['amount']:
                    deficit_days_amounts[i], deficit_days_amounts[j] = deficit_days_amounts[j], deficit_days_amounts[i]

    #get the top 3 highest deficit days
    top_3_deficit_days = deficit_days_amounts[:3]
    result = {'top_3_deficit_days': top_3_deficit_days}

    return result  