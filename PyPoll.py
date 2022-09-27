# Data we need to retrieve
# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote

# # Import the datetime class from the datetime module.
# import datetime as dt
# # Use the now() attribute on the datetime class to get the present time.
# now = dt.datetime.now()
# # Print the present time.
# print("The time right now is ", now)

# Assign a variable for the file to loan and the path
file_to_load= 'C:/Users/ashrs/Desktop/Election_Analysis/Resources/election_results.csv'
#'Resources/electrion_results.csv' 

# Open the election results and read the file 
with open(file_to_load) as election_data:
#election_data = open(file_to_load, 'r')

    # To do: perform analysis 
    print(election_data)

#close the file
#election_data.close()

import csv
import os

# Assign a variable for the file to loan and the path
#file_to_load= os.path.join("..", "Resources", "election_results.csv")

#Create a filename variable to a direct or indirect path to the file 
file_to_save = os.path.join("analysis","election_analysis.txt")

#1 Initialize a total vote counter
total_votes = 0

# Candidate options 
candidate_options = []

# Declare empty dictionary 
candidate_votes = {}

# Open the election results and read the file 
with open(file_to_load) as election_data:

#Read the file object with the reader function
    file_reader = csv.reader(election_data)

#Print the header row 
    headers =next(file_reader)
    #print(headers)

#Print each row in CSV file 
for row in file_reader: 
   #print(row)
   # Add to the total vote count 
   total_votes += 1

#Print candidate name from each row
candidate_name= row[2]

#If candidate does not match any existing candidate 
if candidate_name not in candidate_options:
    
    # Add it to the list of candidate 
    candidate_options.append(candidate_name)

# Begin tracking that candidates vote count 
candidate_votes[candidate_name]=0

# Add a vote to that candidate's count
candidate_votes[candidate_name] += 1

#Print candidate vote dictionary 
print(candidate_votes)

# Print Candidate list 
print(candidate_options)

   # Print the total votes
    print(total_votes)


#Using the open() function with the "w" mode we will write data to file 
open(file_to_save,"w")

#Create a filename variable to a direct or indirect path to the file 
file_to_save = os.path.join ("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file 
with open(file_to_save,"w") as txt_file:

    #Write some data to the file 
    #txt_file.write("Hello world")
    txt_file.write("Counties in the Election")

    # Write three counties to the file 
    txt_file.write("\nArapahoe\nDenver\nJefferson")
   



