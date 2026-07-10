import pandas as pd
df = pd.read_csv("data.csv")

# Task #1: Find the total amount spent on 'Gaming & Subs' using 'SBP'
gis_sum = df[(df['category'] == "Gaming & Subs") & (df['payment_method'] == "SBP")]
print(gis_sum['amount_rub'].sum())

# Task #2: Find the most expensive item purchased in the 'Clothes' category
clothes_pr = df[df['category'] == "Clothes"]
clothes_me = clothes_pr.loc[clothes_pr['amount_rub'].idxmax()]
print(clothes_me[['item', 'amount_rub']])