age = (input("What is your current age?\n"))
years = 90 - int(age)
days = int(years) * 365
weeks = int(days) // 7
months = (int(years) * 12)
print(f"You have {days} days, {weeks} weeks, and {months} months left. Use your time wisely.")