#def line (n1,st1):
#    if st1 == "":
#        print("*"*n1)
#    else:
#        print(st1[0]*n1)
import math

#line(7, "%")
#line(10, "LOL")
#line(3, "")

#def box_of_hashes(row):
#    for i in range (0,row):
#        print("#"*10)


#box_of_hashes(5)
#print()
#box_of_hashes(2)

#def square_of_hashes(n1):
#    for i in range (0,n1):
#        print("#"*n1)

#square_of_hashes(5)
#print()
#square_of_hashes(3)

#def square(num,st1):
#    for i in range(num):
#        print(st1*num)

#square(5, "*")
#print()
#square(3, "o")

#def triangle(n1):
#    for i in range(1,n1+1):
#        print("#"*i)

#triangle(6)
#print()
#triangle(3)

#def shape(n1,st1,n2,st2):
#   for i in range(1,n1+1):
#        print(st1*i)
#    for i in range(1,n2+1):
#        print(st2*i)

#shape(5, "X", 3, "*")
#print()
#shape(2, "o", 4, "+")
#print()
#shape(3, ".", 0, ",")

#def spruce(n1):
#    a ="*"
#    sayac = n1
#    for i in range(1,n1+1):
#        print(" "*sayac + a)
#        sayac -=1
#        a +="**"

#    print(" "*n1 + "*")

#spruce(5)
#spruce(3)
#spruce(2)

#def greatest_number(num1,num2,num3):
#    if num1 > num2 and num1 > num3:
#        return num1
#    elif num2 > num1 and num2 > num3:
#        return num2
#    elif num3 > num1 and num3 > num2:
#        return num3
#    else:
#        return num1
#print(greatest_number(3, 4, 1)) # 4
#print(greatest_number(99, -4, 7)) # 99
#print(greatest_number(0, 0, 0)) # 0

#def same_chars(st1,n1,n2):
#    if n1>len(st1) or n2>len(st1):
#        return False

#    return st1[n1] == st1[n2]

#print(same_chars("programmer", 6, 7))
#print(same_chars("programmer", 0, 4))
#print(same_chars("programmer", 0, 12))

#def first_word(sentence):
 #   for i in range (len(sentence)):
 #       if sentence[i] == ' ':
 #           return sentence[:i]

#def second_word(sentence):

#    words = sentence.split()
#    if len(words) >= 1:
#        return words[1]
#    else:
#        return ''

#def last_word(sentence):
#    words = sentence.split()
#    if len(words) >= 1:
#        return words[-1]
#    elif len(words) == 0:
#        return words[0]
#    else:
#        return ''

#sentence = "it was a dark and stormy python"

#print(first_word(sentence)) # it
#print(second_word(sentence)) # was
#print(last_word(sentence))

#list = [1, 2, 3, 4, 5]
#while True:

#    index = int(input("Index: "))
#    if index == -1:
#        break
#    newValue = int(input("New Value: "))
#    list[index] = newValue
#    print(list)
#mylist = []
#items = int(input("How many items: "))
#for i in range(items):
#    a = int(input("İtem " + str(i+1) +": "))
#    mylist.append(a)

#print(mylist)

#mylist = []
#print(F"The list is now {mylist}")
#sayac = 1
#while True:
#    a = input("a(d)d, (r)emove or e(x)it: ")
#    if a == "d":
#        mylist.append(sayac)
#        sayac += 1
#        print(F"The list is now {mylist}")
#
#    elif a == "r":
#        if mylist:  # Liste boş değilse devam et
#            mylist.remove(mylist[-1])  # Listenin en son eklenen elemanını sil
#            print(F"The list is now {mylist}")
#            sayac -=1
#        else:
#            print("The list is empty, cannot remove an item!")
#
#    elif a == "x":
#        print("Bye")
#        break

#mylist =[]
#while True:
#    a = input("Word: ")
#    if a in mylist:
#        break
#    else:
#        mylist.append(a)
#
#print(F"You typed in {len(mylist)} words.")

