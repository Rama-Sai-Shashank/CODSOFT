import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    char_pool = ''
    if use_letters:
        char_pool += string.ascii_letters
    if use_numbers:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation

    if not char_pool:
        raise ValueError("No character types selected. Please select at least one character type.")
    
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the length of the password: "))
        use_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
