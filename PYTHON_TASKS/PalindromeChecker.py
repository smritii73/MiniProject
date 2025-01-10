def is_palindrome(s):
    normalized = ''.join(char.lower() for char in s if char.isalnum())
    return normalized == normalized[::-1]
if __name__ == "__main__":
    test_string = input("Enter a string to check if it is a palindrome: ")
    if is_palindrome(test_string):
        print(f'"{test_string}" -> Palindrome')
    else:
        print(f'"{test_string}" -> Not a Palindrome')