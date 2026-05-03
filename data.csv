import json
import csv

with open('2nd SEM/Class Codes/Unit-4/data_new.json', 'r') as f:
    data = json.load(f)

with open('2nd SEM/Class Codes/Unit-4/main.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    
    writer.writeheader()
    writer.writerows(data)

print("CSV file created successfully")