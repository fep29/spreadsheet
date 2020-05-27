import csv
with open ('sales.csv','r') as csv_file:
    sales = csv.DictReader(csv_file)
