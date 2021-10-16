
import random as rand

hangmanpic = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''','''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
   \  |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
wordlist = "edition ring product awarded museum innovation".split()


def getword(wordlist):
    rand_index = rand.randint(0, len(wordlist) - 1)
    return rand_index


def displayboard(hangmanpic, word, failed_guess, correct_guess):
    print(hangmanpic[len(failed_guess)])
    hidden = " ___ " * len(word)
    curent_word = word
    for x in range(0, len(word)):
        if word[x] not in correct_guess:
            curent_word = curent_word.replace(word[x], " __ ")

    print(curent_word)


def main():
    print("HANG MAN")
    rand_index = getword(wordlist)
    word = str(wordlist[rand_index])
    failed_guess = 'NO'
    correct_guess = 'YES'
    displayboard(hangmanpic, word, failed_guess, correct_guess)
    guess = "_________"
    playAgain = "yes"
    while (True):
        guess = str(input('enter your guess: '))
        while (len(guess) != 1 or (guess.isalpha() == False)):
            gues = str(input("invalid,enter a single letter: "))
        if (len(failed_guess) >= 5):
            displayboard(hangmanpic, word, failed_guess, correct_guess)
            print("you loose", "The correct word is {}".fomat(word))
            playAgain = str(input("play again? Y or N: "))
            if playAgain != "yes":
                quit()
            else:
                main()
        elif (guess in word):
            correct_guess += guess
            displayboard(hangmanpic, word, failed_guess, correct_guess)
        else:
            failed_guess += guess
            displayboard(hangmanpic, word, failed_guess, correct_guess)
main()
