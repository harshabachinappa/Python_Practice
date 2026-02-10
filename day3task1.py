#Operators Task 1

# #coding exercise
#1

# name = input("Enter your name: ") #taking name from user using input function
# age = int(input("Enter your age: ")) #taking age from user using input function

# print(f"Welcome! Your name is {name} and you are {age} years old!")

# output: Enter your name: Harsha
# Enter your age: 28
# Welcome! Your name is Harsha and you are 28 years old!

#2

# numbers = [1,2,3,4,5,6,7,8,9,10] #creating a list called numbers with 1 to 10 as elements
# print(5 in numbers) #checking if 5 is in the list
# print(15 not in numbers) #checking if 15 is not in the list

# output: 
# True
# True

#Operators Task 2

#coding exercises

#1

#program to calculate area of a recctangle

# length = float(input("Enter the length of the rectangle in cms: ")) #taking user input for length using input function
# width = float(input("Enter the width of the rectangle cms: ")) #taking user input for length using input function

# area = length * width #calculating area by using multiplication operator and storing result in "area" variable

# print(f"The area of the rectangle is {area}cm2. ") #printing the area after calculation

# output: 

# Enter the length of the rectangle in cms: 3.9
# Enter the width of the rectangle cms: 4.5
# The area of the rectangle is 17.55cm2. 

#2

#program to demonstrate incrementing and decrementing variable

#var1 = 5 #declaring variable with value 

#var1 += 1 #incrementing the variable with 1
#print(var1) #printing variable after incrementation

#output: 6

#var2 = 10 #declaring variable with value

#var2 -= 1 #decrementing variable with 1
#print(var2) #printing variable after decrementation

#output: 9

#3

#python program to convert temperature from Celsius to Fahrenheit

# celsius = float(input("Enter temperature in celsius: ")) #taking celsius inout from the user
# fahrenheit = (celsius * (9/5)) + 32 #converting into fahrenheit using formula

# print(f"{celsius} degrees C in fahrenheit is {fahrenheit} degrees F ")

# output: 
# Enter temperature in celsius: 34.7
# 34.7 degrees C in fahrenheit is 94.46000000000001 degrees F 


#4 simple interest calculator

# principal = int(input("Enter the principal amount: ")) #taking principal amount from user
# time = int(input("Enter the time in year(s): ")) #taking time from user
# rate_of_interest = float(input("Enter the rate of interest: ")) #taking rate of interest for the period from user

# simple_interest = (principal * time * rate_of_interest / 100 ) #calculatng simple interest using given formula (ptr/100)

# print(f"The simple interest for {principal} rupees for a given time of {time} years with a rate of interest being {rate_of_interest} % is {simple_interest}") #printing the result using f string

# output: 
# Enter the principal amount: 19000
# Enter the time in year(s): 1
# Enter the rate of interest: 5.5
# The simple interest for 19000 rupees for a given time of 1 years with a rate of interest being 5.5 % is 1045.0

#5 

#concatenate strings

# first_name = input("Enter your first name: ") #taking input from user
# last_name = input("Enter your last name: ") #taking input from user

# full_name = first_name + ' ' + last_name #concatenating both strings using '+' operator

# print(f"Your full name is {full_name}") #printing the final result

# output: 

# Enter your first name: Harsha
# Enter your last name: Bachinappa
# Your full name is Harsha Bachinappa

#6

#converting kilometers to miles

kilometers = float(input("Enter the distance in kilometers: "))

miles = kilometers * 0.621371 

print(f"The distance for {kilometers} kms in miles {miles} mi.")




