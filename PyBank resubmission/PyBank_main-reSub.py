# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period
# Worked with Tutor Mark Fullton on both projects

# Import the necessary dependencies for os.path.join()
import os
import csv

# Create a path to collect data from the budget_data.csv file in the Resources folder
budget_csv=os.path.join("Resources", "budget_data.csv")

# Create a path to send final data to result file Analysis folder
Result_txt=os.path.join("Analysis", "Result_txt")


# Set the variables for total months and net total amount to zero 
# (variable needs to be declared and initialized to a value)
Month_numbers = 0
total_amount = 0

# Create Lists for the total number of months in the dataset and net total amount "Profit/Losses" over period
NumberMonths_list = []
ProfitLoss_list = []

# use `next(csv_reader)` because there is header for this file, 
# To read through each row of data after the header, use 'for row in csv_reader:'
#    csv_reader = csv.reader(csvfile, delimiter=",")
# append() method in python adds a single item to the existing list. 
# append() will modify the original list by adding the item to the end of the list
# use (row[0]) and (row[1]) for months and P&L columns respectively
# Used amount += int(row[1]) as same as saying  amount = int(row[1]) + amount
# Including the newline="" parameter allows the csv module to handle the line endings itself,  replicating the format as defined in your csv
with open(budget_csv, newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        Month_numbers +=1
        total_amount += int(row[1])
        NumberMonths_list.append(row[0])
        ProfitLoss_list.append(int(row[1]))
        
# Generate a new list to store monthly differences
# Calculate the difference between the months 
Month_Diff=[]
for row in range(Month_numbers-1):
    Month_Diff.append(ProfitLoss_list[row+1]-ProfitLoss_list[row])

# Calculate the average change in P & L over the entire period, sum of monthly difference div by number of months
# format number to 2 decimal places
average_change=sum(Month_Diff)/(Month_numbers)
average_change_formatted=round(average_change,2)

# Find the max and min differences
# Use index() to searches for max and min the start of the Month_Diff list  
# The index() method is a member function of the list class. And is widely used to search values in a list.
max_increase=Month_Diff.index(max(Month_Diff))
max_decrease=Month_Diff.index(min(Month_Diff))

# find the greatest profit increase and decrease and months they occurred in
greatest_profit_increase=Month_Diff[max_increase]
greatest_profit_decrease=Month_Diff[max_decrease]
greatest_profit_increase_month=NumberMonths_list[max_increase]
greatest_profit_decrease_month=NumberMonths_list[max_decrease]
 
# output formatted results to terminal
# Examples used: 
# print(f"Stats for {name}")
# print(f"WIN PERCENT: {win_percent}")
# print(f"{name} is a {type_of_wrestler}")
# :, puts commas in numbers to show hundreds - easier to read
print("Financial Analysis")
print("---------------------------------")
print(f"Total Months: {Month_numbers}")
print(f"Total: ${total_amount:,}")
print(f"Average Change: ${average_change_formatted:,}")
print(f"Greatest Increase in Profits: {greatest_profit_increase_month} (${greatest_profit_increase:,})")
print(f"Greatest Decrease in Profits: {greatest_profit_decrease_month} (${greatest_profit_decrease:,})")

# # output Summary lines to results.csv file
# Write updated data to csv file  
with open(Result_txt, "w", encoding='utf-8', newline="") as writefile:
    # writer = txt.writer(writefile)
    writefile.write("Financial Analysis\n")
    writefile.write("---------------------------------\n")
    writefile.write(f"Total Months: {Month_numbers}\n")
    writefile.write(f"Total: ${total_amount:,}\n")
    writefile.write(F"Average Change: ${average_change_formatted:,}\n")
    writefile.write(f"Greatest Increase in Profits: {greatest_profit_increase_month} (${greatest_profit_increase:,})\n")
    writefile.write(f"Greatest Decrease in Profits: {greatest_profit_decrease_month} (${greatest_profit_decrease:,})\n")

# EXAMPLE writing to csv file
# csvpath = os.path.join("output", filename)
# with open(csvpath, "w") as csvfile:
#     fieldnames = ["last_name", "first_name", "ssn", "email"]
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(new_employee_data)
