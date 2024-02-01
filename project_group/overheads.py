#Group: Better_Buys
#overheads.py

import csv
def process_overheads(file_path):
    overhead_data = []

    # Read csv file
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            # Key Category column may be corrupted
            overhead_data.append({'category': row['ï»¿Category'], 'amount': float(row['Overheads'])})


# create a function to determine the highest overhead
def highest_overhead_value(overhead_data):
    #for overhead_value in overhead_data:
    print(overhead_data)







