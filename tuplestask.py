#1

# my_details = ('Harsha', 28, 'Black') #creating a tuple
# print((my_details)) #printing the tuple
# print(type(my_details)) #checking type if my_details is a tuple

#2

# days_of_week = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
# third_item = days_of_week[2] #calling 3rd item as per user preference
# print(third_item) #printing result

#3
# tuple1 = (1, 3, 5) #tuple 1 with odd numbers
# tuple2 = (2, 4, 6) #tuple 2 with even numbers

# result = tuple1 + tuple2 #concatenation with + operator
# print(result) #printing result

#4
# rectangle = (8, 4.5) #tuple with lenght and width
# length = rectangle[0] #unpacking first element 
# width = rectangle[1] #unpacking second element

# area = length * width #calculating area

# print(f"The area of rectangle is {area} cm2") #printing result using f string

#5
# my_details = ('Harsha', 28, 'Black') #user input

# is_present = 'Harsha' in my_details #checking with membership test

# print(is_present) #printing result

#6
# items = [("Apple", 99), ("Banana", 99), ("Milk", 49)] #user input

# total = 0 #initializing total to zero

# print("Item \t\t Price") #printing item and price
# print('-' * 25) #printing - * 25 

# for i, j in items: #using for loop to iterate through each elements
#     print(f"{i} \t\t {j:.2f}") #printing 1 and j
#     total+=j #compound incrementing j to total
# print("-" * 25) 
# print(f"Total \t\t {total:.2f}") #printing result