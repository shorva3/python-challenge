import os
import csv

candidate = []
u_c = []
candidate_vote = []
vote_percent = []
count = 0

election_csv = os.path.join("election_data.csv")
with open(election_csv, newline = "", encoding = "utf8") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csv_reader)
    for row in csv_reader:
        count = count + 1
        candidate.append(row[2])
    for i in set(candidate):
        u_c.append(i)
        c_count = candidate.count(i)
        candidate_vote.append(c_count)
        vote_percent.append(candidate.count(i) / count)
    winner = u_c[candidate_vote.index(max(candidate_vote))]


    
with open("Election_Results.txt", "w") as text:
    text.write("Election Results" + "\n")
    text.write("---------------------------" + "\n")
    text.write("Total Votes " + str(count) + "\n")
    text.write("---------------------------" + "\n")
    for z in range(len(set(candidate))):
        text.write(u_c[z] + ": " + str(round(vote_percent[z]*100,1)) + "% (" + str(candidate_vote[z]) + ")" + "\n")
    text.write("---------------------------" + "\n")
    text.write("Winner: " + winner + "\n")
    text.write("---------------------------" + "\n")
        

    print("Election Results")
    print("---------------------------")
    print("Total Votes " + str(count))
    print("---------------------------")
    for z in range(len(set(candidate))):
        print(u_c[z] + ": " + str(round(vote_percent[z]*100,1)) + "% (" + str(candidate_vote[z]) + ")")
    print("---------------------------")
    print("Winner: " + winner)
    print("---------------------------")  