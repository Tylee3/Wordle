import random
from words import words
from wordle import check_word
from display_utility import green, yellow, grey

def filter_word_list(words, clues):
    """Returns possible secret words from the filtered given list of words based on past clues."""
    
    possible_words = []

    for word in words:
        valid_word = True

        for guess, feedback in clues:
            if check_word(word, guess) != feedback:
                valid_word = False
                break
    
        if valid_word:
            possible_words.append(word)

    return possible_words


if __name__ == "__main__":
    secret = random.choice(words).upper()
    clues = []
    attempts = 6

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

        possible_words = filter_word_list(words, clues)
        print(len(possible_words), "words possible:")

        if possible_words:
            random_words = set()
            while len(random_words) < min(5, len(possible_words)):
                random_words.add(random.choice(possible_words))
            random_words = list(random_words)
        else:
            random_words = []
        
        for word in random_words:
            print(word.lower())
        
        if guess == secret:
            break

        attempts -=1

        if attempts == 0:
            print(f"\nYou ran out of attempts. The word was: {secret}.")