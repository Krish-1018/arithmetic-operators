#take number of days and find how many years , months and days can be possible

a = int(input("enter number of days"))
#for years
years = int(a/365)
print(years)

#for months
rem = a - years*365     #a%365
months = int(rem/30)
print(months)

#for remaining days
days = rem - months*30  #rem%30
print(days)