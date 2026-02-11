#mode = 'r+'

# file = open("/Users/krishnaharshabachinappa/Library/Mobile Documents/com~apple~CloudDocs/Python_tutorial/demo.txt", mode = 'r+') #importing file from working directory
# read_data = file.read() #reading the file
# print(read_data) #printing data
# file.close() #closing the file


# file = open("/Users/krishnaharshabachinappa/Library/Mobile Documents/com~apple~CloudDocs/Python_tutorial/demo.txt", mode = 'r+') #importing file from working directory
# write_data = file.write("I am learning python") #writing data into the file
# file.close() #closing the file

#___________________________________________________________________________________________________________________________________________

#mode = 'a+'

# file = open("tutorial.txt", mode = 'a+') #creating a file using a+
# write_data = file.write("This is a tutorial") #writing data
# print(file.tell()) #checking cursor position
# file.seek(0) #assigning cursor postion to 0
# read_data = file.read() #reading data in file

# print(read_data)
# file.close() #closing file



#___________________________________________________________________________________________________________________________________________


# file = open("sample123.txt", mode = 'w+') #creating a file
# write_data = file.write("This is sample information!") #writing data
# file.close() #closing file

# file = open("sample123.txt", mode = 'w+') #creating a file
# write_data = file.write("Welcome to sample123") #truncating data
# print(file.tell()) #returning curson position
# file.seek(0) #setting cursor position
# read_data = file.read() #reading data

# print(read_data) #printing data that is read
# file.close() #closing file

