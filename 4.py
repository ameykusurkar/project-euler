from itertools import combinations

def all_palindromes(limit):
    return [x * y
            for x, y in combinations(range(limit), 2)
            if is_palindrome(x * y)]

def is_palindrome(n):
    return int("".join(reversed(str(n)))) == n

print(max(all_palindromes(1000)))
