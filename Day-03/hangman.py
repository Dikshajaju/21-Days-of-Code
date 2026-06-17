word = "python"

guessed = ["_"] * len(word)

attempts = 6

while attempts > 0 and "_" in guessed:

    print("\nWord:", " ".join(guessed))
    guess = input("Guess a letter: ").lower()

    if guess in word:

        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess

    else:
        attempts -= 1
        print("Wrong Guess!")
        print("Attempts Left:", attempts)

if "_" not in guessed:
    print("\nCongratulations! You won.")
else:
    print("\nGame Over.")
    print("Word was:", word)
