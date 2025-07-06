#Let’s start with a simple version of the app that:

#Shows a menu

#Lets you add income or expense

#Keeps running until the user exits

#starting with a balance of 0, 0.0 is a float (for decimals, i.e. 45.99)
balance = 0.0 

#creating an empty list to store every income or expense you add
transactions = []

#deisplay menu, Infinite loop - it keeps repeating the menu until you choose to exit
#we'll use break to exit the loop when the user chooses option 5
while True: 

    print("\nWhat would you like to do?") #\n adds a blank line before the menu (for readability)
    print("1. Add income")
    print("2. Add expense")
    print("3. View balance")
    print("4. View all transactions")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ") #choice is stored as a string like '1', '2'

    #option 1: add income 
    if choice == "1":
        amount = float(input("Enter income amount: ")) #ask for the amount and convert it to float (for decimals) 
        balance += amount #add to balance using +=
        transactions.append(("Income", amount)) #add to the transacrtions list as a tuple: ("Income", amount)
        print(f"Added income of ${amount}") #print a confirmation using an f-string 
    elif choice == "2":
        amount = float(input("Enter expense amount: "))
        category = input("Enter category (e.g. food, rent): ")
        balance -= amount #Subtract from balance using -=
        transactions.append((category, -amount))
        print(f"Added expense of ${amount} in category '{category}'") #Store it as a negative value in transactions: e.g. ("food", -20.0)

    elif choice == "3":
        print(f"Current balance: ${balance}") #Just shows your current running balance.

    elif choice == "4": #this loops through the transactions list
        print("\nAll Transactions:") 
        for t in transactions: #each t is a tuple like ("food", -30.0)
            print(f"{t[0]}: ${t[1]}") #t[0] is the catrgory, t[1] is the amount
    
    elif choice == "5":
        print("Ciaooo!")
        break
    
    else:
        print("Invalid choice. Please enter 1-5.")        
