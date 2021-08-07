
import csv
from datetime import datetime
import os

budget_csv = os.path.join("..","Resources","budget_data.csv")
Pydate = []
pnl = []
pnl_chg = []

def main(Pydate, pnl, pnl_chg, big_inc, big_dec,mo_inc,mo_dec):
    with open('PyBank_results.txt','w') as new_file:
        totalmonths = len(Pydate)
        print(f'Total months: {totalmonths}')  #total number of months
        new_file.write(f'Total months: {totalmonths}\n')  #total number of months

        nettotal = sum(pnl)
        print(f'Total: ${nettotal:,}')  #net total amount of Profit/Losses over entire period
        new_file.write(f'Total: ${nettotal:,}\n')  #net total amount of Profit/Losses over entire period

        avg_chg = sum(pnl_chg)/len(pnl_chg)
        print(f'Average Change: -${abs(avg_chg):,.2f}')  #average of changes of Profit/Losses over entire period
        new_file.write(f'Average Change: -${abs(avg_chg):,.2f}\n')  #average of changes of Profit/Losses over entire period

        print(f'Greatest Increase in Profits: {mo_inc} (${big_inc:,})')  #greatest increase in profits (date and amount) over the entire period
        print(f'Greatest Decrease in Profits: {mo_dec} (-${abs(big_dec):,})')  #greatest decrease in profits (date and amount) over the entire period
        new_file.write(f'Greatest Increase in Profits: {mo_inc} (${big_inc:,})\n')  #greatest increase in profits (date and amount) over the entire period
        new_file.write(f'Greatest Decrease in Profits: {mo_dec} (-${abs(big_dec):,})\n')  #greatest decrease in profits (date and amount) over the entire period


with open(budget_csv,'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    next(csv_reader)

    count = 0
    prev_chg = 0
    big_inc = 0
    big_dec = 0

    for row in csv_reader:
        Pydate.append(row[0])
        pnl.append(int(row[1]))

        if count >= 1:
            chg_calc = int(row[1])-prev_val
            pnl_chg.append(chg_calc)

            if chg_calc > big_inc:
                big_inc = chg_calc
                mo_inc =row[0]
            
            if chg_calc < big_dec:
                big_dec = chg_calc
                mo_dec = row[0]
        
        prev_val = int(row[1])
        count = count + 1

main(Pydate, pnl, pnl_chg, big_inc, big_dec,mo_inc,mo_dec)