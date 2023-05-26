strings=int(input())
for i in range(strings):
    text=input()
    if ','in text or '.' in text or '_' in text:
        print(f'{text} is not pure!')
    else:
        print(f'{text} is pure.')