#to accept a string an dprint no.of alphabets,digits,special symbols
str=input("enter an input string")
digits=['0','1','2','3','4','5','6','7','8','9']
alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
spec=['!','@','#','$','%','^','&']
total_digits=0
total_alphabets=0
total_spec=0
for s in str:
    if s  in digits:
       total_digits+=1
    elif s in alphabets:
        total_alphabets+=1
    else:
        total_spec+=1
print("total digits is:",total_digits)
print("total alphabets is:",total_alphabets)
print("total special charecters is :",total_spec) 