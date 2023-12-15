import csv
import ast

# Input and output file paths
input_file_path = "lunar_qphi_1.csv"
output_file_path = "lunar_qphi_1_transfer.csv"


# Read data from the input CSV file
with open(input_file_path, 'r') as input_file:
    reader = csv.reader(input_file)
    rows = [row for row in reader]

# Write data to the output CSV file
with open(output_file_path, 'w', newline='') as output_file:
    writer = csv.writer(output_file)
    
    # Write header
    writer.writerow(['Num episodes', 'Cumulative rewards'])
    
    num = 0
    for row in rows:
        # Extract values from the row (assuming they are comma-separated)
        values = [float(value) for value in row if value.strip()]
        
        # Create lists of 10 values
        for i in range(0, len(values) - 9, 10):
            num_episodes = 10 + i + num
            cumulative_rewards = values[i:i + 10]
            
            # Write a row to the output file
            writer.writerow([num_episodes, cumulative_rewards])
        num = num + 500