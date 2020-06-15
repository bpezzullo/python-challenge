import csv

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
