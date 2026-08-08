from datetime import date

print("===== Birthday Countdown =====")

day = int(input("Enter your birth day (1-31): "))
month = int(input("Enter your birth month (1-12): "))
year = int(input("Enter your birth year: "))

today = date.today()
birth_date = date(year, month, day)

# Total days lived
days_lived = (today - birth_date).days

# Current age
age = today.year - year
if (today.month, today.day) < (month, day):
    age -= 1

# Next birthday
next_birthday = date(today.year, month, day)

if next_birthday < today:
    next_birthday = date(today.year + 1, month, day)

days_left = (next_birthday - today).days

print("\n===== Birthday Report =====")

print(f"Birth Date          : {birth_date}")
print(f"Current Age         : {age} years")
print(f"Days Lived on Earth : {days_lived} days")

if days_left == 0:
    print("🎉 Happy Birthday!")
else:
    print(f"Next Birthday       : {next_birthday}")
    print(f"Days Remaining      : {days_left} days")