# Find the winner of the election based on popular vote
# print out the election results to the terminal
# Print candidate total votes number
# Print candidate percentage of total votes as a percentatge to 3 decimal places
# Print out the winner
# Worked with Tutor Mark Fullton on both projects

#  Import the necessary dependencies for os.path.join()
import os
import csv

# create a csv file to read data into and a csv file to push the results out to
election_csv = os.path.join("Resources", "election_data.csv")
result_txt = os.path.join("Analysis", "result.txt")

# identify the columns that will be read in
# print (election_csv)

# Set total votes counter to start at zero for the total number of votes cast
total_votes = 0
# Create a dictionary for candidate votes
CandidateVotes = {}

# Read the csv file in. Read into a dictionary 'CandidateVotes'
with open(election_csv, 'r', newline="") as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        total_votes += 1
        curr_candidate=row[2] 
        if curr_candidate not in CandidateVotes:
            CandidateVotes[curr_candidate]=0
        CandidateVotes[curr_candidate]+=1

# Count up the total number of votes cast in the election  and the total of votes per candidate
# Python += operator adds two values together and assigns the final value to a variable
# print (total_votes) and print (CandidateVotes)

Win_vote=0
VotePercent=0
Win_name=""
with open(result_txt, "w", encoding='utf-8', newline="") as writefile: 
    print("Election Results")
    print("------------------------------------------------")
    writefile.write("Election Results\n")
    writefile.write("------------------------------------------------\n")
    print(f"Total Votes: {total_votes:,}")
    print("------------------------------------------------")
    writefile.write(f"Total Votes: {total_votes:,}\n")
    writefile.write("------------------------------------------------\n")
    for key, value in CandidateVotes.items():
        VotePercent=(value/total_votes)*100
    
        print (f"{key}: {VotePercent:.3f}% ({value:,})")
        writefile.write(f"{key}: {VotePercent:.3f}% ({value:,})\n")
        if value>Win_vote:
            Win_vote=value
            Win_name=key
    
    print("------------------------------------------------")
    print(f"Winner: {Win_name} with {Win_vote:,} votes")
    print("------------------------------------------------")
    writefile.write("------------------------------------------------\n")
    writefile.write(f"Winner: {Win_name} with {Win_vote:,} votes\n")
    writefile.write("------------------------------------------------")

# :, puts commas in numbers to show hundreds
#.3f puts 3 decimal places
# items() method is used to return the list with all dictionary keys with values.
# Syntax: dictionary.items() Returns: A view object that displays a list of a given dictionary’s (key, value) tuple pair.
# A complete list of candidates who received votes
# if the candidate is in the dictionary, then add 1. else, create initial entry for candidate
# get() method is used in Python to retrieve a value from a dictionary, 
# returns the value for the given key, if present in the dictionary
# != checks if the value of two operands are equal, if values are not equal than the condition becomes true.
# does Data in csv file need splitting?
# x.split(“,”) – the comma is used as a separator. This will split the string into a string array when it finds a comma
# The total number of votes each candidate won
# The percentage of votes each candidate won
# ???Use a dictionary to calculate candidate percentages
# Find the winner of the election based on popular vote
# print out the election results to the terminal
# Print candidate total votes number
# Print candidate percentage of total votes as a percentatge to 3 decimal places
# Print out the winner
# print("Election Results")
# print("-------------------------")
# output the election results lines above to a text file with same headers and formatting
# https://realpython.com/python-csv/#writing-csv-files-with-csv
# with open(result_csv, "w", newline="") as writefile:
#     writer = csv.writer(writefile)
#     writer.writerow(
