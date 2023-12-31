import string, random
def generate_password(length):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(all_chars) for i in range(length))
    return password
password = generate_password(10)
print(password)
def password_checker(password):
    min_length = 8
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special_char = False
    special_chars = "!@#$%^&*()-_=+[{]}\|;:',<.>/?"
    if len(password) < min_length:
        print("Password is too short!")
        return False
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special_char = True
    if not has_uppercase:
        print("Password must contain at least one uppercase letter!")
        return False
    if not has_lowercase:
        print("Password must contain at least one lowercase letter!")
        return False
    if not has_digit:
        print("Password must contain at least one digit!")
        return False
    if not has_special_char:
        print("Password must contain at least one special character!")
        return False
    print("Password is strong!")
    return True
word = password
password_checker(word)
