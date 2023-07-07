import random
import string
import time
import termcolor


def generate_password(length=10):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

print("Please type the lenght of the password:",)
psw_lenght = int(input())
print("Generating password...")
time.sleep(0.5)
psw = generate_password(psw_lenght)
print("Your password is : " + " "+termcolor.colored(psw, 'green'))



