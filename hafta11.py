from itertools import count


def factorial(n: int):
    """ The function calculates the factorial n! for integers above zero """
    k = 1
    while n >= 2:
        k *= n
        n -= 1
    return k

if __name__ == "__main__":
    numbers = [5, 2, 4, 3, 0]
    factorials = []
    for number in numbers:
        factorials.append(factorial(number))
    print(factorials)

def factorials(numbers: list):
    return [factorial(number) for number in numbers]

print(factorials([3, 5]))

from math import sqrt
def square_roots(numbers: list):
    return [sqrt(number) for number in numbers]

lines = square_roots([1,2,3,4])
for line in lines:
    print(line)

def rows_of_stars(numbers: list):
    return [row*"*" for row in numbers]

rows = rows_of_stars([1,2,3,4])
for row in rows:
    print(row)

class ExamResult:
    def __init__(self, name, grade1, grade2, grade3):
        self.name = name
        self.grade1 = grade1
        self.grade2 = grade2
        self.grade3 = grade3


    def best_results(results: list):
        return [max(result.grade1, result.grade2, result.grade3) for result in results]


result1 = ExamResult("Peter", 5, 3, 4)
result2 = ExamResult("Pippa", 3, 4, 1)
result3 = ExamResult("Paul", 2, 1, 3)
results = [result1, result2, result3]

print(ExamResult.best_results(results))


def lengths(numbers: list):
    return [len(number) for number in numbers]

lists = [[1,2,3,4,5], [324, -1, 31, 7],[]]
print(lengths(lists))

numbers = [1, 1, 2, 3, 4, 6, 4, 5, 7, 10, 12, 3]

even_items = [item for item in numbers if item % 2 == 0]
print(even_items)

def remove_smaller_than(numbers: list, limit: int):
    return [number for number in numbers if limit<number]

numbers = [1,65, 32, -6, 9, 11]
print(remove_smaller_than(numbers, 10))

print(remove_smaller_than([-4, 7, 8, -100], 0))

def begin_with_vowel(words: list):
    return [word for word in words if word[0].lower() in "aeiou"]

word_list = ["automobile","motorbike","Animal","cat","Dog","APPLE","orange"]
for vowelled in begin_with_vowel(word_list):
    print(vowelled)

numbers = [1, -3, 45, -110, 2, 9, -11]
abs_vals = [number if number >= 0 else -number for number in numbers]
print(abs_vals)

class LotteryNumbers:
    def __init__(self, weeknum, numbers: list):
        self.weeknum = weeknum
        self.numbers = numbers

    def number_of_hits(self, numbers: list):
        return len([number for number in numbers if number in self.numbers])

    def hits_in_place(self,numbers: list):
        return [number if number in numbers else -1 for number in self.numbers]
week5 = LotteryNumbers(5, [1,2,3,4,5,6,7])
my_numbers = [1,4,7,11,13,19,24]

print(week5.number_of_hits(my_numbers))
print(week5.hits_in_place(my_numbers))

name = "Peter Python"

uppercased = [character.upper() for character in name]
print(uppercased)

name = "Peter"
char_list = list(name)
print(char_list)

print("".join(char_list))
print(" ".join(char_list))
print(",".join(char_list))
print(" and ".join(char_list))

test_string = "Hello there, this is a test!"

vowels = [character for character in test_string if character in "aeiou"]
new_string = "".join(vowels)

print(new_string)

def filter_forbidden(string: str,forbidden: str) -> str:
    return "".join([character for character in string if character not in forbidden])
sentence = "Once! upon, a time: there was a python!??!?!"
filtered = filter_forbidden(sentence, "!?:,.")
print(filtered)

def lengths(strings: list):
    return {string:len(string) for string in strings}

word_list = ["once", "upon" , "a", "time", "in"]

word_lengths = lengths(word_list)
print(word_lengths)

#def most_common_words(filename:str,lower_limit: int):
#    with open(filename,"r") as file:
#        for line in file:
#            return {word: count(word) for word in file if count(word >=lower_limit)}

#most_common_words("qwe.txt",4)

def add_numbers_to_list(numbers: list):
    a = 1
    while len(numbers) % 5 !=0:
        numbers.append(numbers[-1]+a)
    return numbers

numbers = [1,3,4,5,10,11]
add_numbers_to_list(numbers)
print(numbers)

def add_numbers_to_list(numbers: list):
    a = 1
    if len(numbers) % 5 ==0:
        return numbers
    else:
        numbers.append(numbers[-1] + a)
        add_numbers_to_list(numbers)

numbers = [1,3,4,5,10,11]
add_numbers_to_list(numbers)
print(numbers)


