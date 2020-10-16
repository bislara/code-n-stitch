import base64
import binascii
from morse3 import Morse as m

message = input("Please enter the text you would like to encrypt or decrypt: ")
option = input("Please select the method you'd like to use: base64/morse/hex/caesar cipher: ")
choice = input("Would you like to encrypt or decrypt(e/d): ")
while option == 'base64' or option == 'morse' or option == 'hex' or option == 'caesar cipher':
    if option == 'base64':
        if choice == 'e':
            message_bytes = message.encode('ascii')
            base64_bytes = base64.b64encode(message_bytes)
            base64_message = base64_bytes.decode('ascii')
            print("Encrypted Message: " + base64_message)
        if choice == 'd':
            base64_bytes = message.encode('ascii')
            message_bytes=base64.b64decode(base64_bytes)
            message = message_bytes.decode('ascii')
            print("Decrypted Message: " + message)
        else:
            raise Exception("Invalid choice. ")


    if option == 'morse':
        if choice == 'e':
            print(m(message).stringToMorse())
        if choice == 'd':
            print(m(message).morseToString())

    if option == 'hex':
        if choice == 'e':
            print(message.encode("utf-8").hex())
        if choice == 'd':
            print(bytes.fromhex(message).decode('utf-8'))
    if option == 'caesar cipher':
        def encrypt(message,s):
            s = int(input("Please enter the shift number you'd like (Exmaple: 4): "))
            result = ""
            # transverse the plain text
            for i in range(len(message)):
                char = message[i]
                # Encrypt uppercase characters in plain text
                
                if (char.isupper()):
                    result += chr((ord(char) + s-65) % 26 + 65)
                # Encrypt lowercase characters in plain text
                else:
                    result += chr((ord(char) + s - 97) % 26 + 97)
            print(result)
        '''
        def decrypt(message):
            LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            for key in range(len(LETTERS)):
                translated = ''
                for symbol in message:
                    if symbol in LETTERS:
                        num = LETTERS.find(symbol)
                        num = num - key
                        if num < 0:
                            num = num + len(LETTERS)
                        translated = translated + LETTERS[num]
                    else:
                        translated = translated + symbol
                print('Hacking key #%s: %s' % (key, translated))
        '''
        if choice == 'e':
            encrypt(message)
        '''elif choice == 'd':
            decrypt(message)'''
    break

