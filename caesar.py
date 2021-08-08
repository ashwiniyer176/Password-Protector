string = "Ashwiniyer@_!-176"
s = ""

for char in string:
    char = chr(ord(char)+2)
    s += char
    print(char)
print(s)

for char in s:
    char = chr(ord(char)-2)
    print(char)
