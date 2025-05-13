#def read_integer():
#    while True:
#        try:
#            input_str = input("Please type in an integer: ")
#            return int(input_str)
#        except ValueError:
#            print("This input is invalid")
import string
#number = read_integer()
#print("Thank you!")
#print(number, "to the power of three is", number**3)

#def read_Array(x):
#    list_dizi =[]
#    for i in range(x):
#        while True:
#            try:
#                input_str =input(f"Please {i+1}th type item as integer:")
#                if int(input_str) not in list_dizi:
#                    list_dizi.append(int(input_str))
#                    break
#                else:
#                    print("You can not enter the same integer")
#            except ValueError:
#                print("This value is invalid")

#    return list_dizi

#array1 = read_Array(3)
#print(array1)
#from random import randint
#def lottery_numbers(amount: int,lower: int,upper: int):
#    numbers_list=[]
#    for i in range(amount):
#        new_rnd =randint(lower,upper)
#        if new_rnd not in numbers_list:
#            numbers_list.append(new_rnd)

#    numbers_list.sort()
#    return numbers_list


#for number in lottery_numbers(100,0,100):
#    print(number)
#import random
#import string

#def password(length: int):
#    password= ''
#    for i in range(length):
#        password +=chr(random.randint(97,122))
#    return password

#for i in range(10):
#    print(password(8))

from datetime import datetime
def date_time():
    day = int(input("Please enter day number: "))
    month = int(input("Please enter month number: "))
    year = int(input("Please enter year number: "))
    my_time = datetime(year, month, day)
    time_now = datetime.today()
    if my_time > time_now:

        return  print("You are not born yet")

    howoldinday = time_now - my_time
    return print(f"You were{howoldinday} days old on the eve of the new millenium")

date_time()