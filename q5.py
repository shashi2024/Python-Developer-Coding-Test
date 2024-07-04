def get_balance(account_number: str) -> float:
    with open("accounts.txt", 'r') as file:
        for line in file:
            acc_num, balance = line.strip().split(',')
            if acc_num == account_number:
                return float(balance)
    return 0.0  

def update_account(account_number: str, balance: float):
    accounts = {}
    with open("accounts.txt", 'r') as file:
        for line in file:
            acc_num, bal = line.strip().split(',')
            accounts[acc_num] = float(bal)
    
    accounts[account_number] = balance
    
    with open("accounts.txt", 'w') as file:
        for acc_num, bal in accounts.items():
            file.write(f"{acc_num},{bal}\n")

def deposit(account_number: str, amount: float):
    current_balance = get_balance(account_number)
    new_balance = current_balance + amount
    update_account(account_number, new_balance)

def withdraw(account_number: str, amount: float):
    current_balance = get_balance(account_number)
    if current_balance >= amount:
        new_balance = current_balance - amount
        update_account(account_number, new_balance)
    else:
        print("Insufficient balance")

print(get_balance("123456"))
deposit("123456", 50.0)
print(get_balance("123456"))
withdraw("123456", 30.0)
print(get_balance("123456"))
