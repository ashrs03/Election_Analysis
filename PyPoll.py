
# Add our dependencies
import csv
import os

# Assign a variable for the file to loan and the path
file_to_load= os.path.join("Resources", "election_results.csv")

#Create a filename variable to a direct or indirect path to the file 
file_to_save = os.path.join("analysis","election_analysis.txt")

# 1 Initialize a total vote counter
total_votes = 0

# Candidate options 
candidate_options = []

# Declare empty dictionary 
candidate_votes = {}

 # Winning Candidates and winning count tracker 
winning_candidate = ""
winning_count = 0
winning_percentage = 0

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

# Save thw results to text file
with open(file_to_save,"w") as txt_file:

    # Print the final vote count to the terminal 
    election_results =( 
        f"\nElection_Results\n"
        f"----------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------------\n")
    print(election_results, end="")

    #Save final vote count to text file 
    txt_file.write(election_results)
    
    # Determine the percentage of votes for each candidate by looping through the counts
    #1. Iterate through the candidate list 
    for candidate_name in candidate_votes:
        
        #2 Retrieve vote count of a candidate 
        votes = candidate_votes[candidate_name]
        
        #3 Calculate the percentage of votes
        vote_percentage = float(votes) /float(total_votes)* 100
        
        #4 Print the candidate name and percentage of votes
        candidate_results= (f"{candidate_name}: {vote_percentage:,.1f}% ({votes:,})\n")
        print (candidate_results)

        # Save candidate_results to text file
        txt_file.write(candidate_results)

        # Determine winning vote count, percentage and candidate 
        if (votes> winning_count) and (vote_percentage > winning_percentage):
            # If true set winning_count = votes and winning_percent = 
            # vote_percentage 
            winning_count = votes
            winning_percentage = vote_percentage

            # And, set the winning_candidate equal to the candidate's name 
            winning_candidate = candidate_name

    # Print winning candidate results to terminal 
    winning_candidate_summary = (
        f"-----------------------------\n"
        f"Winner : {winning_candidate}\n"
        f"Winning Vote Count : {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}% \n"
        f"-----------------------------\n")

    print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary)

    #Print candidate vote dictionary 
    #print(candidate_votes)

    # Print Candidate list 
    #print(candidate_options)

    # Print the total votes
    #print(total_votes)

  




    



