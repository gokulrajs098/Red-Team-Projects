
def main(text):
    cipher = ""
    for char in text:
        if char.islower():
            cipher += chr((ord(char) + 13 - 97) % 26 + 97 )

        elif char.isupper:
            cipher += chr((ord(char) + 13 - 65) % 26 + 65 )

        else:
            cipher += char
    print(cipher) 
    
text = input("Enter the text:")
main(text)