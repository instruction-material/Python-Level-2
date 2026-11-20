accounts = {
    "ari": {"access_phrase": "demo-ari", "balance": 0},
    "bea": {"access_phrase": "demo-bea", "balance": 0},
}


def read_amount():
    try:
        amount = int(input("Whole dollars: "))
    except ValueError:
        return 0
    return amount


def run_account(username, account):
    print(f"{username} has ${account['balance']}.")
    while True:
        command = input("1 deposit, 2 withdraw, 3 change phrase, 4 log out, 5 balance: ").strip()
        if command == "4":
            return
        if command in {"1", "2"}:
            amount = read_amount()
            if amount <= 0:
                print("Enter a positive whole-dollar amount.")
            elif command == "2" and amount > account["balance"]:
                print("Insufficient balance.")
            else:
                account["balance"] += amount if command == "1" else -amount
                print(f"Balance: ${account['balance']}")
        elif command == "3":
            old_phrase = input("Current sample phrase: ")
            if old_phrase != account["access_phrase"]:
                print("The current phrase did not match.")
                continue
            new_phrase = input("New sample phrase: ").strip()
            if new_phrase:
                account["access_phrase"] = new_phrase
                print("Sample phrase updated.")
            else:
                print("Enter a nonempty phrase.")
        elif command == "5":
            print(f"Balance: ${account['balance']}")
        else:
            print("Choose a command from 1 through 5.")


while True:
    username = input("Fictional account name (or q): ").strip().lower()
    if username == "q":
        break
    access_phrase = input("Sample access phrase: ")
    account = accounts.get(username)
    if account is None or account["access_phrase"] != access_phrase:
        print("Account name or access phrase did not match.")
    else:
        run_account(username, account)
