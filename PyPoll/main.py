#Import modules
import os
import csv

in_file=open("/Users/coramicsunescu/Desktop/UCD_BootCamp/03-Python/Python-Challenge/PyPoll/Resources/election_data.csv")
reader= csv.reader(in_file)
next(reader)

Votes=[]
Candidates=[]

print("Election Results")
print("---------------------")
print("Total Votes")
print("------------------------")
