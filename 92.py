#check if the given string is palindrome or not
str1=input("ener a string")
r=reversed(str1)
output="".join(r)
print(output)
if str1==output:
    print("given string a palindrom")
else:
    print("not a palindrome")

    #using function

def palin(str):
    r=reversed(str)
    output="".join(r)
    print(output)
    if str==output:
        print("given string a palindrom")
    else:
        print("not a palindrome")


palin('amma')
palin('mani')