import random
import string

s1 = string.ascii_letters
s2 = string.digits
s3 = string.punctuation
s = s1 + s2 + s3
password = ""

for i in range(5):
    p = random.choice(s)
    password = password + p

print(f"Новый пароль [{i}]: {password}")
