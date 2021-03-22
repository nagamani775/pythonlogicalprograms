#count all vowels present in the string

s={'a','e','i','o','u'}
str1=input("enter some string")
s1=s.intersection(str1)
print("the vowels present in the {0} are {1}".format(str1,s1))