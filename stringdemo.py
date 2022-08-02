s="Tejal Vasan"
print(s)
#for string length
print(len(s))
#The first character is the upper case only.
print(s.capitalize())
#all the characters are lower case
print(s.casefold())
#Returns the string centered in a string of length width.
print(s.center(40,"$"))
#Returns the string centered in a string of length width.
print(s.count("a"))
#check string end with
print(s.endswith("n"))
#find element in string
print(s.find("V"))
#find element in string with given index number
print(s.find("a",4))
#find element index in string
print(s.index("s"))
#Returns True if all characters in the string are alphanumeric
print("tejal123".isalnum())
print("$%te123".isalnum())
print(" * ")
print("123".isalnum())
#check string is numeric or not
print(s.isnumeric())
#Returns True if the string follows the rules of a title
print("Python programm".istitle())
#return string in title for
print("Python programm".title())

