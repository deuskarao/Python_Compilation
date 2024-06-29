import random
import string
from time import sleep

class PasswordGenerator:
    def __init__(self):
        self.chars_ = []
        self.key = ""
        self.length = 0

    def add_to_chars(self):
        self.chars_ = ["*", "!", "_", "-", ".", "?", "%", "&", "+"]
        for value in range(97, 123):
            self.chars_.append(value)

        for value in range(97, 123):
            self.chars_.append(str(value).capitalize())

        for nums in range(0, 10):
            self.chars_.append(nums)

    def generate(self):
        print("******** Generator Started ********")

        # get_chars = input("Do you want specific characters in your Password ? ""Ex: 1-2-a-b-D-c: ")
        key_len = int(input("Password Length: "))
        length = key_len

        while len(self.key) < length:
            char = random.choice(self.chars_)
            self.key += str(char)

            if len(self.key) == length:
                break

        with open("passwd.txt", "a") as txt:
            txt.write(self.key)

        self.verify(self.key)
        self.julius(self.key)


    def verify(self, passwd):
        try:
            if not 8 <= len(passwd) <= 24:
                print("\nLength     : x")
                sleep(1)
                print("Characters : ✓")
                sleep(1)
                print("Strong     : x\n")
                sleep(1)

                while len(passwd) < 12:
                    passwd += random.choice(self.chars_)
                    if len(passwd) == 12:
                        break

                print("Stronger version  : " + passwd)

            else:
                print("\nLength     : ✓")
                sleep(1)
                print("Characters : ✓")
                sleep(1)
                print("Strong     : ✓\n")
                sleep(1)

        except:
            print("Verify function doesn't work!")


    def julius(self, text, shift=7, alphabets=None):
        text = self.key
        if alphabets is None:
            alphabets = [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]

        def shift_alphabet(alphabet):
            return alphabet[shift:] + alphabet[:shift]

        shifted_alphabets = tuple(map(shift_alphabet, alphabets))
        final_alphabet = ''.join(alphabets)
        final_shifted_alphabet = ''.join(shifted_alphabets)
        table = str.maketrans(final_alphabet, final_shifted_alphabet)
        print("\nPassword         : " + self.key)
        sleep(1)
        print("Password (Caesar): " + text.translate(table))
        sleep(1)
        

    def starter(self):
        while True:
            mode = input("""
======== Mode ========
1 - Generate
2 - Check

|> """)
            print("-" * 25 + "\n")

            if mode == "1":
                self.generate()

            elif mode == "2":
                print("******** Verifier Started ********")
                password = input("\nPassword to check: ")
                self.verify(password)

            elif mode not in ["1", "2"]:
                print("\nChoose between 1 - 2 !")


if __name__ == "__main__":
    start = PasswordGenerator()
    try:
        start.add_to_chars()
        start.starter()

    except KeyboardInterrupt:
        print("Exiting..")
        exit()
