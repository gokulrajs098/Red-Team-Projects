def main(text, key):
    
    cipher = ""
    for char in text:
        
        if char.islower():
            cipher += chr((ord(char) + key - 97) % 26 + 97)

        elif char.isupper():
            cipher += chr((ord(char) + key -65) % 26 + 65)

        else:
            cipher += char
    print(cipher)

text = input("Enter the word:")
key = int(input("Enter the key:"))

main(text, key)