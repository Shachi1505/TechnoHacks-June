import string
import random
def gen_pass(length, use_special_char=False):
    chars = string.ascii_letters + string.digits
    if use_special_char:
        chars += string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password
def main():
    print("Welcome to Password Generator")
    try:
        length = int(input("Enter desired length of password "))
        use_special_chars = input("Include special chars? yes/no ").lower()=='yes'
        if length<=0:
            print("password length should be a positive number!")
        else:
            password = gen_pass(length, use_special_chars)
            print("Your generated password=", password)
    except ValueError:
        print("Invalid Input")
if __name__=="__main__":
    main()