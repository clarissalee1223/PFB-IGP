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

    # Find the highest overhead category
    highest_overhead_category = find_highest_overhead_category(overhead_data)

    result = {'highest_overhead_category': highest_overhead_category}

    # Write results to a text file
    with open("overheads_summary.txt", "w") as summary_file:
        summary_file.write("Overheads Results:\n")
        summary_file.write(f"Highest Overhead Category: {result['highest_overhead_category']}\n")

    return result

def find_highest_overhead_category(overhead_data):
    # Initialize variables to store the highest overhead information
    highest_overhead_category = ""
    highest_overhead_value = 0

    # Iterate through each row in the overhead data
    for row in overhead_data:
        category = row['category']
        overhead = row['amount']

        # Check if the current overhead is higher than the current highest overhead
        if overhead > highest_overhead_value:
            highest_overhead_value = overhead
            highest_overhead_category = category

    return highest_overhead_category