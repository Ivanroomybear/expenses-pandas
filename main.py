import pandas as pd
df = pd.read_csv("data.csv")

# Task #1: Find the total amount spent on 'Gaming & Subs' using 'SBP'
gis_sum = df[(df['category'] == "Gaming & Subs") & (df['payment_method'] == "SBP")]
print(gis_sum['amount_rub'].sum())

# Task #2: Find the most expensive item purchased in the 'Clothes' category
clothes_pr = df[df['category'] == "Clothes"]
clothes_me = clothes_pr.loc[clothes_pr['amount_rub'].idxmax()]
print(clothes_me[['item', 'amount_rub']])

# Task #3: Calculate the total sum (amount_rub) spent on the Food category where the payment_method was strictly Cash
ctc_sum = df[(df['category'] == "Food") & (df['payment_method'] == "Cash")]
sum1 = ctc_sum['amount_rub'].sum()
print(sum1)

# Task #4: Find the item name that appears the highest number of times in the dataset.
print(df['item'].value_counts().idxmax())

# Task #5: Calculate the average transaction value (amount_rub) for each unique category and return the category name with the highest average value.
print(df.groupby('category')['amount_rub'].mean().idxmax())

# Task #6: Convert the date column to datetime. Group the data by the day of the week (Monday, Tuesday, etc.). Find the day of the week with the highest average transaction volume (amount_rub) and the day with the highest total transactions count.
df['date'] = pd.to_datetime(df['date'])
df['weekday'] = df['date'].dt.day_name()
transactions_count = df.groupby('weekday').size()
print(transactions_count.idxmax())
