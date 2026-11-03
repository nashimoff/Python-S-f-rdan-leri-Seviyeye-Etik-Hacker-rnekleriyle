name = input("Enter name: ")
print("Welcome " + name + " time to play hangman")

secret_word = "Metallica"

lives = 10

while lives > 0:

    guess = input("Guess a letter: ")

    if guess in secret_word:
