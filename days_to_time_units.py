from constants.data import *
from constants.prompts import *

def days_to_years(days):
    return days / DAYS_IN_A_YEAR

def days_to_months(days):
    return days / DAYS_IN_MONTH

def days_to_hours(days):
    return days * HOURS_IN_A_DAY

def days_to_minutes(days):
    return days_to_hours(days) * MINUTES_IN_AN_HOUR

def days_to_seconds(days):
    return days_to_minutes(days) * SECONDS_IN_A_MINUTE

def get_valid_days_input():
    while True:
        user_input = input(PROMPT_NUM_DAYS)

        if user_input.lower() == "x":
            return None

        try:
            days = int(user_input)
            if days <= 0:
                print("\nError: Please enter a number greater than 0\n")
            else:
                return days
        except ValueError:
            print("\nError: Please enter a numeric value\n")

def get_valid_unit_input():
    while True:
        user_input = input(PROMPT_UNIT_NAME)

        if user_input.lower() == 'x':
            return None

        unit_name = UNIT_NAME_MAPPINGS.get(user_input)
        if unit_name:
            return unit_name

        print("\nError: Please enter a valid unit\n")

UNIT_CONVERSIONS = {
    "seconds": days_to_seconds,
    "minutes": days_to_minutes,
    "hours": days_to_hours,
    "months": days_to_months,
    "years": days_to_years,
}

def convert_days_to_unit(days, unit_name):
    amount = UNIT_CONVERSIONS.get(unit_name)
    if amount:
        return amount(days)

def format_num(num):
    return "{:.2f}".format(num).rstrip('0').rstrip('.')

def collect_user_input():
    days = get_valid_days_input()
    if days is None:
        print(PROMPT_EXIT)
        return None

    unit_name = get_valid_unit_input()
    if unit_name is None:
        print(PROMPT_EXIT)
        return None

    return days, unit_name

def get_result(days, unit_name, unit_amount):
    result = f"{days} days "

    if unit_amount == 1:
        result += f"make a {unit_name[:-1]}"
    elif unit_amount > 1:
        unit_amount = format_num(unit_amount)
        result += f"are {unit_amount} {unit_name}"
    else:
        percentage = unit_amount * 100
        percentage = format_num(percentage)
        result += f"are {percentage}% of a {unit_name[:-1]}"

    return result

def print_result(result):
    print("\n-----------------------------------------------")
    print(result)
    print("-----------------------------------------------\n")

def main():
    while True:
        user_input = collect_user_input()
        if user_input is None:
            break
        days, unit_name = user_input

        unit_amount = convert_days_to_unit(days, unit_name)
        if unit_amount is None:
            print(PROMPT_EXIT)
            break

        result = get_result(days, unit_name, unit_amount)
        print_result(result)

if __name__ == "__main__":
    main()
