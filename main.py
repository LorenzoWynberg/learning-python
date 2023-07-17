DAYS_IN_A_YEAR = 365
HOURS_IN_A_DAY = 24
MINUTES_IN_AN_HOUR = 60
PROMPT = "Enter number of days you'd \nlike to translate into minutes \nor enter 'x' to exit: \n\n"

def days_to_minutes(days):
    return days * HOURS_IN_A_DAY * MINUTES_IN_AN_HOUR

def get_valid_days_input():
    while True:
        user_input = input(PROMPT)

        if user_input == "x":
            return None

        try:
            days = int(user_input)
            if days <= 0:
                print("\nError: Please enter a number greater than 0\n")
            else:
                return days
        except ValueError:
            print("\nError: Please enter a numeric value\n")

def main():
    while True:
        days = get_valid_days_input()
        if days is None:
            print("\nExiting...\nEnjoy your day!")
            break
        else:
            minutes = days_to_minutes(days)
            print("\n-----------------------------------------------")
            print(f"There are {minutes} minutes in {days} days")
            print("-----------------------------------------------\n")
if __name__ == "__main__":
    main()