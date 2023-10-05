# Dependencies
import os
import csv

#variables
month_count = 0
profits = 0
total = 0
last_month = 0
change = 0
months = []
changes = []

# Set path for file
csvpath = os.path.join( "Resources", "budget_data.csv")

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    
    #count months
    for row in csvreader:
        month_count += 1
        profits = int(row[1])
        total += profits

        if month_count == 1:
            last_month = profits
            continue

        else:
            change = profits - last_month
            months.append(row[0])
            changes.append(change)
            last_month = profits

    #find average change      
    total_loss = sum(changes)
    average = round(total_loss/(month_count - 1), 2)
    greatest_increase = max(changes)
    greatest_decrease = min(changes)

    #find months withs greatest profits and greatest losses
    best_month_index = changes.index(greatest_increase)
    worst_month_index = changes.index(greatest_decrease)
    best_month = months[best_month_index]
    worst_month = months[worst_month_index]

    #print values
    print('Financial Anlysis')
    print('-----------------------')
    print(f'Total Months: {month_count}')
    print(f'Total: ${total}')
    print(f'Average Change: ${average}')
    print(f'Greatest Increase in Profits: {best_month} (${greatest_increase})')
    print(f'Greatest Decrease in Profits: {worst_month} (${greatest_decrease})')

    #export text file
    with open('pybank.txt', "w") as f:

        f.write("Financial Analysis\n")
        f.write("----------------------------\n")
        f.write(f"Total Months: {month_count}\n")
        f.write(f"Total: ${total}\n")
        f.write(f"Average Change: ${average}\n")
        f.write(f"Greatest Increase in Profits: {best_month} (${greatest_increase})\n")
        f.write(f"Greatest Decrease in Profits: {worst_month} (${greatest_decrease})\n")
