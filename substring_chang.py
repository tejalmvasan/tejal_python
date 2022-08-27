'''
Write a Python program to find the first appearance of the substring 'not'
and 'poor' froma given string, if 'not' follows the 'poor', replace the whole
'not'...'poor'substring with 'good'. Return the resulting string
'''

s="this man is not a poor"

pnot=s.find("not")
ppoor=s.find("poor")

print("Position of not :",pnot)
print("Position of poor :",ppoor)

if pnot<ppoor:
    print(s[:pnot]+"good")
    


