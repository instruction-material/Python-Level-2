accounts = {"janesmith": "secret123", "bobsmith": "programm3r"}
balances = {"janesmith": 0, "bobsmith": 0}

while True:

  # login functionality
  while True:
    print("Welcome to the bank! Please log in.")
    username = input("Username: ")
    password = input("Password: ")
    if username not in accounts:
      print("\nWe don't recognize your username. Please try again.\n")
    elif password != accounts[username]:
      print("\nYour password is incorrect. Please try again.\n")
    else:
      break

  while True:
    num_choice = input("\nWelcome " + username + "! You currently have $" + str(balances[username]) + " in your account. What would you like to do?\n\t1. Make a deposit\n\t2. Make a withdrawal\n\t3. Change your password\n\t4. Log out\n")

    if num_choice == "1":
      deposit = input("How much would you like to deposit? ")
      balances[username] += int(deposit)
    elif num_choice == "2":
      withdraw = input("How much would you like to withdraw? ")
      balances[username] -= int(withdraw)
    elif num_choice == "3":
      old_password = input("To change your password, please type in your old password:")
      if old_password == accounts[username]:
        new_password = input("Please type in your new password:")
        accounts[username] = new_password
        print("\nYour password has been changed successfully!")
      else:
        print("\nYour old password does not match the password in our records.")
    elif num_choice == "4":
      break