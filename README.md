# python-challenge

## Background
I used Python and Pandas to analyzse financial records and election polling data. 


## PyBank
I created Panda DataFrames to analyze PyBank data. From the [budget_data.csv](https://github.com/rflammia-py/python-challenge/blob/main/PyBank/Resources/budget_data.csv), I converted the csv into Panda DataFrames to effectively sum the profit and calculate the averages.
### Code Output:
    Financial Analysis
    ---------------------------------------------
    Total Months: 86
    Total Net Profit: $38382578
    Average Change: $-2315.12
    Greatest Increase in Profits: Feb-2012 ($1926159)
    Greatest Decrease in Profits: Sep-2013 ($-2196167)


## PyPoll
I created Panda DataFrames to analyze and determine election data. Given [election_data.csv](https://github.com/rflammia-py/python-challenge/blob/main/PyPoll/Resources/election_data.csv), I was able to solve the following:
 
  - The total number of votes cast

  - A complete list of candidates who received votes
 
  - The percentage of votes each candidate won

  - The total number of votes each candidate won

  - The winner of the election based on popular vote.
### Code Output:

    Election Results
    ---------------------------------------------
    Total Votes: 3521001
    ---------------------------------------------
              Percentage    Votes
    Khan            63.0  2218231
    Correy          20.0   704200
    Li              14.0   492940
    O'Tooley         3.0   105630
    ---------------------------------------------
    Winner
    Khan
    
