#with open ("ugabuga.txt") as new_file:
#    content = new_file.read()
#    print(content)

#sayilist =[]
#with open ("numbers.txt") as file:
#    for number in file:
#        sayilist.append(int(number))
#    print(sayilist)

#def largest(numbers):
#    largest = 0
#    for number in numbers:
#        if number > largest:
#            largest = number
#    return largest

#def minimum(numbers):
#    minimum = 99
#    for number in numbers:
#        if number < minimum:
#            minimum = number
#    return minimum
#def average(numbers):
#    average = 0
#    for number in numbers:
#        average += number

#    return average/len(numbers)

#print(largest(sayilist))
#print(minimum(sayilist))
#print(average(sayilist))

#text ="iskender,büyük,ana adı cevriye,baba adı musa,istanbul 01.01.1955doğumlu,istanbul üsküdar kuzguncuk mahallesine kayıtlı,türkiye cumhuriyeti uyruklu,bekar,sabıkasız,emekli memur"
#words = text.split(",")
#for word in words:
#    print(word)

#notlist =[]
#with open("grades.csv",encoding ="utf-8") as file:
#    for line in file:
#        line = line.replace("\n","")
#        parts = line.split(";")
#        name = parts[0]
#        grade = [int (x) for x in parts[1:]]
#        notlist.append(grade)
#dict ={}
#def read_fruits():
#    with open("fruits.csv",encoding='utf-8') as fruits:
#        for line in fruits:
#            line = line.replace('\n','')
#            parts =line.split(';')
#            name=parts[0]
#            price=[float(x) for x in parts[1:]]
#            dict[name]=price
#        return dict

#print(read_fruits())

#def row_sums(lines):
#    sums =[]
#    for line in lines:

#        parts =line.strip().line.split(",")
#        for row in column:
#            sum += row
#        list.append(sum)
#    return list


#def matrix_sum():
#    with open("matrix.txt",encoding="utf-8") as file:
#        for line in file:
#            line = line.replace("\n","")
#            parts = line.split(",")
#            row_sums(line)



#def average(grades):
#    total = []
#    for grade in grades:
#        avg = sum(grade)/len(grade)
#        total.append(avg)
#    return total

#print(average(notlist))

#with open("new_file.txt", "w") as my_file:
#    my_file.write("Hello there!")
#    my_file.write("This is the second line")
#    my_file.write("This is the last line")


