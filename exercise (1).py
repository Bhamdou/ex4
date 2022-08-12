# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn
from asyncio import Task
## Task 1
counter = 1
while counter <= 3:
    first_number = int(input("Enter a number:"))
    second_number = int(input("Enter another number:"))
    high_number = False

    if first_number >= 10000 and second_number >= 10000:
       high_number = True 
       print("Both numbers are big")
    if first_number != second_number:
       print("Numbers are not equal!")

    if second_number >= first_number:
       print("Second number is greater than or equal to first number") 
    if second_number > first_number:
       print("Second number is greater than first number") 
    if first_number >= second_number:
       print("First number is greater than or equal to second number")
    if first_number > second_number:
       print("First number is greater than second number") 
    if first_number %2 == 0:
       print("First Number is equal") 
    if second_number %2 == 0:
       print("Second Number is equal") 
    if first_number %2 != 0:
        print("1. Number is odd")
    if first_number %2 != 0:
          print("2. Number is odd")
          
          counter +=1
          if high_number == True:
              print("Variable High Number is true")
 



























#Task2
months_31 = [
    "January",
    "March",
    "May",
    "July",
    "August",
    "October",
    "December",]
months_30 = [
    "February",
    "April",
    "June",
    "September",
    "November",]

months_28 = [
    "February"]

user_month = input("please choose a month").capitalize()
if user_month in months_28:
    print(f"{user_month} has 28 days")
elif user_month in months_31 is True:
    print(f"{user_month} has 31 days")
elif user_month in months_30:
    print(f"{user_month} has 30 days")
