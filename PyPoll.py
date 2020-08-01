#deoendencies
import os
import csv


#retrieve data
file_to_load = os.path.join('Resource', 'election_results.csv')

with open(file_to_load) as election_data:

    print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")


# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    # Write three counties to the file.
     txt_file.write("Counties in the Elections\n--------------------\nArapahoe\nDenver\nJefferson")





#Total number of votes cast
#A complete list of candidates who received votes
#Total number of votes each candidate received


#process data
#Percentage of votes each candidate won
#The winner of the election based on popular vote
