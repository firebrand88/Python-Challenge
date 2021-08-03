
import csv
from datetime import datetime

Pydate = []
PNL = []

def main(Pydate, PNL):
    totalmonths = len(Pydate)
    print(totalmonths)

    nettotal = 0
    print(PNL)

    for x in PNL:
        nettotal = nettotal + x
    
    print(nettotal)

#total number of months
#net total amount of Profit/Losses over entire period
#calculate changes in Profit/Losses over the entire period, then find the average of those changes
#greatest increase in profits (date and amount) over the entire period
#greatest decrease in profits (date and amount) over the entire period

with open('budget_data.csv','r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    next(csv_reader)

    for row in csv_reader:
        Pydate.append(row[0])
        PNL.append(int(row[1]))

    # with open('new_PyBank.csv','w') as new_file:
    #     fieldnames = ['Date','Profit/Losses']

    #     csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',')

    # for row in csv_reader:
    #     print(row)

# if __name__ == '__main__':

main(Pydate, PNL)