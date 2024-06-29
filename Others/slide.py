import string
import time
import pyfiglet

banner = pyfiglet.figlet_format("SLIDE")
print(banner)


text = "Fuck Niggaz"
temp = ""

for ch in text:
    for i in string.printable:
        if i == ch or ch == string.whitespace:
            time.sleep(0.02)
            print(temp+i)
            temp += ch
            break
        else:
            time.sleep(0.02)
            print(temp+i)
            