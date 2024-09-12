import itertools
import string
import os
import sys
import time
def animated(text):
     for x in text:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.05)
logo ='''

██████╗ ██████╗ ██╗   ██╗████████╗███████╗██╗  ██╗
██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝╚██╗██╔╝
██████╔╝██████╔╝██║   ██║   ██║   █████╗   ╚███╔╝
██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝   ██╔██╗
██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗██╔╝ ██╗
╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝

'''
animated(logo)
print('           »»»Coder_By_White_Devil««« ')

def brute_force_password(target_password):
    # Define the character set to use in password guesses
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    max_length = 4  # Set a maximum length for the password guesses

    # Iterate over all possible combinations of characters
    for length in range(1, max_length + 1):
        for guess in itertools.product(characters, repeat=length):
            guess_password = ''.join(guess)
            if guess_password == target_password:
                return guess_password
    return None

# Example usage
target_password = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 1234567890 abcdefghijklmnopqrstuvwxyz ,*@#"  # The password we are trying to crack
cracked_password = brute_force_password(target_password)

if cracked_password:
    print(f"Password cracked: {cracked_password}")
else:
    print("Password not found.")

