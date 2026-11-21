import random

def display_hangman(wrong):
    stages = [
        """
         -----
         |   |
             |
             |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
             |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
         |   |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
        /|   |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
        /    |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
        / \\  |
             |
        =========
        """
    ]
    print(stages[wrong])


def load_words():
    try:
        with open("words.txt", "r", encoding="utf-8") as file:
            words = [
                word.strip().lower()
                for word in file.read().split()
                if word.strip().isalpha()
            ]
        if words:
            return words
    except FileNotFoundError:
        pass

    return [
        "python", "computer", "database", "programming",
        "keyboard", "college", "student"
    ]


def play_game():
    words = load_words()
    secret_word = random.choice(words)
    guessed_letters = set()
    wrong_attempts = 0
    max_attempts = 6

    print("WELCOME TO HANGMAN GAME!")
    print("Guess the hidden word letter by letter.")

    while wrong_attempts < max_attempts:
        display_hangman(wrong_attempts)

        display_word = " ".join(
            letter if letter in guessed_letters else "_"
            for letter in secret_word
        )

        print("\nWord:", display_word)
        print("Wrong attempts:", wrong_attempts, "/", max_attempts)

        if all(letter in guessed_letters for letter in secret_word):
            print("\nCONGRATULATIONS! YOU WON!")
            print("The word was:", secret_word)
            return

        guess = input("\nEnter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Correct guess!")
        else:
            wrong_attempts += 1
            print("Wrong guess!")

    display_hangman(wrong_attempts)
    print("\nGAME OVER! YOU LOST.")
    print("The correct word was:", secret_word)


if __name__ == "__main__":
    play_game()
