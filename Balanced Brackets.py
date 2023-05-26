def check_balanced_parentheses(n, lines):
    stack = []

    for line in lines:
        if line == '(':
            if len(stack) > 0 and stack[-1] == '(':
                return "UNBALANCED"
            stack.append(line)
        elif line == ')':
            if len(stack) == 0 or stack[-1] != '(':
                return "UNBALANCED"
            stack.pop()

    if len(stack) == 0:
        return "BALANCED"
    else:
        return "UNBALANCED"


# Example usage
n = int(input())  # Read the number of lines from input
lines = [input() for _ in range(n)]  # Read the lines from input

result = check_balanced_parentheses(n, lines)
print(result)

