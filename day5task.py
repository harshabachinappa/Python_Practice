#1 Vowel checker

# vowel = 'aeiouAEIOU' #pre dertiming vowels and assigning it to a variable

# character = input("Enter an alphabet: ") #taking input from user to check 

# if character in vowel: #if condition and using membership operator
#     print(f"Character {character} you have entered is a vowel!") #printing result

# else: #else condition if TBOC does not run
#     print(f"Character {character} you have entered is not a vowel!") #printing result


#_______________________________________________________________________________________________________________________________________________

#2 Age group classification

# age = int(input("Enter your age: ")) #taking input from user

# if age <= 0: #checking for age using if condition, age below 0 cannot exist
#     print(f"Invalid age! Age cannot be {age}!") #printing result as invalid

# elif age <= 12: #age below 12 in child, checking with elif
#     print(f"You are a child and your age is {age}!") #printing result as child

# elif age >= 13 and age <= 17: #age from 13 to 17 is teenager, checking with elif
#     print(f"You are a teenager and your age is {age}!") #printing result as teenager

# elif age >= 18 and age <= 64: #age from 18 to 64 is adult, chechking with elif 
#     print(f"You are an adult and your age is {age}!") #printing result as adult

# else: #else block if TBOC does not run
#     print(f"You are a senior and your age is {age}!") #printing result as senior

#_______________________________________________________________________________________________________________________________________________

# #3 Number Classifier

# number = int(input("Enter a number: ")) #taking a number from user and converting it into integer

# if number == 0: #checking for number using if codition and assignment operator
#     print(f"The number you have entered is zero!") #printing result

# elif number > 0: #checking for number using elif codition 
#     print(f"You entered {number} and it is positive") #printing result

# else: #using else codition if TBOC does not execute
#     print(f"You entered {number} and it is negative!") #printing result

#_______________________________________________________________________________________________________________________________________________

#4 Leap Year calculator

# year = int(input("Enter a year: ")) #taking input from user 

# if year % 400 == 0: #checking if year is divisible by 400 using if condition and assignment operator
#     print(f"The year {year} is a leap year!") #printing result

# elif year % 100 == 0: #checking if year is divisible by 100 using if condition and assignment operator
#     print(f"The year {year} is not a leap year!") #printing result

# elif year % 4 == 0: #checking if year is divisible by 4 using if condition and assignment operator
#     print(f"The year {year} is a leap year!") #printing result

# else: #else condition if TBOC does not execute
#     print(f"The year {year} is not a leap year!") #printing result

#_______________________________________________________________________________________________________________________________________________

#5 simple calculator

# num1 = float(input("Enter number1 to perform calculation: ")) #taking first number as input from user
# num2 = float(input("Enter number2 to perform calculation: ")) #taking second number as input from user
# operator = input("Enter a operator either +, -, *, /: ") #taking operator preference from user o perform calculation 

# if operator == '+': #checking for operator that user entered using if and assignment operator
#     result = num1 + num2 #adding two numbers becasue user chose addition operator
#     print(f"You chose {operator} (addition operator) and the sum of {num1} and {num2} is {result}!") #printing result using f string

# elif operator == '-': #checking for operator that user entered using elif and assignment operator
#     result = num1 - num2 #subtracting two numbers becasue user chose subtraction operator
#     print(f"You chose {operator} (subtraction operator) and the difference of {num1} and {num2} is {result}!") #printing result using f string

# elif operator == '*': #checking for operator that user entered using elif and assignment operator
#     result = num1 * num2 #multiplying two numbers becasue user chose multiplication operator
#     print(f"You chose {operator} (multiplicaton operator), {num1} times {num2} is {result}!") #printing result using f string

# elif operator == '/': #checking for operator that user entered using elif and assignment operator
#     result = num1 / num2 #diving two numbers becasue user chose division operator
#     print(f"You chose {operator} (division operator), {num1} divided by {num2} is {result}!") #printing result using f string

# else: #else block if TBOC does not execute
#     print(f"Invalid operator entered! {operator} is not an operator!") #printing result using f string

#_______________________________________________________________________________________________________________________________________________

#6 Short hand if

# x = 8
# if x % 2 == 0: 
#     result = "even"
# else: 
#     result = "odd"

#short hand if

# x = 8
# result = print(f" {x} is 'Even'" if x % 2 == 0 else "'Odd'") #short hand if - left side will run when if condition is true otherwise right side will run

#_______________________________________________________________________________________________________________________________________________

#7 Discount calculator

# original_price = float(input("Enter the original price of the item: ")) #taking original price from user
# discount_percentage = float(input("Enter the discount percentage: ")) #takinf discount percentage from user

# final_price = original_price - (original_price * (discount_percentage / 100)) #calculating final price by deducting original price time discount

# print(f"The final price of the item after applying {discount_percentage} % is {final_price}!") #printing result using f string

#_______________________________________________________________________________________________________________________________________________

#8 BMI calculator

# weight = float(input("Enter your weight in kgs: ")) #taking weight from user using input function 
# height = float(input("Enter your height in meters: ")) #taking height from user using input function 

# BMI = (weight / (height ** 2)) #calculating BMI using formula

# print(f"Your BMI for {weight} kgs and {height} m is {BMI}!") #printing result using f strings

#_______________________________________________________________________________________________________________________________________________








