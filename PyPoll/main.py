import csv
import os

rows = []
#set path to csv file
file = os.path.join ('Resources', 'budget_data.csv')
# name the variable header
header = []
total_months = 0
total = 0

# open the file in "read" mode ('r') and store the contents in the variable "text"

with open (file,'r') as text:
    readercsv = csv.reader(text, delimiter=",")





#print(lines)
#print("End of Printing LInes")
header = next(readercsv)
for row in readercsv:
    rows.append(row)
    total += row[1]

print(row)
print("This is the array")
print(rows)
print("The total months:", len[rows])
print("Total : $", total)