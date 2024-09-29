sum = 0
win = 0

for i in range(0, 30):
    score = int(input())
    sum += score
    if score == 3:
        win += 1

print(sum,'', win)
