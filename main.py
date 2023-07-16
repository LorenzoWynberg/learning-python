days_in_a_year = 365
hours_in_a_day = 24
minutes_in_an_hour = 60

prompt = "Enter number of days you'd \nlike to translate into minutes \nor enter 'x' to exit: \n"

def days_to_minutes(days):
    return days * hours_in_a_day * minutes_in_an_hour

while True:
    user_input = input(prompt)

    if user_input == "x":
        print("\nExiting...\nEnjoy your day!")
        break

    try:
        days = int(user_input)
    except ValueError:
        print("\nError: Please enter a numeric value")
        continue

    if days <= 0:
        print("\nError: Please enter a number greater than 0")
    else:
        minutes = days_to_minutes(days)
        print("\n-----------------------------------------------")
        print(f"There are {minutes} minutes in {days} days")
        print("-----------------------------------------------")