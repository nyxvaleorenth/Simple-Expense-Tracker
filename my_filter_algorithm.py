import datetime

data = [
    ["15", "food", "pizza", "2025-11-28", "8:52"],
    ["25", "transportation", "taxi", "2025-11-28", "14:12"],
    ["36", "entertainment", "cinema", "2025-11-27", "12:45"],
]

# get all entries with with day = today
today = datetime.datetime.now().strftime("%Y-%m-%d")
today_list = []
for row in data:
    if row[3] == today:
        today_list.append(row)

print(today_list)
