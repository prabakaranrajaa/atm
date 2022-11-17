# A python code to design an ATM machine

# start by defining some functions to make our code stress free
def substract(a, b):
    return a - b


def add(a, b):
    return a + b


def withdraw(accBalance, amount):
    newBalance = substract(accBalance, amount)
    return newBalance


def deposit(accBalance, amount):
    newBalance = add(accBalance, amount)
    return newBalance


def thanks():
    print("Thank you for banking with PRABA BANK")

# welcoming the user and assigning values to some variables


def main():
    name = print("WELCOME HAPPY DAY, TO PRABA BANK")

    balance = int(1000000)


# inputs your pin and checks if its correctso as to display your available balance
    while True:
        pin = int(input("Enter your password: "))
        password = 12345
        if password != pin:
            print("Password Incorrect")
            continue
        else:
            print("Your Balance Is: ", balance)

    # if balance is displayed, it prompts the user to select between 1,2 or 3 for the next line of action that would be performed
    # if the user selects "1", it askes "how much" and then shows available balance by deducting the amount withdrawn from the initial balance
            #money = input("1: withdraw or 2: deposit or 3: exit: ")
            while True:
                money = input(
                    "1: withdraw \n2: deposit\n3: exit \nEnter your choice: ")
                if money == "1":
                    user_withdraw = int(input("How Much: "))
                    print("You have withdrawn #",
                          user_withdraw, "from your Account")
                    if user_withdraw > balance:
                        print("You don't have sufficient funds")
                        thanks()
                    else:
                        balance = withdraw(balance, user_withdraw)
                        print("Your balance after withdrawal is: ", balance)
                        thanks()

        # elif the user selects "2", it shows "how much" and then shows the total balance
                elif money == "2":
                    user_deposit = int(input("How Much: "))
                    print("You have deposited $",
                          user_deposit, "to your Account")
                    if user_deposit > balance:
                        print("Plenty money to spend!")
                        print("Your balance after deposit is: ",
                              deposit(balance, user_deposit))
                        thanks()
                    else:
                        print("Your balance after deposit is: ",
                              deposit(balance, user_deposit))
                        thanks()

        # if user selects "3", thank you for banking with us!
                elif money == "3":
                    thanks()
                    break

                else:
                    print("Please Call The Security")
                    continue
        break


if __name__ == "__main__":
    main()
