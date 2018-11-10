import pandas as pd
import numpy as np

csvfile="election_data.csv"
election_data=pd.read_csv(csvfile)

election_data.head()

total_votes=election_data["Voter ID"].count()

total_votes_each=election_data.groupby("Candidate").count()
df_new=total_votes_each.rename(columns={"Voter ID": "Total_Votes"}).drop(columns=["County"])
df_new["Percentage"]=(df_new["Total_Votes"]/total_votes)*100
df_sorted=df_new.sort_values(["Total_Votes"], ascending=False).reset_index().round()
df_sorted.head()

output = (
    f"\nElection Results\n"
    f"----------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"----------------------------\n"
    f"{df_sorted.Candidate[0]}: {df_sorted.Percentage[0]}% ({df_sorted.Total_Votes[0]})\n"
    f"{df_sorted.Candidate[1]}: {df_sorted.Percentage[1]}% ({df_sorted.Total_Votes[1]})\n"
    f"{df_sorted.Candidate[2]}: {df_sorted.Percentage[2]}% ({df_sorted.Total_Votes[2]})\n"
    f"{df_sorted.Candidate[3]}: {df_sorted.Percentage[3]}% ({df_sorted.Total_Votes[3]})\n"
    f"----------------------------\n"
    f"Winner: {df_sorted.Candidate[0]}")

print(output)

