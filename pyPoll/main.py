import csv
import os


csvpath=os.path.join("..", "pyPoll","election_data.csv")

candidates = []
total_votes = 0

with open(csvpath, 'r') as csv_file:
    csvreader = csv.reader(csvfile, delimiter=',')
    header=next(csvreader)
    for row in csvreader:
        totalvotes += 1
        candidates.append(row[2])


