# Given two letters extract common letters from there

letter1 = input("Enter string 1: ")
letter2 = input("Enter string 2: ")
s1 = set(letter1)
s2 = set(letter2)
print(s1 & s2)

