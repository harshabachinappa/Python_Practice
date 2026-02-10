#1

# my_list = [10, 20, 30, 40, 50, 11]
# my_list.reverse() #method 1 using reverse function
# print(my_list) #printing list 

# reverse_list = my_list[::-1] #method 2 slicing using negative indexes
# print(reverse_list) #printing the list

#_____________________________________________________________________________________________________


#2 

# list1 = [1,2,3,4,5] #list1
# list2 = [4,5,6,7,8] #list2

# empty_list = [] #creating empty list

# for i in list1: #using for loop to iterate through numbers from list1
#     for j in list2: #using for loop to iterate through numbers from list2 
#         if i == j: #checking for if condition
#             empty_list.append(i) #appending i into empty list

# print(empty_list) #printing empty list

#_____________________________________________________________________________________________________


#3

# original_list = [1,2,2,3,4,4,5] #original list from user
# unique_list = [] #creating a unique list

# for i in original_list: #for loop to iterate through original list
#     if i not in unique_list: if the element is not in unique list
#         unique_list.append(i) #appending it into unique list

# print(unique_list) #printing unique list

# unique_list = print(set(original_list)) #other method is using type conversion into set

#_____________________________________________________________________________________________________

#4 

# duplicated_list = [1,2,2,3,4,4,5]

# new_list = []

# for i in duplicated_list:
#     if i not in new_list:
#         new_list.append(i)

# print(new_list)

#_____________________________________________________________________________________________________

#1 List concatenation

# list1 = [1,2,3,4,5]
# list2 = [6,7,8,9,10]

# new_list = list1 + list2 #concatenation using + operator
# list1.extend(list2) #using extend function

# print(list1) #printing result
# print(new_list) #printing resut 

#_____________________________________________________________________________________________________


#2 

# list1 = ['a','b','c','d','e'] #user input list

# print(list1.copy()) #using copy() function to duplicate and print the list
# print(list1.copy()) #using copy() function to duplicate and print the list
# print(list1.copy()) #using copy() function to duplicate and print the list

#_____________________________________________________________________________________________________


#3 

# list1 = [1,2,3,4,5,6,7,8,9,10] #user input list

# print(list1[::2]) #using slicing method to remove even indices from the list by giving step count 2

#_____________________________________________________________________________________________________


#4

# my_list = [1, 2, 'python life', 5.6, 8, 'list'] #user list

# my_list.insert(0,10) #adding 10 at 0 index
# my_list.insert(1,11) #adding 11 at 1st index
# my_list.insert(2,12) #adding 12 at 2nd index

# print(my_list) #printing the list after operations

#output : 
# [10, 1, 2, 'python life', 5.6, 8, 'list']
# [10, 11, 1, 2, 'python life', 5.6, 8, 'list']
# [10, 11, 12, 1, 2, 'python life', 5.6, 8, 'list']

#_____________________________________________________________________________________________________

#1 Square numbers 

#sqaures = print([i**2 for i in range(1,11)]) #List comprehension using for loop in a single line of code

#output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#_____________________________________________________________________________________________________


#2

# even_numbers = print([i for i in range(1,21) if i % 2 == 0]) #List comprehension using for loop and if condition in a single line of code

#_____________________________________________________________________________________________________


#3

# words = ['apple','banana','cherry','date'] #user input

# new_list = [] # creating a new list

# for i in words: looping through each element in list
#     new_list.append(len(i)) #appending i in new list

 
# print(new_list) #printing new list

#_____________________________________________________________________________________________________




