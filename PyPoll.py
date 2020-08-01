#dependencies
import os
import csv


#retrieve data
file_to_load = os.path.join('Resource', 'election_results.csv')

file_to_save = os.path.join("analysis", "election_analysis.txt")

#A)Total number of votes cast
#A1) initilize vote counter
total_votes = 0

#B) Complete list of candidates who received votes
#B1) Candidate Options
candidate_options = []

#C) Total number of votes each candidate received
#C1) declare an empty dictionar
candidate_votes = {}

#E) The winner of the election based on popular vote
#E1) Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# setup) open election results
with open(file_to_load) as election_data:

#setup) read the csv
    file_reader = csv.reader(election_data)

    #setup) read+print header row
    headers = next(file_reader)

    for row in file_reader:
        #A2) add vote count
        total_votes += 1

        #B2) print the candidate name from each row
        candidate_name = row[2]
        
        #B3) if the cadidate doe not match and existing candadit
        if candidate_name not in candidate_options:
            #B4) add the candidate name to candidate list
            candidate_options.append(candidate_name)
            #C2) begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        #C3) add vote to candadit's count
        candidate_votes[candidate_name] += 1

        #F)save to text file
        #F1) open text file
with open(file_to_save,"w") as txt_file:
    #F2) Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    #F3) Save the final vote count to the text file.
    txt_file.write(election_results)
    
    #D) Percentage of votes each candidate won
    #D1) iterate through candidate list
    for candidate_name in candidate_votes:
        #D2) retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        #D3) clac the % vote
        vote_percentage = float(votes) / float(total_votes) * 100
        #E4) get candidate results out name, vote count, and %
        candidate_results = (f"{candidate_name}: {round(vote_percentage,1)}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)


        #E1) determine if the votes are greater the the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #E2) If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            #E3) Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
    
       
    
    #E5) print summery
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)





#A3) print total votes
#print(total_votes)

#B5) print the candidate list
#print(candidate_options)

#C4) print the candidate vote dictioary
#print(candidate_votes)

 #D4) print candidate name and % votes
#print(f"{candidate_name}: received {round(vote_percentage, 1)}% of the vote.")