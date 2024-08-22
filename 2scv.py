import json
import csv

# Load the JSON data
with open('test-9aa10-default-rtdb-export.json', 'r') as json_file:
    data = json.load(json_file)

# Define the CSV file name
csv_file_name = 'gyroscope_data.csv'

# Open CSV file for writing
with open(csv_file_name, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # Write header
    csv_writer.writerow(['timestamp', 'x', 'y', 'z'])
    
    # Write data
    for key, value in data['gyroscope'].items():
        csv_writer.writerow([value['timestamp'], value['x'], value['y'], value['z']])

print(f'Data has been written to {csv_file_name}')
