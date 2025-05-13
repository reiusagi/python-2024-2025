#hourly_wage = float(input("Hourly wage: "))
#hours = int(input("Hours worked: "))
#day = input("Day of the week: ")


#daily_wages = hourly_wage * hours
#if day.upper() == "SUNDAY":
 #   daily_wages *= 2

#print(f"Daily wages: {daily_wages} euros")



#kosul1 = True

#while(kosul1):
    #try:
        #number = int(input("Please type in a number: "))
        #if number > 100:
         #   print("The number was greater than one hundred")
        #    number -= 100
       #     print("Now its value has decreased by one hundred")
      #      print("Its value is now " + str(number))
     #       print(str(number) + " must be my lucky number!")
    #        print("Have a nice day!")
   #     kosul1 = False
  #  except ValueError:
 #       print("Please type a number.")


#yas =int(input("yasinizi giriniz:"))
#if yas <18:
#    print("ufaklik")

#elif yas>18: #   print("yasiniz uygundur")
#print("Person 1")
#name = input("Enter your name: ")
#age = int(input("Enter your age: "))
#print("\n Person 2")
#name2 = input("Enter your name: ")
#age2 = int(input("Enter your age: "))

#if age>age2:
#    print(f"{name} elder than {name2}")

#elif age<age2:
#    print(f"{name2} elder than {name}")

#else:
#    print(f"{name} and {name2} at same age")

#verb1 =input("Please enter a verb: ")
#verb2 = input("Please enter a verb 2: ")

#if verb1.upper() > verb2.upper():
#    print(F"{verb1} is alphabetically last")

#elif verb1.upper() < verb2.upper():
#    print(F"{verb2} is alphabetically last")
#else:
#    print("Both are alphabetically same")

#grade = float(input("Grade: "))
#if grade < 0 or grade > 100:
#    print("impossible!")

#elif grade >= 90 and grade <= 100:
#    print("5")
#elif grade >= 80 and grade <= 89:
#    print("4")
#elif (grade >= 70 and grade <=79):
#    print("3")
#elif grade >= 60 and grade <= 69:
#    print("2")
#elif grade >= 50 and grade <= 59:
#    print("1")
#elif grade >= 0 and grade <= 49:
#    print("get the fuck out of here")

#gift = int(input("Value of gift: "))
#if gift <0:
#    print("impossible")
#elif gift <5000:
#    print("no tax")
#elif gift>=5000 and gift<25000:
#    print(F"Amount of tax: {100+(gift-5000)*0.08}")
#elif gift>=25000 and gift<55000:
#    print(F"Amount of tax: {1700+(gift-25000)*0.1}")
#elif gift>=55000 and gift<200000:
#    print(F"Amount of tax: {4700+(gift-55000)*0.12}")
#elif gift>=200000 and gift<1000000:
#    print(F"Amount of tax: {22100+(gift-200000)*0.15}")
#elif gift>=1000000:
#    print(F"Amount of tax: {142100+(gift-1000000)*0.17}")

#hak = 3
#while True:
#    password ="1234"
#    sifreal =input("sifre: ")
#    if sifreal =="1234":
#        print("Sifreyi dogru girdiniz sistem açılıyor...")
#        break
#    else:
#        hak -=1
#    if hak >=0:
#        print(F"Lütfen doğru giriniz {hak} hakkınız kaldi")
#    else:
#        print("Hakkiniz kalmadi baybay")
#        break

attempt = 1
while True:
    password ="1234"
    sifreal =input("sifre: ")
    if sifreal =="1234":
        print(F"Sifreyi {attempt}. seferde dogru girdiniz.")
        break
    else:
        attempt +=1
        print("Sifreyi yanlis girdiniz. Tekrar deneyiniz.")
