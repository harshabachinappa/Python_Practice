#single line comment 
#Used to explain small part of the code in a single line

'''Multi line
comments'''

'''Used to explain a big part of the code spanning over multiple lines'''
#____________________________________________________

var1 = 3 #interger variable
var2 = "pythonlife" #string variable

print(var1) #printing integer variable using print function
print(var2) #printing string variable using print function

#_____________________________________________________

#printing a pattern using multiple print statements 

print("   *")
print("  **")
print(" ***")
print("****")

'''output:   *
            **
           ***
          ****'''
#_____________________________________________________

#performing integer division of two numbers

var1 = 6.8 #declaring floating point number
var2 = 2 #declaring an interger

result = var1 // var2 #performing integer division and storing number in result variable

print(result) #printing the result 

#_______________________________________________________

var1 = 4 #integer datatype
var2 = 7.8 #float dataype
var3 = "PythonLife" #string datatype

print(var1) #printing the result 
print(var2) #printing the result 
print(var3) #printing the result 

#_____________________________________________________

discount = 20 
print(discount) #printing discount
print(type(discount)) #printing discount using type function

#Expected output: 20
#Dataype of discount: <class 'int'>

#_____________________________________________________

#The memory addresses of x and y

employee_id = 10
person_age = 10

print(id(employee_id))
print(id(person_age))

#output: 

#4323861136
#4323861136

#______________________________________________________

age = input("Enter age: ") #user enter age

age = int(age) #converting age into int datatype
print(type(age)) #printing the variable with type function

#output: <class 'int'>

#_______________________________________________________

str1 = "Python" #string 1
str2 = "Life" #string 2

result = str1 + str2 #concatenating the strings

print(result) #printing result of concatenation

#output: PythonLife