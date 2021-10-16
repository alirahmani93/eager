"""
from  tkinter import *

hangman = ['head','neck','left hand' ,'right hand' ,'left foot','right foot', 'die']

win = Tk()
win.title("Hang Man")

lab1=Label(win,text = "Lfe is short so play MORE")
lab2=Label(win,text= " Take care if you wrong he die if he die you loose")
def func1():
    b=bt1.getattr()
    if b==1: print('hi')
bt=Button(win,text= "submit",command=func1)
bt.config(fg = 'red',bg='green')

# Alpha bet BUTTON

bt1=Button(win,text= "A",command='yellow') ; bt1.pack()
bt2=Button(win,text= "B") ; bt2.pack()
bt3=Button(win,text= "C") ; bt3.pack()
bt4=Button(win,text= "D") ; bt4.pack()
bt5=Button(win,text= "E") ; bt5.pack()
bt6=Button(win,text= "F") ; bt6.pack()
bt7=Button(win,text= "G") ; bt7.pack()
bt8=Button(win,text= "H") ; bt8.pack()
bt9=Button(win,text= "I") ; bt9.pack()
bt10=Button(win,text= "J") ; bt10.pack()
bt11=Button(win,text= "K") ; bt11.pack()
bt12=Button(win,text= "L") ; bt12.pack()
bt13=Button(win,text= "M") ; bt13.pack()
bt14=Button(win,text= "N") ; bt14.pack()
bt15=Button(win,text= "O") ; bt15.pack()


#


en=Entry(win)
en.config(takefocus=
exam == en.get()
if exam =='salam':
    lab3=Label(win,text= 'yess')
else:
    lab3=Label(win,text= 'Hang the MAN')
    print(lab3)

lab1.pack()
lab2.pack()
bt1.pack()
en.pack()
"""


import random as rand

hangmanpic = ['head', 'neck', 'left hand', 'right hand', 'left foot', 'right foot', 'die']
wordlist = "edition ring product awarded museum innovation"


def getword(wordlist):
    rand_index = rand.randint(0, len(wordlist) - 1)
    return rand_index


def displayboard(hangmanpic, word, failed_guess, correct_guess):
    print(hangmanpic[len(failed_guess)])
    hidden = " !woow! " * len(word)
    curent_word = word
    for x in range(0, len(word)):
        if word[x] not in correct_guess:
            curent_word = curent_word.replace(word[x], " !woow! ")

    print(curent_word)


def main():
    print("HANG MAN")
    rand_index = getword(wordlist)
    word = str(wordlist[rand_index])
    failed_guess = 'NO'
    correct_guess = 'YES'
    displayboard(hangmanpic, word, failed_guess, correct_guess)
    guss = "_________"
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





