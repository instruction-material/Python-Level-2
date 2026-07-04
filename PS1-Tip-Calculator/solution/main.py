###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

bill = float(input("Enter your total bill amount, in dollars: "))
tip_percent = float(input("Enter the percent you would like to tip, as a decimal: "))

tip = bill * tip_percent

print("Your tip, rounded down to the nearest dollar: " + str(int(tip)))
print("Your tip, rounded down to the nearest cent: " + str("%.2f" % tip))
