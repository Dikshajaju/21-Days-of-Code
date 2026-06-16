# Day 02 - Array Warrior

numbers = [12, 45, 7, 89, 23]

# Largest Number
print("Largest Number:", max(numbers))

# Smallest Number
print("Smallest Number:", min(numbers))

# Sum of Elements
print("Sum:", sum(numbers))

# Count Even Numbers
count = 0

for num in numbers:
    if num % 2 == 0:
        count += 1

print("Even Numbers Count:", count)

# Reverse the List
reversed_list = numbers[::-1]

print("Reversed List:", reversed_list)
