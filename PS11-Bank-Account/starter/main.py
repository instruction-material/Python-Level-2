accounts = {
    "ari": {"access_phrase": "demo-ari", "balance": 0},
    "bea": {"access_phrase": "demo-bea", "balance": 0},
}

username = input("Fictional account name: ").strip().lower()
access_phrase = input("Sample access phrase: ")
account = accounts.get(username)
if account is not None and account["access_phrase"] == access_phrase:
    print(f"{username} has ${account['balance']}.")
    # Add the account menu and validated deposits and withdrawals.
else:
    print("Account name or access phrase did not match.")

# Repeat login after logout and retain each account's own balance.
