import random

secret = random.randint(1, 30)
count = 0
low_score = 0

with open("score.txt", "r") as score:
    low_score = int(score.read())
    print("The minimum number of guesses so far was: {0}".format(low_score))

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    count += 1

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret) + "!")
        print("You have guessed {0} times.".format(count))
        if count < low_score:
            print("Congratulation! You have reached a new low-score")
            with open("score.txt", "w") as score:
                score.write(str(count))
        break
    elif guess < secret:
        print("Sorry, your guess is too small... The secret number is not " + str(guess))
    else:
        print("Sorry, your guess is too big... The secret number is not " + str(guess))
