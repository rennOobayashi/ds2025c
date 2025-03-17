import time
import random

random.seed(time.time())

random_a = random.randint(1, 100) + 1

print("~Random Integer~")

for i in range(7, 0, -1):
    guess = int(input(f"Enter Answer(remain: {i}): "))

    if guess > random_a and i > 1:
        print("down")
    elif guess < random_a and i > 1:
        print("up")
    elif i <= 1:
        print(f"You lose! (answer is {random_a})")
    else:
        print("You win!")
        break
