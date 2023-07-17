DAYS_IN_A_YEAR = 365
DAYS_IN_MONTH = 30
HOURS_IN_A_DAY = 24
MINUTES_IN_AN_HOUR = 60
SECONDS_IN_A_MINUTE = 60
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
        user_input = input(PROMPT_UNIT_NAME)
        user_input = user_input.lower()

        match user_input:
            case 'secs':
                return "seconds"
            case 'mins':
                return "minutes"
            case 'hrs':
                return "hours"
            case 'mos':
                return "months"
            case 'yrs':
                return "years"
            case 'x':
                return None
            case _:
                print("\nError: Please enter a valid unit\n")

def get_unit_amount(days, unit_name):
    match unit_name:
        case "seconds":
            return days_to_seconds(days)
        case "minutes":
            return days_to_minutes(days)
        case "hours":
            return days_to_hours(days)
        case "months":
            return days_to_months(days)
        case "years":
            return days_to_years(days)
        case _:
            return None

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

        print("\n-----------------------------------------------")
        if unit_amount == 1:
            print(f"{days} days make a {unit_name[:-1]}")
        elif unit_amount > 1:
            unit_amount = round(unit_amount, 2)
            print(f"{days} days are {unit_amount} {unit_name}")
        else:
            unit_amount = unit_amount * 100
            unit_amount = round(unit_amount, 2)
            print(f"{days} days are {unit_amount}% of a {unit_name[:-1]}")
        print("-----------------------------------------------\n")

if __name__ == "__main__":
    main()
