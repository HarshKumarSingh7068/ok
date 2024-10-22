#Problem: Valid palindrome
#Solution strategies: Two Pointers at same speed (p++ and q--)
#Efficiency: (0)n
def Is_palindrome(jeher):
    jeher = ''.join(c for c in jeher if c.isalnum()).lower()
    p=0
    q = len(jeher) - 1
    while (p < q):
        if (jeher[p] != jeher[q]):
            return False
        else:
            p = p + 1
            q = q - 1
            return True
Beniwal = input("Enter your string: ")
print(Is_palindrome(Beniwal))