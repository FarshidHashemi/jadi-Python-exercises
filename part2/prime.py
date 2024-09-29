number = int(input())
cnt = 0

for i in range(1, number):
    if number % i == 0:
        cnt += 1

if cnt == 1:
    print("prime")
else:
    print("not prime")
