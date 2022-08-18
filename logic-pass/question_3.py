def count_of_char_in_string(string, char):
    if len(char) > 1:
        return "char length more than 1"
    count = 0
    for i in range(len(string)):
        if string[i] == char:
            count += 1
    return count


x = input("Enter a string: ")
y = input("Enter a char to count it's occurrence in the string: ")
z = count_of_char_in_string(x, y)
print(z)
