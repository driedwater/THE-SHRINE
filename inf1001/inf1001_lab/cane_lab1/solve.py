data = open('testfile1_Sep2024', 'rb').read()

for char in data:
    print(chr(char & 0b01111111), end='')

