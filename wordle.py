import random
from words import words
from display_utility import green, yellow, grey

def check_word(secret, guess):
    """This function compares a guessed word (guess) with the secret word (secret) and returns a list. The list containing green if the letter is correct and in the right place, yellow if the letter is correct but in the wrong place, and grey if the letter is incorrect."""
    secret = secret.upper()
    guess = guess.upper()

    result = []
    for _ in range(len(secret)):
        result.append("grey")

    letters = {}
    for letter in secret:
        letters[letter] = letters.get(letter, 0) + 1
    
    for i in range(len(secret)):
        if guess[i] == secret[i]:
            result[i] = "green"
            letters[guess[i]] -= 1

    for i in range(len(secret)):
        if result[i] == "grey" and letters.get(guess[i], 0) > 0:
            result[i] = "yellow"
            letters[guess[i]] -= 1

    return result


def known_word(clues):
    """Returns the clues of the word pattern. Green letters are in their position and the correct letter and not known letters are returned as an underscore (_)"""

    word = ['_', '_', '_', '_', '_']

    for clue in clues:
        guessed_word = clue[0]
        feedback = clue[1]

        for i in range(5):
            if feedback[i] == "green":
                word[i] = guessed_word[i]
    
    result = ""
    for letter in word:
        result += letter
    return result


def no_letters(clues):
    """Returns a string containing letters that are not in the word or grey."""

    grey_letters = set()
    confirmed_letters = set()

    for clue in clues:
        guessed_word = clue[0]
        feedback = clue[1]

        for i in range(5):
            if feedback[i] == "grey":
                grey_letters.add(guessed_word[i])
            
            elif feedback[i] in ("green", "yellow"):
                confirmed_letters.add(guessed_word[i])

    final_letters = grey_letters - confirmed_letters

    result = ""
    for letter in sorted(final_letters):
        result += letter.upper()
    return result


def yes_letters(clues):
    """Returns green or yellow depending on if the letter is in the word."""

    green_letters = set()
    yellow_letters = set()

    for clue in clues:
        guessed_word = clue[0]
        feedback = clue[1]

        for i in range(5):
            if feedback[i] == "green":
                green_letters.add(guessed_word[i])
            
            elif feedback[i] == "yellow":
                yellow_letters.add(guessed_word[i])

    final_letters = green_letters.copy()
    final_letters.update(yellow_letters)

    result = ""
    for letter in sorted(final_letters):
        result += letter.upper()
    return result


if __name__ == "__main__":
    secret = random.choice(words).upper()
    clues = []
    attempts = 6

    print("Known:", known_word(clues))
    print("Green Letters/Yellow Letters:", yes_letters(clues))
    print("Grey Letters:", no_letters(clues))

    while attempts > 0:
        guess = input("> ").upper()

        if len(guess) != 5:
            print("Word must be 5 letters long")
            continue        
        elif guess.lower() not in words:
            print("Invalid word")
            continue        

        feedback = check_word(secret, guess)
        clues.append((guess, feedback))

        for past_guess, past_feedback in clues:
            for i in range(5):
                if past_feedback[i] == "green":
                    green(past_guess[i])
                elif past_feedback[i] == "yellow":
                    yellow(past_guess[i])
                else:
                    grey(past_guess[i])
            print()

        print("Known:", known_word(clues))
        print("Green Letters/Yellow Letters:", yes_letters(clues))
        print("Grey Letters:", no_letters(clues))        

        if guess == secret:
            print(f"Answer: {secret}")
            break

        attempts -=1

        if attempts == 0:
            print(f"\nYou ran out of attempts. The word was: {secret}.")