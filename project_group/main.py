# Group: Better_Buys
# main.py

from cash_on_hand import process_cash_on_hand
from overheads import process_overheads
from profit_loss import process_profit_loss


# process cash on hand data
cash_on_hand_result = process_cash_on_hand("project_group\csv_reports\CASH ON HAND.csv")

# process overheads data
overheads_result = process_overheads("project_group\csv_reports\OVERHEADS.csv")

# process profit and loss data
profit_loss_result = process_profit_loss("project_group\csv_reports\PROFIT AND LOSS.csv")

# sort the data
cash_deficit_list = []
for row in cash_on_hand_result:
    cash_deficit_list.append(row["cash_deficit"])

sorted_cash_deficit_list = sorted(cash_deficit_list)


profit_deficit_list = []
for row in profit_loss_result:
    profit_deficit_list.append(row["profit_deficit"])

sorted_profit_deficit_list = sorted(profit_deficit_list)


# write results to summary_report.txt
with open("summary_report.txt", "w") as summary_file:
    # HIGHEST OVERHEAD
    summary_file.write(
        f"[HIGHEST OVERHEAD] {overheads_result['category']}: {overheads_result['Overheads']}\n")
    # CASH DEFICIT
    for row in cash_on_hand_result:
        summary_file.write(
            f"[CASH DEFICIT] DAY: {row['day']}, AMOUNT: SGD{row['cash_deficit']}\n")
    # TOP 3 CASH DEFICIT
    for row in cash_on_hand_result:
        if row["cash_deficit"] == sorted_cash_deficit_list[-1]:
            summary_file.write(
                f"[HIGHEST CASH DEFICIT] DAY: {row['day']}, AMOUNT: SGD{row['cash_deficit']}\n")
    for row in cash_on_hand_result:
        if row["cash_deficit"] == sorted_cash_deficit_list[-2]:
            summary_file.write(
                f"[2ND HIGHEST CASH DEFICIT] DAY: {row['day']}, AMOUNT: SGD{row['cash_deficit']}\n")
    for row in cash_on_hand_result:
        if row["cash_deficit"] == sorted_cash_deficit_list[-3]:
            summary_file.write(
                f"[3RD HIGHEST CASH DEFICIT] DAY: {row['day']}, AMOUNT: SGD{row['cash_deficit']}\n")
    # NET PROFIT DEFICIT
    for row in profit_loss_result:
        summary_file.write(
            f"[NET PROFIT DEFICIT] DAY: {row['day']} AMOUNT: SGD{row['profit_deficit']}\n")
    # TOP 3 NET PROFIT DEFICIT
    for row in profit_loss_result:
        if row["profit_deficit"] == sorted_profit_deficit_list[-1]:
            summary_file.write(
                f"[HIGHEST NET PROFIT DEFICIT] DAY: {row['day']}, AMOUNT: SGD{row['profit_deficit']}\n")
    for row in profit_loss_result:
        if row["profit_deficit"] == sorted_profit_deficit_list[-2]:
            summary_file.write(
                f"[2ND HIGHEST NET PROFIT DEFICIT] DAY: {row['day']}, AMOUNT: SGD{row['profit_deficit']}\n")
    for row in profit_loss_result:
        if row["profit_deficit"] == sorted_profit_deficit_list[-3]:
            summary_file.write(
                f"[3RD HIGHEST NET PROFIT DEFICIT] DAY: {row['day']}, AMOUNT: SGD{row['profit_deficit']}\n")
