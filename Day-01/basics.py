# Task 1 : Sum of Two numbers
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
print("sum =", a + b)

# Task 2 : Check Even or Odd

num = int(input("Enter a number: "))
if num % 2 == 0:
  print("Even")
else:
  print("Odd")

# Task 3: Largest of three numbers

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))

print("Largest number is: ",max(a, b, c))

# Task 4: Prime Number Check

num = int(input("Enter a number : "))

if num < 2:
  print("Not Prime")
else:
  prime = True

for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print("Prime")
    else:
        print("Not Prime")
