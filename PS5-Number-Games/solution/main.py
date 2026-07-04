def is_even(n):
  return n % 2 == 0

print("The even numbers between 1 and 50 are...")
for i in range(1,51):
  if is_even(i):
    print(i)
print()

##########

def is_odd(n):
  return n % 2 != 0

print("The odd numbers between 1 and 50 are...")
for i in range(1,51):
  if is_odd(i):
    print(i)
print()

##########

def is_odd2(n):
  return not is_even(n)

print("The odd numbers between 1 and 50 are...")
for i in range(1,51):
  if is_odd2(i):
    print(i)
print()

##########

def is_multiple7(n):
  return n % 7 == 0

print("The multiples of 7 between 1 and 50 are...")
for i in range(1,51):
  if is_multiple7(i):
    print(i)
print()

##########

def is_multiple14(n):
  return n % 14 == 0

print("The multiples of 14 between 1 and 50 are...")
for i in range(1,51):
  if is_multiple14(i):
    print(i)
print()

##########

def is_multiple14v2(n):
  return is_even(n) and is_multiple7(n)

print("The multiples of 14 between 1 and 50 are...")
for i in range(1,51):
  if is_multiple14v2(i):
    print(i)
print()

##########

def is_prime(n):
  if n == 1:
    return False
  for i in range(2,n):
    if n%i == 0:
      return False
  return True

print("The prime numbers between 1 and 50 are...")
for i in range(1,51):
  if is_prime(i):
    print(i)
print()