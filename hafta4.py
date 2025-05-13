#while True:
#    number = int(input("Please type in a number: "))
#    if number == -1:
#        break
#    while number > 0:
#        print(number)
#        number -= 1
from array import array

#number = int(input("Please type in a number: "))
#while number > 0:
#    i = 0
#    while i < number:
#        print(f"{i} ", end="")
#        i += 1
#    print()
#    number -= 1

#st1 = input("Please enter a sentence:")
#sayac = 0
#print(st1[0])
#while sayac < len(st1):
#    if st1[sayac] == " ":
#        print(st1[sayac+1])
#    sayac+=1

#sayi1 = int(input("Please type in a number:"))
#sayac = 0
#while sayac < sayi1:
#    sayac += 1
#    if sayac == sayi1 and sayac % 2 ==1:
#        print(sayac)
#    elif sayac % 2 != 0:
#        print(sayac+1)
#    elif sayac % 2 == 0:
#        print(sayac-1)

#sayi1 = int(input("Please type in a number:"))
#sayac =1
#while sayac <= sayi1:
#    if sayac == sayi1:
#        print(sayi1)
#        break
#    print(sayac)
#    print(sayi1)
#    sayi1-=1
#    sayac+=1

#def hello(target):
#    print("Hello " + target)
#hello("reius")

#def first_character(text):
#    print(text[0])


#first_character('python')
#first_character('yellow')
#first_character('tomorrow')
#first_character('heliotrope')
#first_character('open')
#first_character('night')

#def print_many_times(string,target):

#    while target > 0:
#        print(string)
#        target -= 1

#print_many_times("ahmetine cakayım",31)

#def half_square(sayi):
#    i = sayi
#    while i > 0:
#        print("#"*sayi)
#        i-=1

#half_square(5)

#def half_square(sayi):
#    for i in range(sayi):
#        print("#"*sayi)

#half_square(3)

#def triangle(sayi):
#    for i in range(sayi):
#     print("#"*(i+1))


#triangle(6)

#def greatest_number(n1,n2,n3):
#    if n1 > n2 and n1 > n3:
#        return n1
#    elif n2 > n1 and n2 > n3:
#        return n2
#    elif n3 > n1 and n3 > n2:
#        return n3
#    else:
#        return str(n1) + " they both have the same number"

#print(greatest_number(3,3,3))
mylist = []
while True:
    a = input("Word:")
    if a in mylist:
        break
    else:
        mylist.append(a)
length = len(mylist)
print(F"You typed {length} different words!")