import random

random_number = random.randint(1,21)
guess = 0

while guess != random_number:
    guess = int(input("Please choose a number between 1-20: "))

    if guess > random_number:
        print("You must make a lower guess.")
    
    else:
        print("You must make a higher guess.")

print(f"Congrats! You've guessed the number {random_number} correctly.")