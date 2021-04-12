import datetime      #using the import now function to show current date & time
print(datetime.datetime.now()) #fprint date after login
print("WELCOME TO 'SAYO ATM")

username = input("Enter username\n")
password = input("Enter password\n")
if password==password:
    print('Hello, %s' %username,'Welcome!')

print('These are the available options:')
print("1. Withdrawal")
print("2. Deposit")
print("3. Complaint")
balance = 'deposit'
choice = int(input("Please select an option\n"))

if (choice == 1):
    amount = int(input("Enter an amount to withdraw\n"))
    print('Take your cash.\nThank you for banking with us.')
elif (choice ==2):
    deposit = float(input('Enter amount to deposit.\n'))
    print(f"Available balance is ${deposit}.")
elif (choice ==3):
    complaint = input('What is you complaint?\n')
    print('Thank you for contacting us.\nYour complaint will be resolved in 48 hours.')
else:
    print('You have selected an invalid option.\nTry again.')