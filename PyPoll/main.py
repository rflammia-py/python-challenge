import csv
import pandas as pd
from pathlib import Path

input_file = Path('/Users/ryan/Desktop/bootcamp/homework/hw3_pybank/python-challenge/PyPoll/Resources/election_data.csv')

#csv file to pandas dataframe
poll_df = pd.read_csv(input_file, encoding="utf-8")

#seperate columns to find Count of votes
total_votes = poll_df["Voter ID"].count()

#find individual candidates count
candidate_count = poll_df["Candidate"].value_counts()

#percentage candidate name occurs
candidate_percentage = round(poll_df["Candidate"].value_counts(normalize=True) * 100, 3)

#find the winner; candidate with the highest vote count
winner = poll_df["Candidate"].value_counts().idxmax()

#Print Statements
print("Election Results")
print("---------------------------------------------")
print(f"Total Votes: {total_votes}")
print("---------------------------------------------")
print(pd.DataFrame({'Percentage': candidate_percentage,'Votes': candidate_count}))
print("---------------------------------------------")
print(f"Winner: {winner}")



#export code to text-file
with open("output.txt", "a") as f:
    print("Election Results", file=f)
    print("---------------------------------------------", file=f)
    print(f"Total Votes: {total_votes}", file=f)
    print("---------------------------------------------", file=f)
    print(pd.DataFrame({'Percentage': candidate_percentage,'Votes': candidate_count}), file=f)
    print("---------------------------------------------", file=f)
    print(f"Winner: {winner}", file=f)