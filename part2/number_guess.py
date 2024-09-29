import random

first = 1
second = 99

guess = random.randint(first,second)
print(guess)
answer = input()

while answer != 'd':
    if answer == 'k':
        second = guess
        guess = random.randint(first,second)
        print(guess)
        answer = input()
    elif answer == 'b':
        first = guess
        guess = random.randint(first,second)
        print(guess)
        answer = input()
