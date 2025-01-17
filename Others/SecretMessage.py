import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

x = input("""\nModes:
    1 - Encode
    2 - Decode
 
Choice --> """)

while True:
    if x == "1":
        # ENCRYPTION
        plain_text = input("\nEnter a message to encrypt: ")
        cipher_text = ""

        for letter in plain_text:
            index = chars.index(letter)
            cipher_text += key[index]

        print("-------------------------------------")
        print(f"\nOriginal  message : {plain_text}")
        print(f"\nEncrypted message : {cipher_text}\n")
        print("-------------------------------------")

        break

    elif x == "2":
        # DECRYPTION
        cipher_text = input("\nEnter a message to decrypt: ")
        plain_text = ""

        for letter in cipher_text:
            index = key.index(letter)
            plain_text += chars[index]

        print("-------------------------------------")
        print(f"\nOriginal  message : {cipher_text}")
        print(f"\nDecrypted message : {plain_text}\n")
        print("-------------------------------------")

        break
