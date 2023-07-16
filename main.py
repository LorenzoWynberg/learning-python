days_in_a_year = 365
hours_in_a_day = 24
minutes_in_an_hour = 60

def days_to_minutes(days):
    return days * hours_in_a_day * minutes_in_an_hour

user_input = input("Enter number of days you'd like to translate into minutes: \n")
days = int(user_input)
minutes = days_to_minutes(days)
res = f"There are {minutes} minutes in {days} days"

print(res)