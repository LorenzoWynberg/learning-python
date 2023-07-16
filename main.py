days_in_a_year = 365
hours_in_a_day = 24
minutes_in_an_hour = 60
run = True
prompt = """
Enter number of days you'd 
like to translate into minutes 
or enter 'x' to exit: \n
"""

def days_to_minutes(days):
    return days * hours_in_a_day * minutes_in_an_hour

while run:
    user_input = input(prompt)
    if user_input == "x":
        run = False
        continue
        
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
else:
    print("\nExiting...\nEnjoy your day!")