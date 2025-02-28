class Account:
    def __init__(self,account_number, name , balance):
        self.account_number=account_number
        self.name=name
        self.balance=balance
    def __repr__(self):
        return f"({self.account_number},{self.name},{self.balance}"
class Bank(Account):
    account_numbers=[]
    savings=""
    def  load_from_file():
        try:
            with open("accounts.txt","r") as file:
                lines=file.readlines()
                return lines
        except Exception:
            print("There is no accounts")
            return []

    def create_account(name, initial_deposit):
        for i in range(1000,100000000):
            if i not in Bank.account_numbers:
                account_number=str(i)
                Bank.account_numbers.append(i)
                break
        Bank.savings += f"{account_number} {name} {initial_deposit}\n"

    def view_account(account_number):
        lines = Bank.load_from_file()
        found = False
        for line in lines:
            parts = line.split(" ")
            if len(parts) >= 3 and parts[0] == str(account_number):  
                print(line.strip())
                found = True
                break
        if not found:
            print("There is no account with this number")

    def deposit(account_number, amount):
        lines = Bank.load_from_file()
        Bank.savings = ""

        for line in lines:
            parts = line.strip().split(",")
            if len(parts) >= 3 and parts[0] == str(account_number):
                balance = int(parts[2])  # Extract balance
                balance += int(amount)  # Update balance
                parts[2] = f"{balance}"  # Update balance string
            Bank.savings += " ".join(parts) + "\n"

    def withdraw(account_number, amount):
        lines = Bank.load_from_file()
        Bank.savings = ""

        for line in lines:
            parts = line.strip().split(",")
            if len(parts) >= 3 and parts[0] == str(account_number):
                balance = int(parts[2])  # Extract balance
                balance -= int(amount)  # Update balance
                parts[2] = f"{balance}"  # Update balance string
            Bank.savings += " ".join(parts) + "\n"
    def save_to_file():
        with open("accounts.txt","w") as file:
            file.write(Bank.savings)
        Bank.savings=""
    
a=True
while a:
    print("welcome!\n What do you want to do?")
    print("PLease select 1 for creating account")
    print("Please select 2 for viewing accounts")
    print("PLease select 3 for making deposit")
    print("PLease select 4 to withdraw")
    print("Please select 5 to save your changes")
    print("PLease select 6 to exit" )
    choice=int(input())
    if choice==1:
        print("PLease enter the name and initial deposit")
        name,initial_deposit=input().split()
        Bank.create_account(name, initial_deposit)
    elif choice==2:
        account_number=input("Please enter account number to view: ")
        Bank.view_account(account_number)
    elif choice==3:
        account_number=input("PLease enter the acount number: ")
        amount=input("Please enter the amount you want to deposit: ")
        Bank.deposit(account_number,amount)
    elif choice==4:
        account_number=input("PLease enter the acount number: ")
        amount=input("Please enter the amount you want to withdraw: ")
        Bank.withdraw(account_number,amount)
    elif choice==5:
        Bank.save_to_file()
        print("Your changes succesfully saved!")
    elif choice==6:
        print("Goodbye")
        a=False
    else:
        print("Please select only number between 1 and 6")

        

              
