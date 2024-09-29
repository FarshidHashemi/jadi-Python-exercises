older = 0

while True:
    age = int(input())
    if age == -1 :
        break
    if age > older :
        older = age

print(older)
