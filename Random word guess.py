import random as rnd 

all_words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'kavya', 'education', 'python', 'programming', 'development']

word = rnd.choice(all_words)
guessedWord = ['_'] * len(word)
attempt = 10

while attempt > 0:
    print("\nCurrent word: " + " ".join(guessedWord))
    guess = input("Guess a letter: ").lower()
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
        print("Correct guess!")
    else:
        attempt -= 1
        print(f"Wrong guess! Attempts left: {attempt}")
    if '_' not in guessedWord:
        print("\nCongratulations! You've guessed the word: " + word)
        break

if attempt == 0 and '_' in guessedWord:
    print("\nSorry, you've run out of attempts. The word was: " + word)