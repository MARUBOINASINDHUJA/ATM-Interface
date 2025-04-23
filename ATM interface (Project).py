class ATM:
    def __init__(self):
        self.balance = 0

    def check_balance(self):
        print(f"Current balance is: {self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"{amount} has been deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount
        print(f"{amount} has been withdrawn. New balance: {self.balance}")

def atm_interface():
    atm = ATM()
    while True:
        print("\nATM Menu")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            atm.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            atm.withdraw(amount)
        elif choice == '4':
            print("Thank you for using our ATM.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
if __name__ == "__main__":
    atm_interface()
