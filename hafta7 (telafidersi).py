lists = {}
lists[5] = [1, 2, 3]
lists[42] = [5, 4, 5, 4, 5]
lists[100] = [5, 2, 3]

print(lists)
print(type(lists))

#def times_ten(start_index: int, end_index: int) -> dict:
#    my_dict = {}
#    for i in range (start_index, end_index+1):
#        my_dict[i] = i*10

#    return my_dict

#d = times_ten(5, 10)
#print(d)

#def factorial(n: int):
#    fact = 1
#    for i in range(1, n + 1):
#        fact *= i
#    return fact

#def factorials(n:int) -> dict:
#    fact = {}
#    for i in range(1, n + 1):
#        fact[i] = factorial(i)
#    return fact

#k = factorials(5)
#for a in k:
#    print(f"key: {a}")
#    print(f"value: {k[a]}")

#def histogram(st1):
#    mydict = {}
#    for a in st1:
#        if a in mydict:
#            mydict[a] += 1
#        else:
#            mydict[a] = 1

#    for a in mydict:
#        print(f"{a} : {'*' * mydict[a]}")

#    print(mydict)
#histogram("statistically")
#histogram("anayinahmedi")

#def invert(dictionary: dict) -> dict:
#    inverted = {}
#    for key, value in dictionary.items():
#        inverted[value] = key

#    return inverted

#s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
#a =invert(s)
#print(a)

#def invert(dictionary: dict):
#    keys = list(dictionary.keys())  # Key'leri liste olarak al (sadece iterasyon için)

#    for key in keys:
#        value = dictionary[key]  # Mevcut değeri al
#        del dictionary[key]  # Eski key'i sil
#        dictionary[value] = key  # Yeni key-value çiftini ekle


#s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
#invert(s)
#print(s)

def oldest_person(people:list):
    min = 30000
    name =""
    for person in people:
        if min > person[1]:
            min= person[1]
            name = person[0]

    return name

p1 = ("Adam", 1977)
p2 = ("Ellen", 1985)
p3 = ("Mary", 1953)
p4 = ("Ernest", 1997)
people = [p1, p2, p3, p4]

print(oldest_person(people))







