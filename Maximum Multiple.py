devisor=int(input())#Делител
boundery=int(input())#Делимо
for number in range(boundery,devisor-1,-1):
    if number%devisor==0:#Проверка дали числото е четно
        break
print(number)