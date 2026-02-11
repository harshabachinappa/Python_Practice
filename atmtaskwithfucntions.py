  

def credit(): #credit function
    global balance #using balance as local
    amount = float(input("Enter amount to credit: ")) #user input
    if amount <= 0:
        print("Please enter a positive amount.") #error handling if amount is negative
    else:
        balance += amount
        print(f"${amount} credited to your account.") #printing result


def debit(): #debit function
    global balance #using balance as local
    amount = float(input("Enter amount to debit: ")) #user input
    if amount <= 0:
        print("Please enter a positive amount.") #error handling if amount is negative
    elif amount > balance:
        print("Insufficient balance.") #error handling if balance is zero
    else:
        balance -= amount
        print(f"${amount} debited from your account.") #printing result


def balance_remaining(): #balance remaining function
    global balance #using balance as local
    print(f"Your current balance is: ${balance}") #printing result

def exit(): #exit function
    print("Thank you for using the ATM. Goodbye!") #printing result

balance = 0  #initializing balance to zero

#Repeating options block of code for user to choose
while True: 
    print("\nATM Menu:")
    print("1. Credit")
    print("2. Debit")
    print("3. Balance")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ") #user input

#calling functions as per user requirement

    if choice == '1':
        credit()
    elif choice == '2':
        debit()
    elif choice == '3':
        balance_remaining()
    elif choice == '4':
        exit()
        break
    else:
        print("Invalid choice. Please try again.") #else block 










