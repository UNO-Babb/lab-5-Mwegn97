import random

def inWord(letter, word):
    if word.find(letter) >= 0:
        return True
    else:
        return False

def atSpot(letter, word, spot):
    if word[spot] == letter:
        return True
    else:
        return False
    
def checkWord(word, guess):
    feedback = ""
    spot = 0
    for letter in guess:
        if atSpot(letter, word, spot) == True:
            feedback = feedback + letter.upper()
        elif inWord(letter, word) == True:
            feedback = feedback + letter.lower()
        else:
            feedback = feedback + "*"
        spot = spot + 1
    return feedback

def main():
    wordFile = open("words.txt", 'r')
    content = wordFile.read()
    wordList = content.split("\n")
    todayWord = random.choice(wordList)
    print(todayWord)

    wordLength = len(todayWord)

    print("Welcome to the Word Game!")
    print(f"Guess the {wordLength}-letter word. You have 6 tries.")

    guessCorrect = False

    for attempt in range(6):
        guess = input(f"Guess #{attempt + 1}: ").lower()

        if len(guess) != wordLength:
            print(f"Please enter a {wordLength}-letter word.")
        else:
            feedback = checkWord(todayWord, guess)
            print("Result:", feedback)
            
            if guess == todayWord:
                print("You guessed the word!")
                guessCorrect = True
                break

    if not guessCorrect:
        print(f"You are out of guesses. The word was: {todayWord}")

if __name__ == '__main__':
  main()