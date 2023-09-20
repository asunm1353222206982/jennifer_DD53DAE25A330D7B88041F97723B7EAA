year=int(input("Enter your year:"))
if(year%400==0):
  print("%d is leap year" %year)
elif(year%100==0):
  print("%d is not leap year" %year)
elif(year%4==0):
  print("%d is leap year" %year)
else:
  print("%d is not leap year" %year)