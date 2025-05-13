from datetime import date

def list_years(dates: list) -> list:

    newlist = []
    for date in dates:
        newlist.append(date.year)

    newlist.sort()
    return newlist

date1 = date(2019, 2, 3)
date2 = date(2006, 10, 10)
date3 = date(1993, 5, 9)

years = list_years([date1, date2, date3])
print(years)

class BankAccount:

 def __init__(self, balance: float, owner: str):
        self.balance = balance
        self.owner = owner

#peters_account = BankAccount()
#peters_account.owner = "Peter Python"
#peters_account.balance = 5.0

#print(peters_account.owner)
#print(peters_account.balance)

ahmets_account = BankAccount(balance=10000, owner='ahmet')
ahmets_account.balance +=5000
print(ahmets_account.balance)
print(ahmets_account.owner)
class Book:

    def __init__(self,name,author,genre,year):
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year

python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)

print(f"{python.author}: {python.name} ({python.year})")
print(f"The genre of the book {everest.name} is {everest.genre}")

class Pet:
    def __init__(self,name,species,year_of_birth):
        self.name = name
        self.species = species
        self.year_of_birth = year_of_birth

def new_pet(name:str, species:str, year_of_birth:int) -> Pet:
    return Pet(name,species,year_of_birth)


fluffy = new_pet("Fluffy", "dog", 2017)
print(fluffy.name)
print(fluffy.species)
print(fluffy.year_of_birth)

def older_book(book1: Book, book2: Book):
    if book1.year < book2.year:
      return  print(f"{book1.name} is older than {book2.name}. It was published in {book1.year}.")
    elif book1.year == book2.year:
        return print(f"{book1.name} and {book2.name} were both published in {book1.year}.")
    else:
       return print(f"{book2.name} is older than {book1.name} It was published in {book2.year}.")

python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
norma = Book("Norma", "Sofi Oksanen", "crime", 2015)

older_book(python, everest)
older_book(python, norma)

class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.value = initial_value

    def print_value(self):
        print("value:", self.value)

    def decrease(self):
        if self.value >0:
            self.value -= 1
        if self.value ==0:
            print("DecreasingCounter is done.")
            self.value =0


counter = DecreasingCounter(1)
counter.print_value()
counter.decrease()
counter.print_value()
counter.decrease()
counter.print_value()
counter.decrease()
counter.print_value()