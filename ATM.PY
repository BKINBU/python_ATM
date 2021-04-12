# Initializing system

import random
database = {}

def init():
     
    print('WELCOME TO \'SAYO BANK')
    answer = int(input('Do you have an account with us:\n (1) Yes\n (2) No\nSelect an option\n'))
       
    if(answer == 1):
        login()

    elif (answer == 2):
        register()
    else:
        print('You have selected an invalid option')
        init()



# creating a Login function to include:(Account number or Full name, Password)
def login():

    user_account_number = int(input('Enter your account number.\n'))
    password = input('Enter your password.\n')

    for account_number, user_details in database.items():
        if(account_number == user_account_number):
            if(user_details[-1] == password):
                bank_operation(user)
        else:
            print('Invalid account or password')
            login()


# Registering a new user which to include:(First Name, Last Name, Password, Email)

def register():

    print('========== Fill in you details ==========')

    title = int(input('select a title:\n(1) Mr\n(2) Mrs\n(3) Miss\n'))
    first_name = input('Enter First Name\n')
    last_name = input('Enter Last Name\n')
    email = input('Enter a vaild email address\n')
    full_name = first_name + last_name
    password()

    account_number = genarate_account_number()

    database[account_number, user_details] = [title, first_name, last_name, email, password]
    
    print('Your account number has been generated' + full_name)
    print('=== ==== ==== ==== ==== ==== ==== ===')
    print('This is your account number: %d' %account_number)
    print('=== ==== ==== ==== ==== ==== ==== ===')

    login()

def password():
    password = input('Create a password\n')
    confirm_password = input('Confirm password\n')

    if  password == confirm_password:
        print('You have successfully been registered')
    else:
        print('Re-enter your password')
        password()         

    
# Generating account number and its function
def genarate_account_number():
    print('Generating account number')
    return random.randrange(0000000000, 9999999999)
    login()
    
  
# creating bank operation function

def bank_operation(user):
    
    print('Welcome %s %s' %(user[1], user[2]))
    print('Which transaction would you like to perform?\n(1) Withdrawal\n (2) Deposit\n (3) Complaint\n (4)Logout (5)Exit\n')
    
    choice = int(input("Please select an option\n"))

    if (choice == 1):
        
        Withdrawal()  
    elif (choice ==2):
        
        Deposit()
    elif (choice ==3):
        
        complaint()
    elif (choice == 4):
        login()
    elif (choice == 5):
        exit()
    else:
        print('You have selected an invalid option.\nTry again.')
        bank_operation(user)


#_____(Creating deposit, withdrawal, complaint and logout function)
def Withdrawal():
    amount = int(input("Enter an amount to withdraw\n"))
    print('Take your cash.\nThank you for banking with us.')

def Deposit():
    amount_deposited = float(input('Enter amount to deposit.\n'))
    print(f"Available balance is ${amount_deposited}.")

def complaint():
    user_complaint = input('What is you complaint?\n')
    print('Thank you for contacting us.\nYour complaint will be resolved in 48 hours.')

def logout():
    login()

init()
