def remove_char(string, char_to_remove):
    string = string.replace(char_to_remove, '')
    return string


x = input("Enter a word/sentence: ")
y = input("Enter a char to remove from it: ")
z = remove_char(x, y)
print("Before changing:", x)
print("After changing:", z)
