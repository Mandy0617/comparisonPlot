import csv
import ast

# Input and output file paths
input_file_path = "lunar_qphi_1.csv"
output_file_path = "lunar_qphi_1_transfer.csvv"

with open(input_file_path, mode='r') as infile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames

    # Write to the output CSV file
    with open(output_file_path, mode='w', newline='') as outfile:
        fieldnames = ['Num episodes', 'Cumulative rewards']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            num_episodes = int(row['Num episodes'])
            rewards = ast.literal_eval(row['Cumulative rewards'])
            print(f"reward: {rewards}")

            # Split values into multiple lines
            for i in range(10, 60, 10):
                partial_rewards = rewards[i - 10:i]
                num = num_episodes - 50 + i
                writer.writerow({'Num episodes': str(num), 'Cumulative rewards': f"[{', '.join(map(str, partial_rewards))}]"})
