# Election_Analysis

## Overview of Election Audit

Seth, a Colorado Board of Elections employee delegated a task to perform analysis and audit of election data. 

The initial analysis required to on the data included delivering information by writing and running a python script to identify following for the board: 

       - Total number of votes cast
       - A complete list of candidates who received votes
       - Total number of votes each candidate received
       - Percentage of votes each candidate won
       - The winner of the election based on popular vote

In addition to this further analysis was requested to fetch: 

    - The voter turnout for each county
    - The percentage of votes from each county out of the total count
    - The county with the highest turnout

### Explain the purpose of this election audit analysis

The purpose of this election audit analysis was to find the winner of the election based on popular votes and find the county votes with largest county turnout to get a breakdown of the votes casted per candidates. 

## Election-Audit Results: 

The analysis of the data showed following results:

Total of 369,711 votes were cast in the election.

The candidates were: 
    1. Charles Casper Stockham
    2. Diana DeGette
    3. Raymon Anthony Doane

Largest County Turnout: Denver

County Votes:
Jefferson: 10.5% (38,855)
Denver: 82.8% (306,055)
Arapahoe: 6.7% (24,801)

Candidates /votes:
- Charles Casper Stockham: 23.0% (85,213)
- Diana DeGette: 73.8% (272,892)
- Raymon Anthony Doane: 3.1% (11,606)

Diane DeGette received the maximum votes of 73.8% with a vote count of 272,892. This was a sweeping win over the other candidates. Charles Casper Stockham received 23% of the votes with a vote count of 85,213 and Raymon Anthony Doane received 3.1% votes with a vote count of 11,606. 

Out of the total votes 369,711, the county with maximum votes was Denver county with percentage votes 82.8% and vote count of 306,855, followed by Jefferson with 10.5% / 38,855 vote count and finally Arapahoe with 6.7% votes / 24,801 vote count.

## Election-Audit Summary: 

Winner of the election was Diana DeGette with 272,892 votes which makes 73.8% of total votes! Further analysis can be performed to identify the most popular candidate per county. 

The election analysis first involved downloading the csv file and understanding the dataset. The script written was used to identify the candidates, understand the total votes casted in the election, and then building up the script to find vote count per candidate and percentage votes per candidate. It further looked at applying same logic to find county level information. This is a useful script that could be used for similar election analysis and serve as a template for election data analysis. 

Usually election data includes many counties and may also need information such as maximum votes of candidates per county and percentage votes cast in each county against the county population. A nested for loop could be similarly used for such analysis but in my opinion as this script requires correct syntax and indentation, I would recommend investing in exploring other tools such as Jupyter notebook  or other tools that would simplify running the analysis. To build on existing application if there was data available on the party affiliation, the analysis could be similarly extended to run the similar logic and find which candidates represents a particular party. 

While there are challenges foreseen if their are larger sets of data involved and more columns to analyze, this script does serve as a good starting point for election data analysis that is similar in scope to this dataset. 

