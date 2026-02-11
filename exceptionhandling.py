#ValueError

# try: 
#     num1 = int(input("Enter a number: "))
#     num2 = int(input("Enter a number: "))
#     num1 + num2
    

# except ValueError as e:
#     print(f"ValueError: {e}")

#__________________________________________________________________________________________________________________

#TypeError

# try:
#     my_list = [1, 2, 3, 4]
#     print(my_list['1'])
# except TypeError as e:
#     print(f"TypeError Occured: {e}!")

#__________________________________________________________________________________________________________________

#FileNotFoundError

# try: 
#     file = open("/Users/krishnaharshabachinappa/Library/Mobile Documents/com~apple~CloudDocs/Python_tutorial/demo1.txt", mode = 'r+') 
#     read_data = file.read() 
#     print(read_data) 
#     file.close() 
# except FileNotFoundError as e:
#     print(f"FileNotFoundError: {e}")

#output: FileNotFoundError: [Errno 2] No such file or directory: '/Users/krishnaharshabachinappa/Library/Mobile Documents/com~apple~CloudDocs/Python_tutorial/demo1.txt'

#__________________________________________________________________________________________________________________

#ZeroDivisionError

# try: 
#     num1 = int(input("Enter a number: "))
#     num2 = int(input("Enter a number: "))
#     num1 / num2
    

# except ValueError as e:
#     print(f"ValueError: {e}")

#output: ZeroDivisionError: division by zero

#__________________________________________________________________________________________________________________

#IndexError


# try: 
#     my_list = [1,2,3,4,5]
#     print(my_list[6])
# except IndexError as e:
#     print(e)

#output: IndexError: list index out of range


#__________________________________________________________________________________________________________________


#KeyError

# try: 
#     my_dict = {"name": "Harsha", "Age": 28, "City": "Hyderabad"}
#     print(my_dict["Country"])
# except KeyError as e:
#     print(f"KeyError: {e}")

#output: KeyError: 'Country'

#__________________________________________________________________________________________________________________

#AttributeError


# try: 
#     x = 5
#     x.append(2,3)
#     print(x)
# except AttributeError as e:
#     print(f"Attribute error: {e}")


#__________________________________________________________________________________________________________________

#OverflowError


# import math

# try:
#     print(math.exp(1000))
# except OverflowError as e:
#     print(f"OverflowError: {e}")

#__________________________________________________________________________________________________________________

#runtimeError

# try: 
#     x = "Harsha"
#     print(Harsha)
# except RuntimeError as e:
#     print(e)

#output: NameError: name 'Harsha' is not defined

#__________________________________________________________________________________________________________________









