# H A N G M A N
import random


words = ['python', 'java', 'kotlin', 'javascript']
print("H A N G M A N")
random.seed()
word = random.choice(words)
mask = list("-" * len(word))
unmask = ''.join(mask)
guessed = set()
lives = 0
english_lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
set_english_letters = set(list(english_lowercase_letters))
answer = ''
print('Type "play" to play the game, "exit" to quit: ')
answer = input()
if answer == "play":
    while lives < 8 and ''.join(mask) != word:
        print()
        unmask = ''.join(mask)
        print("".join(mask))
        letter = input("Input a letter: ")
        if len(letter) != 1:
            print("You should input a single letter")
            continue
        elif letter.lower() != letter or letter not in set_english_letters:
            print("Please enter a lowercase English letter")
            continue
        if letter in guessed:
            print("You've already guessed this letter")
            continue
            # lives += 1
        else:
            guessed.add(letter)
            # lives += 1
        # letter in set_english_letters:
        if letter in word:
            guessed.add(letter)
            idx = [i for i, ch in enumerate(word) if ch == letter]
            if len(idx) > 0:
                for j in idx:
                    mask[j] = letter
        elif letter not in word:
            print("That letter doesn't appear in the word")
            lives += 1


        # if unmask == mask:
    if "".join(mask) == word:
        print('You guessed the word!')
        print('You survived!')
    else:
        print('You lost!')
