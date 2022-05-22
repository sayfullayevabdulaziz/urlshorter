import random
import string # ascii_lowercase, ascii_uppercase


def generate_token(length=5, has_digits=True):
    token = ''.join(
        random.choice(list(string.ascii_letters + string.digits)) for i in range(length)
     )
    # print(token)
    # if has_digits and token.isalpha():
    #     token[random.randint(0, length)] = str(random.randint(0, 9))
    return token
# print(string.ascii_letters)
