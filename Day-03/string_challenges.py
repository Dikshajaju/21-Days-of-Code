word = input("Enter a word: ")

# Palindrome
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# Vowel Count
vowels = "aeiouAEIOU"
count = 0

for char in word:
    if char in vowels:
        count += 1

print("Vowel Count:", count)

# Reverse String
print("Reversed:", word[::-1])

# Character Frequency
print("\nCharacter Frequency:")

for char in set(word):
    print(char, "=", word.count(char))
