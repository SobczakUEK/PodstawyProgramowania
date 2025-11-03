def f(palindrome):
    text = palindrome
    return text == text[::-1]


print(f("radar"))
print(f("12-11-21"))
print(f("book"))