#mylist = []
#while True:
#    a = int(input("New item: "))
#    if a == 0:
#        print("Bye!")
#        break
#    mylist.append(a)
#    print(F"The list is now: {mylist}")
#    order = sorted(mylist)

#    print(F"The sorted list is now: {order}")

#def length (mylist):
#    return len(mylist)

#mylist = [1,2,3,4,5]
#a = length(mylist)
#print(F"The length of the list is: {a}")

#def mean(mylist):
#    return sum(mylist) / len(mylist)

#b = mean(mylist)
#print(F"The mean of the list is: {b}")

#def range_of_list(mylist):
#    return max(mylist) - min(mylist)


#c = range_of_list(mylist)
#print(F"The range of the list is: {c}")

#a = input("Type in a string: ")
#aLen = len(a)
#index = 0
#while index < aLen:
#    print(a[index])
#    print("*")
#    index += 1

#a = int(input("Please type in a positive integer: "))
#b = a*-1
#for i in range(a*2):
#    if b == 0:
#        b+=1
#    print(b)
#    b+=1

#def list_of_stars(mylist):
#    for i in range(len(mylist)):
#        print("*"*mylist[i])

#list_of_stars([3, 7, 1, 1, 2])

#def palindrome():
#    st1 = input("Please type in a palindrome: ")
#    st1 = st1.lower()
#    st2 =st1[::-1]
#    if st1 == st2:
#        print(F"{st1} is a palindrome")

#    else:
#        print(F"{st1} is not a palindrome")

#palindrome()

#def anagrams(st1,st2):
#    if sorted(st1) == sorted(st2):
#        return True
#    else:
#        return False

#print(anagrams("tame", "meta")) # True
#print(anagrams("tame", "mate")) # True
#print(anagrams("tame", "team")) # True
#print(anagrams("tabby", "batty")) # False
#print(anagrams("python", "java")) # False

#def sum_of_positives(mylist):
#    sum = 0
#    for i in range(len(mylist)):
#        if mylist[i] > 0:
#           sum += mylist[i]
#    return sum

#my_list = [1, -2, 3, -4, 5]
#result = sum_of_positives(my_list)
#print(F"The result is: {result}")

#def even_numbers(mylist):
#    newlist = []
#    for i in mylist:
#        if i % 2 == 0:
#            newlist.append(i)
#    return newlist

#my_list = [1, 2, 3, 4, 5]
#new_list = even_numbers(my_list)
#print("original", my_list)
#print("new", new_list)


#def list_sum(lista,listb):
#    newlist = []
#    for i in range (len(lista)):
#        newlist.append(lista[i]+listb[i])
#    return newlist

#a = [1, 2, 3]
#b = [7, 8, 9]
#print(list_sum(a, b)) # [8, 10, 12]

#def distinct_numbers(mylist):
#    newlist = []
#    for i in mylist:
#        if i not in newlist:
#            newlist.append(i)

#    newlist.sort()
#    return newlist

#my_list = [3, 2, 2, 1, 3, 3, 1]
#print(distinct_numbers(my_list)) # [1, 2, 3]

#def length_of_longest(list):
#    longest = list[0]
#    for i in range (len(list)):
#            if (len(list[i]))> len(longest):
#                longest = list[i]
#
#    return len(longest)
#
#my_list = ["first", "second", "fourth", "eleventh"]

#result = length_of_longest(my_list)
#print(result)

#def shortest(mylist):
#    shortest = mylist[0]
#    for i in range(len(mylist)):
#        if len(shortest) > len(mylist[i]):
#            shortest = mylist[i]
#    return shortest

#my_list = ["first", "second", "fourth", "eleventh"]

#result = shortest(my_list)
#print(result)

#my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

#result = shortest(my_list)
#print(result)

#def length_of_longest(words):
#    longest = [words[0]]  # İlk elemanı başlangıç olarak ata

