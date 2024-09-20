#Create ATM
print("Welcome to ATM")
print("your username is duaparveen \nyour password is 112233")

user_name = "duaparveen"
password = 112233
login = str(input("Enter your username: "))
pin = int(input("Enter your password: "))
Balance =10000

if user_name == login and password == pin:
   print("WELCOME TO ATM", user_name)
else:
   print( "Invalid username or password")
   exit()

choose = int(input("Select an option: \n1. Check Balance \n2. Withdraw \n3. Transfer"))
if choose == 1:
   print("Your balance is", "Rs.", Balance) 
if choose == 2:
   withdraw = int(input("Enter the amount you want to withdraw: "))
   if withdraw > Balance:
      print("Insufficient Balance")
   else:
      print("Please collect your cash")
      print("Your remaining balance is", "Rs.", Balance - withdraw)
if choose == 3:
  Amount = int(input("Enter the amount you want to transfer: ")) 
  if Amount > Balance:
      print("Insufficient Balance")
  account = int(input("Enter the account number: "))
  print( "Rs.",Amount, "is Transfered to", account)
  print("Your remaining balance is", "Rs.", Balance - Amount)

print("\"Thanks to come\"")

