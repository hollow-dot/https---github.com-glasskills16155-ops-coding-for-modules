from datetime import date

date_user = input()
splitting = date_user.split("-")
print(splitting)
year = int(splitting[0])
month = int(splitting[1])
day = int(splitting[2])


try:
  date(year, month, day)
except ValueError:
    print("invalid date")
else:
    print("valid date")
  