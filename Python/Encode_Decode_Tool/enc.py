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
        def encrypt(message):
            message = message.lower()
            newString = ''
            validLetters = "abcdefghijklmnopqrstuvwxyz " #adding whitespace to valid chars...
            space = []
            for char in message:
                if char in validLetters or char in space:
                    newString += char
            shift = int(input("Please enter your shift : "))
            resulta = []
            for ch in newString:
                x = ord(ch)
                x = x+shift
                # special case for whitespace...
                resulta.append(chr(x if 97 <= x <= 122 else 96+x%122) if ch != ' ' else ch)
            print(''.join(resulta))
        
        def decrypt(message):
            shift = int(input('Please enter its shift value: '))
            space = []

            # creat a list of encrypted words.
            message = message.split()

            # creat a list to hold decrypted words.
            sentence = []

            for word in message:
                cipher_ords = [ord(x) for x in word]
                plaintext_ords = [o - shift for o in cipher_ords]
                plaintext_chars = [chr(i) for i in plaintext_ords]
                plaintext = ''.join(plaintext_chars)
                sentence.append(plaintext)

            # join each word in the sentence list back together by a space.
            sentence = ' '.join(sentence)
            print('Your encrypted sentence is:', sentence)

        if choice == 'e':
            encrypt(message)
        elif choice == 'd':
            decrypt(message)
    break