#    for i in range(1, len(words)):  # İlk elemanı zaten eklediğimiz için 1'den başlıyoruz
#        if len(words[i]) > len(longest[0]):  # Daha uzun bir kelime bulunursa
#            longest = [words[i]]  # Listeyi sıfırla ve yeni kelimeyi ekle
#        elif len(words[i]) == len(longest[0]):  # Aynı uzunlukta kelime varsa
#            longest.append(words[i])  # Listeye ekle

#    return longest  # En uzun kelime(ler) listesini döndür


# Test
#my_list = ["first", "second", "fourth", "eleventh"]
#result = length_of_longest(my_list)
#print(result)  # Çıktı: ['eleventh']
#my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

#result = length_of_longest(my_list)
#print(result) # ['dorothy', 'richard']


#def formatted(mylist):
#    newlist = []
#    for x in mylist:
#        newlist.append(f"{x:.2f}")

#    print(newlist)

#my_list = [1.234, 0.3333, 0.11111, 3.446]
#formatted(my_list)

#def everything_reversed(list):
#    a = len(list)
#    newlist = []
#    while a>0:
#        newlist.append(list[a-1][::-1])
#        a -= 1
#    return newlist

#my_list = ["Hi", "there", "example", "one more"]
#print(everything_reversed(my_list))

#my_string = "Python is fun"

# Replaces the substring and stores the result in the same variable
#my_string = my_string.replace("Python", "Java")
#print(my_string)

#def most_common_character(st1):
#    a=st1.count(st1[0])
#    mcc = st1[0]
#    for i in range(len(st1)):
#        if st1.count(st1[i])>a:
#             mcc =st1[i]
#             a = st1.count(st1[i])

#    return mcc


#first_string = "abcdbde"
#print(most_common_character(first_string))

#def no_vowels(st1):
#    vowels = ['a', 'e', 'i', 'o', 'u']
#    l1 = len(st1)
#    st1 = st1.lower()
#    novowel = ""
#    for i in st1:
#        if i not in vowels:
#            novowel += i
#    return novowel

#my_string = "this is an example"
#print(no_vowels(my_string))

#print("XYZ".isupper())

#is_it_upper = "Abc".isupper()
#print(is_it_upper)

#def no_shouting(list):
#    newlist = []
#    for i in list:
#        if not i.isupper():
#            newlist.append(i)

#    return newlist

#my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
#print(no_shouting(my_list))

#def longest_series_of_neighbours(list):
#    if not list:
#        return 0
#    max_len = 1
#    current_len = 1
#    for i in range(1,len(list)):
#        if abs(list[i]-list[i-1])==1:
#            current_len += 1
#        else:
#            max_len = max(max_len,current_len)
#            current_len = 1

#    return max(max_len,current_len)

#my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
#print(longest_series_of_neighbours(my_list))

avg = []
fail = 0
g1 = 0
g2 = 0
g3 = 0
g4 =0
g5 =0
while True:
    input_data = input("Enter your exam points and exercises completed: ")
    if input_data=="":
        print("Statistics")
        print(F"Points Average: {sum(avg)/len(avg):.2f}")
        print(F"Pass Percentage: {((g1+g2+g3+g4+g5)/fail+g1+g2+g3+g4+g5)*100:.2f}%"),
        print("Grade distribution:")
        print("5: "+"*"*g5)
        print("4: "+"*"*g4)
        print("3: "+"*"*g3)
        print("2: "+"*"*g2)
        print("1: "+"*"*g1)
        print("0: "+"*"*fail)
        break
    exam_points,exercises_completed = map(int,input_data.split())
    exercises_points = exercises_completed //10
    total_points = exam_points + exercises_points
    avg.append(total_points)

    if 0<=total_points<=14:
        fail+=1
    elif 15<=total_points<=17:
        g1+=1
    elif 18<=total_points<=20:
        g2+=1
    elif 21<=total_points<=23:
        g3+=1
    elif 24<=total_points<=27:
        g4+=1
    elif 28<=total_points<=30:
        g5+=1

