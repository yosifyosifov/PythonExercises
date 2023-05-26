while True:
    string = input()

    if string == "End":
        break

    if string == "SoftUni":
        continue

    doubled_string = ""
    for char in string:
        doubled_string += char * 2

    print(doubled_string)
