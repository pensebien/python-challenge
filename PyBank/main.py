import csv
import os

rows = []
#set path to csv file
file = os.path.join ('Resources', 'budget_data.csv')
# name the variable header
header = []
total_months = 0
total = 0
average_change = 0
monthly_change = 0
previous_value = 0
total_monthlychange = 0
greatest_increase_profit = ["", 0]
greatest_decrease_profit =["", 0]

# open the file in "read" mode ('r') and store the contents in the variable "text"

with open (file,'r') as text:
    readercsv = csv.reader(text, delimiter=",")
    header = next(readercsv)

    

    for n, row in enumerate(readercsv):
        # You are free to delete this part
        # The line above is intend for the code to get an enumerator. 
        # Something like a counter. 
        # The goal is to I want to skip the first loop. 
        # I use the variable "n" to store the Value of the counter. 


        rows.append(row)
        # Skip the month of Jan, but use the month of Feb
        if n >  0:
            monthly_change = (int(row[1]) - previous_value)
            total_monthlychange += monthly_change
            
        # Answering the before last and last question.
        # 1. We need to have all the changes in the P&L so we can compare them
        # 2. The greatest would be the Greatest Increase in Profits
        # 3. The smallest would be Greatest Decrease in Profits

        # Obviously in our For Loop, we have being calculating monthlychange, all we need to do now is put it into an Array.

            if greatest_increase_profit[1] < monthly_change:
                greatest_increase_profit[1] = monthly_change
                greatest_increase_profit[0] = row[0]
            
            if greatest_decrease_profit[1] > monthly_change:
                greatest_decrease_profit[1] = monthly_change
                greatest_decrease_profit[0] = row[0]
           

        total += int(row[1])
        previous_value = int(row[1])

average_change = ((total_monthlychange)/(len(rows)-1))


print("The total months:", len(rows))
print("Total: $",total) # improve code by deleting space between the dollar sign and value
#print("Average Change: $")
print("Average_Change: $ ", average_change)
print("The greatest Increase: ", greatest_increase_profit[0], greatest_increase_profit[1])
print("The greatest Decrease: ", greatest_decrease_profit[0],greatest_decrease_profit[1])