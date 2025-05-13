#my_list = [1, 2, 3, 3, 5]

#new_list = []
#for item in my_list:
#    new_list.append(item)

#new_list[0] = 10
#new_list.append(6)
#print("the original:", my_list)
#print("the copy:", new_list)

#my_list = [1,2,3,4]
#new_list = my_list[:]

#my_list[0] = 10
#new_list[1] = 20

#print(my_list)
#print(new_list)

#def augment_all(my_list: list) -> list:
#    new_list = []
#    for item in my_list:
#        new_list.append(item + 10)
#    my_list = new_list
#    return my_list
#numbers = [1, 2, 3]
#print("in the beginning:", numbers)
#numbers2= augment_all(numbers)
#print("after the function is executed:", numbers2) #sınav sorusu olabilir

#my_list = [1, 2, 3, 4]
#my_list[:] = [100, 99, 98, 97]
#print("in the end:", my_list)

#def double_items(mylist: list) -> list:
#    new_list = []
#    for item in mylist:
#        new_list.append(item * 2)

#    return new_list

#numbers = [1, 2, 3]
#print("in the beginning:", numbers)
#numbers2= double_items(numbers)
#print("after the function is executed:", numbers2)

#def double_items(mylist: list) -> list:
#    return [item*2 for item in new_list]

#numbers = [1, 2, 3]
#print("in the beginning:", numbers)
#numbers2= double_items(numbers)
#print("after the function is executed:", numbers2)

def remove_smallest(my_list: list):
    enkucuk = my_list[0]
    for item in my_list:
        if item < enkucuk:
            enkucuk = item

    my_list.remove(enkucuk)

numbers = [2, 4, 6, 1, 3, 5]
remove_smallest(numbers)
print(numbers)

def transpose(matrix: list):
   for i in range(len(matrix)):
       for j in range(i+1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]




   print(matrix)



matris =[[1,2,3],[4,5,6],[7,8,9]]
transpose(matris)