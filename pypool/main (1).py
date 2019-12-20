#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Pypool home work 


import csv
import os

file_to_load = os.path.join("election_data.csv")
file_to_output = os.path.join("election_analysis.txt")


total_votes = 0
candidate_options = [ ]
candidate_votes = { }


winning_candidate = ""
winning_count = 0

    
    
with open(file_to_load) as election_data:
    
    reader = csv.reader(election_data)
    header = next(reader) 
    for row in reader:
        
        print(". ", end=" ")


    total_votes = total_votes + 1
    candidate_name = row[2]

if candidate_name not in candidate_options: 
    candidate_options.append(candidate_name)
    candidate_votes[candidate_name] = 0
    candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1 
    
    with open(file_to_output, "W") as txt_file:
        
        election_results = (
        "\n\nElection Resulting\n" + 
        "--------------------\n"+
        "Total Votes: " + str(total_votes) + "\n"+
        "-------------------\n")
        #print(election_results, end = " ")
        
        txt_file.write(election_results)
        for candidate in candidate_votes: 
            votes = candidate_votes.get(candidate)
            vote_percentage = float(votes) / float(total_votes) * 100
            if(votes > winning_count): 
                winning_count = votes
                winning_candidate = candidate
                
                voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
                
                print(voter_outage, end="")
                txt_file.writer(voter_output)
                
                #print the_winning_candidates 
                winning_candidate_summary = (
                    f"-----------\n"
                    f"Winner: {wining_candidate}\n"
                    f"------------------\n")
                #print(winning_candidate_summary)
                #Save hte winning candidate name to the text file
                txt_file.writer(Winning_candiate_summerty)
                
                  


# In[ ]:





# In[ ]:




