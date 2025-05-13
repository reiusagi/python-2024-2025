#print("Are you ready?")
#number = int(input("Please type in a number: "))
#while number > 0:
#    print(number)
#    number -=1

#print("Now!")

#number = int(input("Please type in a number: "))

#while number < 100 and number % 5 != 0:
#    print(number)
#    number += 3

#upper = int(input("Upper Limit: "))
#base = int(input("Base: "))

#a = base
#while a < upper:
#   print(a)
#   a = a*base
#n =10
#row ="*"
#while n>0:
#    print(" " * n + row)
#    row += "**"
#    n = n-1

#st1 = input("String 1: ")
#st2 = input("String 2: ")
#l1 = len(st1)
#l2 = len(st2)
#if l1 > l2:
#    print(F"{st1} is longer than {st2}")

#elif l2 > l1:
#    print(F"{st2} is longer than {st1}")
#else:
#    print(F"{st1} and{st2} both have the same length")

#st1 = input("Please type in a string: ")
#index = -1
#length = len(st1)
#while length > 0:
#    print(st1[index]) #pythonda indexlerin tersten kullanımı ile yapilan sistem
#    index -= 1
#    length -=1

#st1 = input("Please enter st1 : ")
#index = len(st1)-1
#while index >= 0: #yukaridaki ornegın normal sekilde yapilmis hali
#    print(st1[index])
#    index -= 1

#width = int(input("Enter width: "))
#height = int(input("Enter height: "))
#
#while height >0:
#    print("#"*width)
#    height -=1


#l1 = len(word)
#l1 //=2
#start = 14-l1
#end = 14+l1
#print("*"*30)
#print("*" + " "*start + word + " "*end + "*")
#print("*"*30)
#word = input("Enter a word: ")
#index =1
#while index <=3:
#    if index %2 ==1:           # yukseklik indeksi 1 veya 3 ise
#        print("*"*30)
#    else:                      # yukseklik indexi 2 ise
#        if(len(word) %2) == 0: # uzunluk cift sayi ise
#            print("*" + word +"*")
#
#        else:
#            start = (28 - len(word)) // 2
#            print("*" + " " * start + word + " " * (28 - start - len(word)) + "*")
#    index += 1
#input_string = "presumptious"

#print(input_string[0:3])
#print(input_string[4:10])

# if the beginning index is left out, it defaults to 0
#print(input_string[:3])

# if the end index is left out, it defaults to the length of the string
#print(input_string[4:])

#st1 = input("Please type in a string: " )
#l1 = len(st1)
#a = 1
#while l1 > 0:
#    print(st1[0:a])
#    a+=1
#    l1-=1

#st1 =input("Please type in a string: ")
#l1 =len(st1)
#while l1>0:
#    print(st1[0:l1])
#    l1=l1-1

#st1 =input("Please type in a string: ")
#l1 =len(st1)
#l2 = l1 -1
#while l2>=0:
#        print(st1[l2:l1])
#        l2 -= 1

st1 =input("Please type in a string: ") #sinav sorusu
char = input("Please type in a character: ")
index =st1.find(char)

if index == -1:
    print("The character doesn't exist")
else:
    print(st1[index] + st1[index + 1] + st1[index + 2])


