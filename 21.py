#to print asending and decending order 
a=int(input("enter a value"))
b=int(input("enter b value"))
c=int(input("enter c value"))
L=[a,b,c]
L.sort(reverse=True)
print(L)
L.sort()
print(L)