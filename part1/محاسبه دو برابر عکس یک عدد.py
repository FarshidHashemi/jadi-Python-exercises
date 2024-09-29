num = int(input())
reverse_num = 0

while num > 0:
    temp = num % 10
    reverse_num = reverse_num * 10 + temp
    num = num // 10
multiply = reverse_num * 2
print(multiply)
