##GUESSING GAME FOR FUN!!
import random
randomNum = random.randint(1, 100)
userGuess = None
guess = 0

while(userGuess != randomNum):
    userGuess = int(input('Guess a number less than 100: '))
    guess += 1
    if userGuess == randomNum:
        print('Congrats.Your guess is right')

    else:
        if (userGuess > randomNum):
            print('You guessed it wrong! Enter a smaller number')
        else:
            print('You guessed it wrong! Enter a larger number')


print(f'You guessed the number in {guess} gueses!')
with open('highscore.txt') as f:
    highScore = int(f.read())

if guess < highScore:
    with open('highscore.txt', 'w') as f:
        f.write(str(guess))