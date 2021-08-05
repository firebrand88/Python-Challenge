import csv
import os
import pandas as pd

election_csv = os.path.join("..","Resources","election_data.csv")

PyVoter = []
Candidates = []

df = pd.read_csv(election_csv)

def main(PyVoter,Candidates,kvotes,cvotes,lvotes,ovotes):
    with open('PyVote_results.txt','w') as new_file:
        totalvotes = len(df)
        candlist = df["Candidate"].unique()  #get list of candidates in dataset
        # print(len(candlist))  # ['Khan' 'Correy' 'Li' "O'Tooley"]
        # nullvalues = df.isnull().sum()  #check to see if there are blank cells
        # print(nullvalues)  

        pctk = kvotes/totalvotes
        pctc = cvotes/totalvotes
        pctl = lvotes/totalvotes
        pcto = ovotes/totalvotes
        candies = {
            "Khan": pctk,
            "Correy": pctc,
            "Li": pctl,
            "O'Tooley": pcto
        }

        pctwin = 0

        for i in candies:
            if candies[i] > pctwin:
                pctwin = candies[i]

        def get_key(x):
            for k, v in candies.items():
                if x == v:
                    return k

        wincd = get_key(pctwin)

        print("Election Results")
        new_file.write("Election Results\n")
        print("------------------------")
        new_file.write("------------------------\n")
        print(f"Total Votes: {totalvotes:,}")
        new_file.write(f"Total Votes: {totalvotes:,}\n")
        print("------------------------")
        new_file.write("------------------------\n")
        print(f"Khan: {pctk:.1%} ({kvotes:,})")
        new_file.write(f'Khan: {pctk:.1%} ({kvotes:,})\n')  #Khan data
        print(f"Correy: {pctc:.1%} ({cvotes:,})")
        new_file.write(f'Correy: {pctc:.1%} ({cvotes:,})\n')  #Correy data
        print(f"Li: {pctl:.1%} ({lvotes:,})")
        new_file.write(f'Li: {pctl:.1%} ({lvotes:,})\n')  #Li data
        print(f"O'Tooley: {pcto:.1%} ({ovotes:,})")
        new_file.write(f"O'Tooley: {pcto:.1%} ({ovotes:,})\n")  #O'Tooley data
        print("------------------------")
        new_file.write("------------------------\n")
        print(f"Winner: {wincd}")
        new_file.write(f"Winner: {wincd}\n")
        print("------------------------")
        new_file.write("------------------------\n")


with open(election_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)

    kvotes = 0
    cvotes = 0
    lvotes = 0
    ovotes = 0

    for row in csv_reader:
        if row[2] == 'Khan':
            kvotes = kvotes + 1
        elif row[2] == 'Correy':
            cvotes = cvotes + 1
        elif row[2] == 'Li':
            lvotes = lvotes + 1
        else:
            ovotes = ovotes + 1


main(PyVoter,Candidates,kvotes,cvotes,lvotes,ovotes)