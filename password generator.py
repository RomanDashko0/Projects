from random import choice
import string

def generate_password(length):
    chars = string.ascii_letters + string.digits
    password = ""

    for i in range(length):
        password += choice(chars)

    return password

length = int(input("Type your password's length"))
password = generate_password(length)
print("Your generated password:", password)

