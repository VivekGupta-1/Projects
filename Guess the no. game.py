# create a random number between 1 and 50
random_number = random.randint(1, 50)

# function to check if the user's guess is right or wrong
def check_guess(guess, target):
    if guess < target:
        print("Too low! Try guessing a higher number.")
        return False
    elif guess > target:
        print("Too high! Try guessing a lower number.")
        return False
    else:
        print("Congratulations! You guessed the correct number.")
        return True

# game loop with 5 attempts limit
attempts = 5
while attempts > 0:
    user_guess = input(f"Guess a number between 1 and 50 (Attempts left: {attempts}): ")

    # Checking if the input is a valid number
    try:
        user_guess = int(user_guess)
    except ValueError:
        print("Please enter a valid number.")
        continue

    # Checking if the guess is correct
    if check_guess(user_guess, random_number):
        break

    attempts -= 1

# Informing the user if they have used all their attempts
if attempts == 0:
    print(f"Sorry, you have used all your attempts. The correct number was {random_number}.")ing