import csv

# Input and output file paths
input_file_path = "lunar_adrl_1 copy.csv"
output_file_path = "lunar_adrl_1_cut.csv"

with open(input_file_path, 'r') as infile:
    # Create a CSV reader
    reader = csv.DictReader(infile)
    
    # Extract the header
    header = reader.fieldnames
    
    # Read all rows into a list
    all_rows = list(reader)

# Take only the last 100 lines
last_100_rows = all_rows[-248:]

# Modify "Num episodes" and write to the output CSV file
with open(output_file_path, 'w', newline='') as outfile:
    # Create a CSV writer
    writer = csv.DictWriter(outfile, fieldnames=header)
    
    # Write the header to the output file
    writer.writeheader()
    
    # Write modified rows
    for i, row in enumerate(last_100_rows):
        # Decrease the original "Num episodes" by 4000
        row['Num episodes'] = str(int(row['Num episodes']) - 2520)
        
        # Write the modified row to the output file
        writer.writerow(row)

print(f"Output written to {output_file_path}")