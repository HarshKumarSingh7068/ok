#Problem: Reverse string
#Solution strategies: Two Pointers at same speed (p++ and q--)
#Efficiency: (0)n
def reverse_vowels(s):
    vowels ="aeiouAEIOU"
    s = list(s)
    p = 0
    q = len(s) - 1
    while (p < q):
        if (s[p] not in vowels):
            p += 1
        elif(s[q] not in vowels):
            q -= 1
        else:
            s[p], s[q] = s[q], s[p]
            p += 1
            q -= 1
    return "".join(s)
str = input("Enter a string: ")
print("Reversed Vowels:", reverse_vowels(str))

