# This is a sample Python script.
def show_balance():
    print(f'Your balance is {balance:.2f} taka')

def deposit():
    amount = float(input('Enter an amount'))
    if amount<0:
        print('Invalid amount')
        return 0
    else:
        return amount
def withdraw():
    amount = float(input('Enter the amount'))

    if amount > balance:
        print('Insufficinet funds')
        return 0
    elif amount < 0:
        print('Amount must be greater than 0')
        return 0
    else:
        return amount

balance =0
is_running = True

while is_running:
    print('Banking program')
    print('1.Show Balance')
    print('2.Deposit')
    print('3.Withdraw')
    print('4.Exit')
    choice = input('Enter your choice:')
    if choice =='1':
        show_balance()
    elif choice == '2':
        balance+=deposit()
    elif choice == '3':
        balance-=withdraw()
    elif choice =='4':
        is_running = False
    else:
        print("That is not a valid choice")
