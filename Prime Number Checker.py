num = int(input())
if num <= 1:
    result = False
else:
    result = True
for i in range(2, num):
    if num % i == 0:
        result = False
        break
print(result)
