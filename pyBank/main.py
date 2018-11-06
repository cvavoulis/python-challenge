import os
import csv
import pandas as pd
import numpy as np

csvpath=("budget_data.csv")

budget_df=pd.read_csv(csvpath)
budget_df.head()

total_months=budget_df["Date"].count()
sum_p_l=budget_df["Profit/Losses"].sum()

AmtChange = budget_df["Profit/Losses"].diff()
budget_df["Amount Changed"] = AmtChange

sum_change=budget_df["Amount Changed"].sum()
sum_months=total_months-1
avg_change=sum_change/sum_months
budget_df.head()

greatest_increase=budget_df["Amount Changed"].max()

greatest_decrease=budget_df["Amount Changed"].min()

greatest_dec_month=budget_df.loc[budget_df["Amount Changed"]==greatest_decrease,["Date"]]
great_dec=greatest_dec_month["Date"].values[0]

greatest_inc_month=budget_df.loc[budget_df["Amount Changed"]==greatest_increase,["Date"]]
great_inc=greatest_inc_month["Date"].values[0]

output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${sum_p_l}\n"
    f"Average  Change: ${avg_change}\n"
    f"Greatest Increase in Profits: {great_inc} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {great_dec} (${greatest_decrease})\n")

print(output)    