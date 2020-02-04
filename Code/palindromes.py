#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # implement the is_palindrome function iteratively here
    '''
    Best time complexity -- O(1), text is either empty or contains one character
    Average time complexity -- O(n/2), text is palindrome
    '''
    text_lowercase = text.lower()
    left_index = 0
    right_index = len(text) - 1
    while left_index < right_index:
        if not text_lowercase[left_index].isalpha():
            left_index += 1
            continue
        if not text_lowercase[right_index].isalpha():
            right_index -= 1
            continue
        if text_lowercase[left_index] == text_lowercase[right_index]:
            left_index += 1
            right_index -= 1
        else:
            return False
    return True

    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests


def is_palindrome_recursive(text, left=None, right=None):
    # implement the is_palindrome function recursively here
    '''
    Best time complexity -- O(1), text is either empty or contains one character
    Average time complexity -- O(n/2), text is palindrome
    '''
    if left is None or right is None:
        left = 0
        right = len(text) - 1
    text_lowercase = text.lower()
    if left > right:
        return True
    if not text_lowercase[left].isalpha():
        return is_palindrome_recursive(text, left + 1, right)
    if not text_lowercase[right].isalpha():
        return is_palindrome_recursive(text, left, right - 1)
    if text_lowercase[left] == text_lowercase[right]:
        return is_palindrome_recursive(text, left + 1, right - 1)
    else:
        return False

    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your recursive implementation passes all tests


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
