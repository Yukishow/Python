n = int(input())
for i in range(n):
    number = input()
    result = 1
    for j in range(len(number)):
        result *= int(number[j])
    print(result)