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


/////////////////////////////////////////////////////////////////////////////////
#Problem: Reverse string
#Solution strategies: Two Pointers at same speed (p++ and q--)
#Efficiency: (0)n
def is_palindrome(sir):
    sir = ''.join(c for c in sir if c.isalnum()).lower()
    return sir == sir[::-1]
maam = input("Enter a string: ")
print(is_palindrome(maam))


/////////////////////////////////////////////////////////////////////////////////
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

/////////////////////////////////////////////////////////////////////////////////////

#Problem: Reverse only words
#Solution strategies: Two Pointers at same speed (p++ and q--)
#Efficiency: (0)n
def reverse_only_letters(s1):
    s1 = list(s1)
    p=0
    q = len(s1) - 1
    while (p < q):
        if (not s1[p].isalpha()):
            p = p + 1
        elif (not s1[q].isalpha()):
            q = q - 1
        else:
            s1[p], s1[q] = s1[q], s1[p]
            p = p + 1
            q = q - 1
    return "".join(s1)
kya_Karu= input("Enter a string: ")
print("Reversed Letters: ", reverse_only_letters(kya_Karu))


