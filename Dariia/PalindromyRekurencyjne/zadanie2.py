def is_palindrome(integer):
    if len(integer) < 1:
        return True
    else:
        if integer[0] == integer[-1]:
            return is_palindrome(integer[1:-1])
        else:
            return False
a = str(input())
a = a.replace(' ', '')
if (is_palindrome(a) == True):
    print("Jest palindrom!")
else:
    print("Nie jest palindrom!")
