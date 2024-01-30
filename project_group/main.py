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


# write results to summary_report.txt
with open("summary_report.txt", "w") as summary_file:
    summary_file.write("Cash on Hand Results:\n")
    summary_file.write(str(cash_on_hand_result) + "\n\n")

    summary_file.write("Overheads Results:\n")
    summary_file.write(str(overheads_result) + "\n\n")

    summary_file.write("Profit and Lost Result:\n")
    summary_file.write(str(profit_loss_result) + "\n\n")
