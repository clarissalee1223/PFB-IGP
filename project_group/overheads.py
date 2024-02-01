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
            overhead_data.append({'category': row['ï»¿Category'], 'Overheads': float(row['Overheads'])})

    highest_overhead_val = highest_overhead_value(overhead_data)
    highest_overhead = highest_overhead_row(overhead_data,highest_overhead_val)
    return highest_overhead

# create a function to determine the highest overhead
def highest_overhead_value(overhead_data):
    highest_overhead = 0
    for row in overhead_data:
        if (row["Overheads"] > highest_overhead):
            highest_overhead = row["Overheads"]

    return highest_overhead
            
def highest_overhead_row(overhead_data, highest_overhead):
    for row in overhead_data:
        if (row["Overheads"] == highest_overhead):
            return row










