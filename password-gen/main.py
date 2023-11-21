import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_password_length():
    while True:
        try:
            length = int(input('Enter the desired password length: '))
            if length > 0:
                return length
            else:
                print('Password length must be a positive integer.')
        except ValueError:
            print('Invalid input. Please enter a valid integer.')

# Example usage:
password_length = get_password_length()
random_password = generate_password(password_length)
print(f'Random Password:\n{random_password}')
