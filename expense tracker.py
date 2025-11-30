"""
[x] show total by category (list all categories)
[ ] search
[ ] refactor
"""

import csv
import datetime


# -------------------- loading and writing ------------------------------------------------
def load_data():
    with open("data.csv", "r") as file:
        csv_reader = csv.reader(file)
        data = [row for row in csv_reader]
    return data


def write_data(data):
    with open("data.csv", "w") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data)


# -------------------- main functions -----------------------------------------------------
def add_expense(data):
    amount = input("Enter the amount: ")
    category = input("Enter the category: ")
    note = input("Enter a note: ")
    date = input("Enter the date (YYYY-mm-dd) (Press enter for today): ")
    time = input("Enter the time (HH:MM) (Press enter for now): ")

    if not date:
        date = datetime.datetime.now().strftime("%Y-%m-%d")
    if not time:
        time = datetime.datetime.now().strftime("%H:%M")

    data.append([amount, category, note, date, time])

    return data


def view_expenses(data):
    if not data:
        print("No expenses found! Add some!")
        return

    for row in data:
        print(f"{row[3]} {row[4]} {row[0]} {row[1]} {row[2]}")


# -------------------- Filter functions --------------------------------------------------
def filter_by_date(data):
    index = 3
    date = input("Enter the date (Press enter for today): ")

    if not date:
        date = datetime.datetime.now().strftime("%Y-%m-%d")

    filtered_list = []
    for row in data:
        if row[index] == date:
            filtered_list.append(row)

    return filtered_list


def filter_by_category(data):
    total = {}
    for row in data:
        if row[1] in total:
            total[row[1]] += float(row[0])
        else:
            total[row[1]] = float(row[0])

    for i in total:
        print(f"{i}: {total[i]}")


# -------------------- search functions -------------------------------------------------


def search(data):
    print(
        "Chose what to search by:",
        "[1] Category",
        "[2] Date",
        "[3] Date range",
        "[4] Keyword in a note",
        sep="\n",
    )
    user_input = input(">>> ")

    filtered_list = []
    if user_input == "1":
        category = input("Enter the category: ")
        for row in data:
            if row[1] == category:
                filtered_list.append(row)

    elif user_input == "2":
        date = input("Enter the date (YYYY-mm-dd): ")
        for row in data:
            if row[3] == date:
                filtered_list.append(row)

    elif user_input == "3":
        start_date = input("Enter the start data: ")
        end_date = input("Enter the end date")

    elif user_input == "4":
        keyword = input("Enter the keyword: ")
        for row in data:
            if keyword in row[2]:
                filtered_list.append(row)

    return filtered_list


# -------------------- other ------------------------------------------------------------


def sum_expenses(data):
    total = 0.0
    amount_index = 0
    for row in data:
        total += float(row[amount_index])
    return total


data = load_data()

while True:
    print(
        "[1] Add expense",
        "[2] View all expenses",
        "[3] Show total spent by date",
        "[4] Show total spent by category",
        "[5] Search",
        sep="\n",
    )
    user_input = input(">>> ")

    if user_input == "1":
        data = add_expense(data)
        write_data(data)
    elif user_input == "2":
        view_expenses(data)
    elif user_input == "3":
        filtered_list = filter_by_date(data)
        total_spent = sum_expenses(filtered_list)
        print(f"Total spent: {total_spent}")
    elif user_input == "4":
        filter_by_category(data)
    elif user_input == "5":
        filtered_data = search(data)
        view_expenses(filtered_data)
