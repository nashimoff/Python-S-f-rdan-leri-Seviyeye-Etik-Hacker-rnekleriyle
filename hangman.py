name = input("Enter name: ")
print("Welcome " + name + " time to play hangman")

secret_word = "Metallica"

lives = 10

while lives > 0:

    for character in secret_word:
        print(character)
        if guess == "a":
            print("a")

    guess = input("Guess a letter: ")

    if guess not in secret_word:
        lives -= 10
        print("Wrong guess!")
        print(f"You have {lives} left")

        if lives == 0:
            print("You died!")
