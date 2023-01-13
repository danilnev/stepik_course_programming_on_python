n = int(input())
values = dict()
for i in range(n):
    num = int(input())
    if num in values:
        print(values[num])
    else:
        result = f(num)
        print(result)
        values[num] = result
