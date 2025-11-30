from datetime import datetime


def is_date_in_range(
    target_date_str, start_date_str, end_date_str, date_format="%Y-%m-%d"
):
    """
    Checks if a target date string is between a start and end date string (inclusive).

    The date strings must be in the specified date_format (default is YYYY-mm-dd).
    """
    try:
        # Convert the string dates to datetime.date objects
        target_date = datetime.strptime(target_date_str, date_format).date()
        start_date = datetime.strptime(start_date_str, date_format).date()
        end_date = datetime.strptime(end_date_str, date_format).date()

        # Check if the target date is greater than or equal to the start date
        # AND less than or equal to the end date.
        return start_date <= target_date <= end_date

    except ValueError:
        # Handle cases where the date format is incorrect
        print("Error: One or more date strings are in an incorrect format.")
        return False


# --- Example Usage ---
target_date = "2023-10-15"
start_date = "2023-10-01"
end_date = "2023-10-31"

print(
    f"Is {target_date} in the range [{start_date} to {end_date}]? \
{is_date_in_range(target_date, start_date, end_date)}"
)

target_date_out = "2023-11-01"
print(
    f"Is {target_date_out} in the range [{start_date} to {end_date}]? \
{is_date_in_range(target_date_out, start_date, end_date)}"
)
