

def Show_balance(balance):
    print("***************")
    print(f"your balance is ${balance:.2f}")
    print("***************")

def deposit():
    print("***************")
    amount = float(input("Enter an amount to be deposited: "))
    print("***************")
    if amount < 0:
        print("***************")
        print("that's not a valid amount")
        print("***************")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter an amount to be withdrawn: ")) 

    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print("that's not a valid amount")
        return 0
    else:
        return amount
    
def main():

    balance = 0
    is_running = True

    while is_running:
        print("***************")
        print("Banking program")
        print("***************")
        print("1.Show balance")
        print("2.Deposit")
        print("3.withdraw")
        print("4.Exit")
        print("***************")

        choice = input("Enter your choice (1-4): ")


        if choice == '1':
            Show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice =='3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("***************")
            print("That is not a valid choice")
            print("***************")

    print("***************")
    print("Thank you! Have a nice day!")
    print("***************")

if __name__ == '__main__':

    main()