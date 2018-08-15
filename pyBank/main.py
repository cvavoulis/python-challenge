import os
import csv

months=[]
revenue=[]
changeinpl=0
all_changes=[]
avg_change=0
max_increase=0
max_decrease=0

csvpath=os.path.join("..","pyBank","budget_data.csv")
with open (csvpath, 'r') as csvfile: 
    csvreader=csv.reader(csvfile, delimiter=",")


    header=next(csvreader)


    for row in csvreader:
        months.append(row[0])
        revenue.append(int(row[1]))
        totalrevenue=sum(revenue)
        totalmonths=len(months)


for row in range(totalmonths-1): 
    changeinpl=revenue[row+1]-revenue[row]
    all_changes=all_changes + [changeinpl]


avg_change = sum(all_changes)/(totalmonths-1)
max_increase=(max(all_changes))
max_index=all_changes.index(max_increase)
max_month=months[max_index+1]

max_decrease=(min(all_changes))
min_index=all_changes.index(max_decrease)
min_month=months[min_index+1]

# max_decrease=changeinpl.index(min(all_changes))


print("Financial Analysis")
print("-----------------------")
print("Total Months: "+ str(totalmonths))
print("Total: "+ str(totalrevenue))
print("Average change: "+ str(avg_change))
print("Greatest Increase in Profits "+ str(max_month) + " " +str(max_increase))
print("Greatest Decrease in Profits " + str(min_month) + " " +str(max_decrease))

