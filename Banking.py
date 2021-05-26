# Calculate grade for students
balance = 1000
def manageBanking():
    while True:
        bankingChoice = int(input("\nPlease Press 1 for your balance. \nPlease press 2 to make withdrawal. \nPlease press 3 to pay in. \nPlease press 4 to return card. \nWhat would you like to choose?"))
        if bankingChoice == 1:
            showBalance()
        elif bankingChoice == 2:
            withDrawFromAccount()
        elif bankingChoice == 3:
            depositToAccount()
        elif bankingChoice == 4:
            returnCard()
        else:
            print("Invalid option..\n")
        
        doReturn = input("\nWould you like to go back? ")
        if doReturn == "n":
            break
        

    return


def withDrawFromAccount():
    bankingChoice = int(input("\n$10\n$20\n$40\n$60\n$80\n$100\nFor other enter 1: "))
    global balance
    if bankingChoice == 10 or bankingChoice == 20 or bankingChoice == 40 or bankingChoice == 60 or bankingChoice == 80 or bankingChoice == 100 :
        balance = balance - bankingChoice
        showBalance()
    elif bankingChoice == 1 :
        customChoice = int(input("\nPlease Enter Desired Amount: "))
        balance = balance - customChoice
        showBalance()
    else:
        print("Invalid amount, please re-try..\n")

    return

def depositToAccount():
    depositAmount = int(input("\nHow Much Would You Like to Deposit? "))
    if depositAmount > 0:
        global balance
        balance = balance + depositAmount
        showBalance()
    else:
        print("Invalid amount, please re-try..\n")

    return

def returnCard():
    print("Please wait while your card is Returned .. \n\nThanks you for your service.")
    return

def showBalance():
    print("Your balance is :",balance)
    return

defaultPassword = 1234
count = 3
print("Welcome to Humber Bank ATM \n")
while True:
    try:
        if(count > 0):
            choice = int(input("Please Enter your 4 digit pin: "))
            if choice == defaultPassword:
                print("You entered your pin correctly.\n")
                count = 3
                manageBanking() 
            else:
                count = count - 1
                print("Incorrect password.\n")
        else:
            print("No more tries. \n")
            input("Press Enter to exit...")
            break
        
    
    except AssertionError as msg:
        print(msg)
        input("Press Enter to exit...")

