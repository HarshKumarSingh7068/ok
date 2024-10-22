#Problem: Reverse string
#Solution strategies: Two Pointers at same speed (p++ and q--)
#Efficiency: (0)n
def is_palindrome(sir):
    sir = ''.join(c for c in sir if c.isalnum()).lower()
    return sir == sir[::-1]
maam = input("Enter a string: ")
print(is_palindrome(maam))