def main():
    transactions = []
    
    balance = float(input("Enter initial account balance: "))
    
    while True:
        print("\n1. Withdraw")
        print("2. View Transactions")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                amount = int(input("Enter amount to withdraw: "))
                fee = 100
                max_withdrawal = 20000
                max_percent = balance * 0.9

                if amount <= 0:
                    print(" Amount must be positive.")
                elif amount % 500 != 0:
                    print(" Must be in multiples of 500.")
                elif amount > max_withdrawal:
                    print(" Cannot withdraw more than 20,000 at once.")
                elif amount > max_percent:
                    print(" Cannot withdraw more than 90% of balance.")
                elif balance - amount - fee < 100:
                    print(" Your minimum balance cannot be less than 100 naira")
                else:
                    balance -= (amount + fee)
                    print(" Withdrawal successful!")
                    print(f"Amount Withdrawn: {amount}")
                    print(f"Withdrawal Fee: {fee}")
                    print(f"Remaining Balance: {balance}")
                    transactions.append(f"Withdrawn: {amount}, Fee: {fee}, Balance: {balance}")
            except ValueError:
                print(" Invalid amount. Please enter a number.")

        elif choice == '2':
            print("\n Transaction History:")
            if not transactions:
                print("No transactions yet.")
            else:
                for t in transactions:
                    print(t)

        elif choice == '3':
            print(" Thanking for using the ATM.")
            break

        else:
            print(" Invalid choice. Try again.")

if __name__ == "__main__":
    main()
