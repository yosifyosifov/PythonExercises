def is_special_number(num):
    # Пресмятаме сумата от цифрите на числото
    digit_sum = sum(int(digit) for digit in str(num))

    # Проверяваме дали сумата е 5, 7 или 11
    if digit_sum == 5 or digit_sum == 7 or digit_sum == 11:
        return True
    else:
        return False


# Четем входа от потребителя
n = int(input())

# Итерираме през числата от 1 до n и проверяваме дали са специални
for num in range(1, n + 1):
    special = is_special_number(num)
    print(f"{num} -> {special}")


