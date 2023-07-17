DAYS_IN_A_YEAR = 365
HOURS_IN_A_DAY = 24
MINUTES_IN_AN_HOUR = 60
PROMPT_WELCOME = "Welcome to the Days to Minutes Converter!\n"
PROMPT_EXIT = "\nExiting...\nEnjoy your day!\n"
PROMPT_NUM_DAYS = "Enter number of days \nyou'd like to convert \nor enter x to exit: \n\n"
PROMPT_UNIT_NAME = "\nWhat would you like \nto convert to? \n\nType:\n    1 for minutes, \n    2 for hours, \n    3 for months, \n    4 for years or \n    x to exit: \n\n"

def days_to_years(days):
    return days / DAYS_IN_A_YEAR

def days_to_months(days):
    return days_to_years(days) * 12

def days_to_hours(days):
    return days * HOURS_IN_A_DAY

def days_to_minutes(days):
    return days * HOURS_IN_A_DAY * MINUTES_IN_AN_HOUR

def get_valid_days_input():
    while True:
        user_input = input(PROMPT_NUM_DAYS)

        if user_input == "x" or user_input == "X":
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

        if user_input == "x" or user_input == "X":
            return None

        try:
            user_input = int(user_input)
        except ValueError:
            print("\nError: Please enter a numeric value\n")
            continue

        match user_input:
            case 1:
                return "minutes"
            case 2:
                return "hours"
            case 3:
                return "months"
            case 4:
                return "years"
            case "x":
                return None
            case "X":
                return None
            case _:
                print("\nError: Please enter a valid unit\n")

def get_unit_amount(days, unit_name):
    match unit_name:
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
