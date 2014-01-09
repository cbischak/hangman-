import random
import pygame

size = (700, 500)
screen = pygame.display.set_mode(size)

words = word_file = "/usr/share/dict/words"
WORDS = open(word_file).read().splitlines()

def getRandomWord(wordlist):

    wordIndex = random.randint(0, len(wordlist)-1)
    return wordlist[wordIndex]

def displayBoard(HANGMANPICS, missedletters, correctletters, secretword):
    print(HANGMANPICS[len(missedletters)])
    print()

    print("Missed Letters:", end = '')
    for letter in missedletters:
        print(letter, end ='' )
    print()

    blanks = '' * len(secretword)

    for i in range (len(secretword)):
        if secretword[i] in correctletters:
            blanks = blanks [:i] + secretword [i] + blanks[i+1:]

    for letter in blanks:

        print(letter, end = '')
    print()

def getGuess(alreadyguessed):

    while True:
        print("Guess a letter.")
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print("Please enter a single letter")
        elif guess in alreadyguessed:
            print("You have already guessed that letter. Choose again.")

        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
                print("Please enter a letter.")

        else:
            return guess

def playagain():

    print("Do you want to play again? (yes or no)")
    return input().lower().startswith('y')

print("HANGMAN")
missedletters = ''
correctletters = ''
secretword = getRandomWord(words)
gameisdone = False

while True:
    displayBoard(HANGMANPICS, missedletters, correctletters, secretword)

    guess = getGuess(missedletters + correctletters)

    if guess in secretword:
        correctletters = correctletters + guess

        foundAllLetters = True

        for i in range (len(secretword)):
            if secretword[i] not in correctletters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print("You have won, the secret word is " + secretword)

            gameisdone = True

    else:
        missedletters = missedletters + guess

        if len(missedletters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedletters, correctletters, secretword)

            print('''You have run out of guess!\nAfter
                  + str(len(missedletters)) + "correct guesses, and the word was "' + secretword + '"')
                  + 'missed guesses and ' + str(len(correctletters)) + 'correct guesses, the word was"' + secretword + ''')
            gameisdone = True

    if gameisdone:
        if playagain():
            missedletters = ''
            correctletters = ''
            gameisdone = False
            secretword = getRandomWord(words)
    else:
        break