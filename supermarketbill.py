name = input("Enter your Name:")

# List of items
lists = '''
Rice       Rs 10/kg
Sugar      Rs 8/kg
Oil        Rs 30/liter
Salt       Rs 25/kg
Paneer     Rs 40/kg
Maggie     Rs 12/pack
Boost      Rs 200/bottle
'''

# Declaration
price = 0
pricelist = []
totalprice = 0
Finalprice = 0
ilist = []
qlist = []
plist = []

# Rate for each item
items = {'rice':55, 'sugar': 30, 'oil': 160, 'salt': 25, 'paneer': 110, 'maggie': 22, 'boost': 235}

while True:
    option = input("Press 1 for list or 2 to exit: ")
    if option == '2':
        print("Thank you for shopping")
        break
    elif option == '1':
        print(lists)

        while True:
            inp1 = input("To buy press 1 or press 2 to exit: ")
            if inp1 == '2':
                print("Thank you for shopping")
                break
            elif inp1 == '1':
                item = input("Choose your items: ").lower()
                while True:
                    quantity_input = input("Enter quantity: ")
                    if quantity_input.isdigit():  
                        quantity = int(quantity_input)
                        break
                    else:
                        print("Please enter a valid quantity.")

                if item in items:
                    price = quantity * items[item]
                    pricelist.append((item, quantity, items[item], price))
                    totalprice += price
                    ilist.append(item)
                    qlist.append(quantity)
                    plist.append(price)
                else:
                    print("Selected item is not available. Sorry for the inconvenience.")

        if totalprice > 0:
            tax = (totalprice * 12) / 100
            finalamount = tax + totalprice

            print(25 * "=", "HyperMart Supermarket", 25 * "=")
            print(28 * " ", "Hyderabad, 500-062")
            print("Name:", name, 30 * " ")
            print(75 * "-")
            print("S.No", 10 * " ", 'Items', 8 * " ", 'Quantity', 8 * " ", 'Price')
            for i in range(len(pricelist)):
                print(i, 13 * " ", ilist[i], 8 * " ", qlist[i], 8 * " ", plist[i])
            print(75 * "-")
            print(50 * " ", 'Total amount:', 'Rs', totalprice)
            print("Tax amount", 50 * " ", 'Rs', tax)
            print(75 * "-")
            print(50 * " ", 'Final amount:', 'Rs', finalamount)
            print(75 * "-")
            print(20 * " ", "Thank you & Visit again")
            print(75 * "-")
