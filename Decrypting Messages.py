def decrypt_message(key, n, lines):
    decrypted_message = ""

    for line in lines:
        decrypted_line = ""

        for char in line:
            # Check if the character is a lowercase letter
            if char.islower():
                decrypted_char = chr((ord(char) - ord('a') + key) % 26 + ord('a'))
            # Check if the character is an uppercase letter
            elif char.isupper():
                decrypted_char = chr((ord(char) - ord('A') + key) % 26 + ord('A'))
            else:
                decrypted_char = char

            decrypted_line += decrypted_char

        decrypted_message += decrypted_line

    return decrypted_message


# Example usage
key = int(input())  # Read the key from input
n = int(input())  # Read the number of lines from input
lines = [input() for _ in range(n)]  # Read the lines from input

result = decrypt_message(key, n, lines)
print(result)
