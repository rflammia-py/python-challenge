import csv
import pandas as pd
from pathlib import Path

input_file = Path('/Users/ryan/Desktop/bootcamp/homework/hw3_pybank/python-challenge/PyBank/Resources/budget_data.csv')

#csv file to pandas dataframe
bank_df = pd.read_csv(input_file, encoding="utf-8")

#seperate column to find sum of profits and losses
profit_loss_column = bank_df["Profit/Losses"]
sum_profit = profit_loss_column.sum(axis=0)

#seperate column to find Count of dates
dates_column = bank_df["Date"]
count_date = dates_column.count()

#shift profit loss column to find difference between each row
shifted_profit= bank_df["Profit/Losses"].shift(1)

#find the difference and calculate the average
difference_profit = profit_loss_column - shifted_profit
average_profit_change = (round(difference_profit.mean(), 2))

#find max change in profit for "greatest increase"
greatest_increase = (int(difference_profit.max()))
#find date where max occured
date_great_increase = bank_df.sort_values('Profit/Losses').tail(1).Date

#find min change in profit for "greatest decrease"
greatest_decrease = (int(difference_profit.min()))
#find date where min occured
date_great_decrease = bank_df.sort_values('Profit/Losses').head(1).Date


#Print Statements
print("Financial Analysis")
print("---------------------------------------------")
print(f"Total Months: {count_date}")
print(f"Total Net Profit: ${sum_profit}")
print(f"Average Change: ${average_profit_change}")
print(f"Greatest Increase in Profits:{date_great_increase.to_string(index=False)} (${greatest_increase})")
print(f"Greatest Decrease in Profits:{date_great_decrease.to_string(index=False)} (${greatest_decrease})")

#export code to text-file
with open("output.txt", "a") as f:
    print("Financial Analysis", file=f)
    print("---------------------------------------------", file=f)
    print(f"Total Months: {count_date}", file=f)
    print(f"Total Net Profit: ${sum_profit}", file=f)
    print(f"Average Change: ${average_profit_change}", file=f)
    print(f"Greatest Increase in Profits:{date_great_increase.to_string(index=False)} (${greatest_increase})", file=f)
    print(f"Greatest Decrease in Profits:{date_great_decrease.to_string(index=False)} (${greatest_decrease})", file=f)