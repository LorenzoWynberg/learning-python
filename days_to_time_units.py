DAYS_IN_A_YEAR = 365
DAYS_IN_MONTH = 30
HOURS_IN_A_DAY = 24
MINUTES_IN_AN_HOUR = 60
SECONDS_IN_A_MINUTE = 60
UNIT_NAME_MAPPINGS = {
    'secs': 'seconds',
    'mins': 'minutes',
    'hrs': 'hours',
    'mos': 'months',
    'yrs': 'years'
}
PROMPT_WELCOME = "Welcome to the Days to Time Unit Converter!\n"
PROMPT_EXIT = """
Exiting...
Enjoy your day!

"""
PROMPT_NUM_DAYS = """
Enter number of days
you'd like to convert
or enter x to exit:

"""
PROMPT_UNIT_NAME = """
What would you like
to convert to?

Type:
    secs for seconds,
    mins for minutes,
    hrs for hours,
    mos for months,
    yrs for years or
    x to exit:

"""

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
        user_input = input(PROMPT_UNIT_NAME).lower()

        if user_input == 'x':
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

def get_unit_amount(days, unit_name):
    conversion_function = UNIT_CONVERSIONS.get(unit_name)
    if conversion_function:
        return conversion_function(days)

def main():
    while True:
        days = get_valid_days_input()
        if days is None :
            print(PROMPT_EXIT)
            break

        unit_name = get_valid_unit_input()
        if unit_name is None:
            print(PROMPT_EXIT)
            break

        unit_amount = get_unit_amount(days, unit_name)
        if unit_amount is None:
            print(PROMPT_EXIT)
            break

        result = f"{days} days "

        if unit_amount == 1:
            result += f"make a {unit_name[:-1]}"
        elif unit_amount > 1:
            unit_amount = round(unit_amount, 2)
            result += f"are {unit_amount} {unit_name}"
        else:
            unit_amount = unit_amount * 100
            unit_amount = round(unit_amount, 2)
            result += f"are {unit_amount}% of a {unit_name[:-1]}"

        print("\n-----------------------------------------------")
        print(result)
        print("-----------------------------------------------\n")

if __name__ == "__main__":
    main()
