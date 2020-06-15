import csv

# In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.
#
# You will be give a set of poll data called election_data.csv. The dataset found in the folder 'Resources' is 
# composed of three columns: Voter ID, County, and Candidate. 
# 
# This Python script analyzes the votes and calculates each of the following:
#
# The total number of votes cast
#
# A complete list of candidates who received votes
#
#  - The percentage of votes each candidate won
#  - The total number of votes each candidate won
#  - The winner of the election based on popular vote.
#
#
# As an example, your analysis should look similar to the one below:
#
# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------

#
# In addition, your final script should both print the analysis to the terminal and export a text file 'results'
# found in the folder 'analsis' with the results.

with open("Resources/election_data.csv") as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')

    # initialize the variables to 0 or empty for the lists
    Candidates = []
    Candidate_count = []
    Candidate_percent = []


    # Strip off the header
    header = next(csv_reader)

    for row in csv_reader:

        # For each row check to see if the candidate is in the list.  If the candidate
        # is not in the list than a ValueError is thrown.  Chck to see if that happens 
        # when you try to find the candidate name in the list Candidates.  If not found 
        # then append the name and start the count at 1.  If found than increase the
        # count by 1.
            try:
                next_vote = Candidates.index(row[2])     # is the candidate in the list?
            except(ValueError):
                next_vote = -1                          # no then set the next_vote
                                                        # variable to -1
            # if next_vote is -1 than this is a new candidate. Save the name by appending
            # to the list and start the count as 1 as someone voted for them
            if next_vote == -1:                         
                Candidates.append(row[2])
                Candidate_count.append(1)
            # else increment the count at the index
            else:                                   
                Candidate_count[next_vote] += 1

    # get the number of votes
    total_votes = sum(Candidate_count)

    # set the index counter to 0
    Index_counter = 0

    # Calculate the percentage
    for cand in Candidate_count:

        Candidate_percent.append(round(int(cand)/total_votes * 100,4))
    
    # close the csv file
    csv_file.close 

# find the index of the max count.  This will be used to print out the Candidate
winner = Candidate_count.index(max(Candidate_count))

# format the results     
cand_formated = zip(Candidates,Candidate_percent, Candidate_count)

# write the information to the file 'results'in the folder 'a'nalysis'
f = open("analysis/results","w",newline='\n')
f.write("Election results \n")
f.write("------------------------------- \n")
f.write("Total Votes: " + str(total_votes) + "\n")
f.write("------------------------------- \n")

# Print out the list of candidates
for cand_list in cand_formated:
    
    f.write(cand_list[0] + ": " + str(cand_list[1]) + "% (" + str(cand_list[2]) + ")\n")

f.write("-------------------------------\n")
f.write("Winner: " + Candidates[winner] + "\n")

f.write("-------------------------------\n")
# close the file and then use the file to display the results to the sreen
f.close

# Print the file
f = open("analysis/results","r")
file_contents = f.read()
print (file_contents)
    
f.close
