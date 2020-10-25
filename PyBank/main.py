#Import Modules
import os
import csv

#Specify file path, activate csv reader 
#Please see https://stackoverflow.com/questions/14257373/skip-the-headers-when-editing-a-csv-file-using-python/14257599#14257599 

in_file= open("/Users/coramicsunescu/Desktop/UCD_BootCamp/03-Python/Python-Challenge/PyBank/Resources/budget_data.csv")
reader= csv.reader(in_file)
next(reader)

#Define lists for looping
date=[]
profits=[]
change=[]

#Please see https://stackoverflow.com/questions/46965192/python-how-can-i-find-difference-between-two-rows-of-same-column-using-loop-in
#Column[0] contains the months, Column[1] contains the profits/losses. Add up total months. Add up net total profits/losses 

#Create for loop
for row in reader:
    date.append(row[0])
    profits.append(float(row[1]))
for i in range(1,len(profits)):
    change.append(profits[i]-profits[i-1])
    average_change=round(sum(change)/len(change),2)

#Calculate greatest increase/decrease using max and min functions. Round to 2 decimal places
    max_change= round(max(change),2)
    min_change= round(min(change),2)

#Define two new variables to include the months in which the changes occured
    max_change_date=str(date[change.index(max(change))])
    min_change_date=str(date[change.index(min(change))])

#Print results
print("Financial Analysis:")
print("-----------------------------")
print("Total Months:", len(date))
print("Net Total:", sum(profits))
print("Average Change in Profit/Losses:",round(average_change))
print("Greatest increase in profits:", max_change_date,"($",max_change,")")
print("Greatest decrease in profits:", min_change_date,"($", min_change,")")