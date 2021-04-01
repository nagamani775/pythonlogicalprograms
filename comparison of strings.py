#accept two string and compare them
s1=input("enter first string")
s2=input("enter second string")
if s1==s2:
    print("two strings are equal")
elif s1>s2:
    print("{0} is larger than {1}".format(s1,s2))
else:
    print("{0} is smaller than {1}".format(s1,s2))