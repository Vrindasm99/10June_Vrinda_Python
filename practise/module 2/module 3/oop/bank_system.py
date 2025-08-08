
class Account:
    def acc_info(self):
        self.acc_no = input("Enter a new Account Number: ")
        self.name = input("Enter Account Holder Name: ")
        self.acc_type = input("Enter Account Type (Savings/Current): ")


class BankDetails(Account):
    def cre_ac(self):
        self.balance = float(input("Enter Opening Balance (Min ₹20000): "))
        if self.balance < 2000:
            print("Opening balance must be at least ₹20000.")
            exit()
        print("\n Account Created Successfully!")


class Transaction(BankDetails):
    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        self.balance += amount
        print(" Amount added successfully. Current Balance: ₹", self.balance)

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if amount > self.balance:
            print(" Not enough balance.")
        else:
            self.balance -= amount
            print(" Withdrawal successful. Remaining Balance: ₹", self.balance)


    def show(self):
        print("\n Account Details:")
        print("Account Number :", self.acc_no)
        print("Holder Name    :", self.name)
        print("Account Type   :", self.acc_type)
        print("Current Balance: ₹", self.balance)

user = Transaction()
user.acc_info()
user.cre_ac()

for i in range(3):
    print("\nSelect an option:")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Show Account Info")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        user.deposit()
    elif choice == '2':
        user.withdraw()
    elif choice == '3':
        user.show()
    else:
        print("Invalid choice. Please enter 1, 2 or 3.")

print("\n--------THANK YOU----------")
