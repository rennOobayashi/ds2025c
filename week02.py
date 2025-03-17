import time
import random

random.seed(time.time())

random_a = random.randint(1, 100) + 1

print("Random Integer")

for i in range(7, 0, -1):
    inp = int(input(f"Enter Answer(remain: {i}): "))

    if inp > random_a :
        print("down")
    elif inp < random_a:
        print("up")
    else:
        print("You win!")
        break

    if i <= 1:
        print("You lose!")