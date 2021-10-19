# Authour: SCT (ADMG) 10/19/21
year = int(input("Enter the year of the date:\n"))

month = int(input("Enter the month of the date:\n"))
if month <= 1:
    month = int(13)
elif month <= 2:
    month = int(14)

day = int(input("Enter the day of the date:\n"))

day_week = ((day) + (26 * (month + 1)) // (10) + (year % 100) + ((year % 100) // 4) + ((year // 100) // (4)) + (5 * (year // 100))) % 7
if day_week <= 0:
    day_week = str("Saturday")
elif day_week <= 1:
    day_week = str("Sunday")
elif day_week <= 2:
    day_week = str("Monday")
elif day_week <= 3:
    day_week = str("Tuesday")
elif day_week <= 4:
    day_week = str("Wednesday")
elif day_week <= 5:
    day_week = str("Thursday")
elif day_week <= 6:
    day_week = str("Friday")

print(str(month) + "/" + str(day) + "/" + str(year) + " was a " + day_week + ".")
