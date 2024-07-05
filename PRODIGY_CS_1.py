def caesar_cipher(text, shift, option):
    result = ""
    
    for char in text:
        if char.isalpha():
            if option == 'encrypt':
                if char.isupper():
                    result += chr((ord(char) - 65 + shift) % 26 + 65)
                else:
                    result += chr((ord(char) - 97 + shift) % 26 + 97)
            elif option == 'decrypt':
                if char.isupper():
                    result += chr((ord(char) - 65 - shift) % 26 + 65)
                else:
                    result += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            result += char
    
    return result

text = input("Enter the message to encrypt or decrypt: ").strip()
shift = int(input("Enter the shift value: "))
option = input("Enter 'encrypt' or 'decrypt': ").lower()

result = caesar_cipher(text, shift, option)
print("Result:", result)
