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


