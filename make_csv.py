import random

# Столбцы на чистом английском
columns = ["id", "date", "category", "item", "amount_rub", "payment_method"]

# Все данные переводим на английский
categories_items = {
    "Food": ["Supermarket", "Grocery Store", "Food Delivery", "Cafe"],
    "Transport": ["Bus/Metro", "Taxi", "Train Ticket"],
    "Gaming & Subs": ["Steam", "In-game Donate", "Music Streaming", "Premium Subs"],
    "Clothes": ["Sneakers", "Hoodie", "T-Shirt", "Backpack"],
    "Entertainment": ["Cinema", "Concert Ticket", "Board Game", "Fast Food"]
}

payment_methods = ["T-Bank", "Sber", "SBP", "Cash"]

rows = []
for i in range(1, 201):
    date = f"2026-06-{random.randint(1, 30):02d}"
    cat = random.choice(list(categories_items.keys()))
    item = random.choice(categories_items[cat])
    
    if cat == "Food":
        amount = random.randint(150, 2500)
    elif cat == "Transport":
        amount = random.randint(50, 800)
    elif cat == "Gaming & Subs":
        amount = random.randint(299, 1999)
    elif cat == "Clothes":
        amount = random.randint(1200, 8000)
    else:
        amount = random.randint(300, 3000)
        
    pay = random.choice(payment_methods)
    rows.append(f"{i},{date},{cat},{item},{amount},{pay}")

with open("data.csv", "w") as f:
    f.write(",".join(columns) + "\n")
    for row in rows:
        f.write(row + "\n")

print("Success! 'personal_expenses.csv' with 200 rows generated in English.")
