secret = 42
attempts = 0
guess = 0

while guess != secret:
    guess = int(input("Guess a number between 1 and 100:"))
    attempts += 1

    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")

print("Correct! It took you " + str(attempts) + " attempts.")
