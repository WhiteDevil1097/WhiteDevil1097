import itertools
import string
import time
import colorama
from colorama import Fore,Style

# some decorations for giving it a good look and feel.
colorama.init()
print(Fore.RED + Style.BRIGHT)
print()

def brute_force(password_length, charset):
    """
    Attempts to guess a password by trying all possible combinations of characters.

    Args:
        password_length (int): The length of the password to guess.
        charset (str): The character set to use for the brute force attack.

    Returns:
        str: The guessed password.
    """
    start_time = time.time()
    attempts = 0

    for attempt in itertools.product(charset, repeat=password_length):
        attempts += 1
        password = ''.join(attempt)
        print(f"Attempt {attempts}: {password}")

        # Replace this with your own password checking logic
        if password == "/data/data/com.termux/files/home/Brute-force/file.txt":
            end_time = time.time()
            print(f"Password found: {password}")
            print(f"Time taken: {end_time - start_time} seconds")
            print(f"Attempts: {attempts}")
            return password

    print("Password not found.")
    return None

# Example usage:
charset = string.ascii_letters + string.digits + string.punctuation
password_length = 12
brute_force(password_length, charset)
