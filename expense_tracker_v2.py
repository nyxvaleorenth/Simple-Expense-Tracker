"""
 * continue till the end, no refactor, keep the shitty code
[x] add expenses
[x] view all expenses
[x] total spent today
    [x] and by date
[ ] total by category
[ ] search
    [ ] category
    [ ] date
    [ ] date range
    [ ] keyword in a note
[ ] statistics
    [ ] biggest expense
    [ ] smallest expense
    [ ] average spending
    [ ] most expensive category
[ ] dealing with invalid input
[ ] dealing with missing or corrupted files
--- extra ---
[ ] beautiful looking view all
"""

import csv
from datetime import datetime


def load_expenses():
    """load data from data.csv file"""
    with open("data.csv", "r", newline="") as file:
        csv_reader = csv.reader(file)
        data_list = list(csv_reader)
    return data_list


def save_expenses(data):
    """save data to data.csv file"""
    with open("data.csv", "w", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data)


def add_expense(data):
    """return updated data with adding new item to it"""
    try:
        amount = float(input("Enter the amount: "))
    except ValueError:
        print("Print enter a valid input!")
        return data

    category = input("Enter the category: ")
    note = input("Enter a note: ")

    date = input("Enter the date (YYYY-mm-dd) (Press enter for today): ")
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    data.append([amount, category, note, date])

    return data


def view_expenses(data):
    """views giving data"""
    for expense in data:
        print(f"[{expense[3]}] {expense[0]} {expense[1]} {expense[2]}")


def show_total_by_date(data):
    """returns the sum of amount by a specific date"""
    date = input("Enter the date (YYYY-mm-dd) (Press enter for today): ")
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    result = 0

    for expense in data:
        if expense[3] == date:
            result += float(expense[0])

    return result


def show_total_by_category(data):
    """prints each category and the sum of expenses of that category"""
    pass


# main code
data = load_expenses()


while True:
    print(
        "Chose what to do:",
        "[1] Add new expense",
        "[2] View all expenses",
        "[3] Show total by date",
        sep="\n",
    )
    user_input = input(">>> ")

    if user_input == "1":
        data = add_expense(data)
        save_expenses(data)
    elif user_input == "2":
        view_expenses(data)
    elif user_input == "3":
        print(show_total_by_date(data))
