#to print asending and decending order 
a=int(input("enter a value"))
b=int(input("enter b value"))
c=int(input("enter c value"))
L=[a,b,c]
L.sort(reverse=True)
print("deccending order:",L)
L.sort()
print("asceng order:",L)

#using function
def asend_decend(a,b,c):
    L=[a,b,c]
    L.sort(reverse=True)
    print("deccending order:",L)
    L.sort()
    print("asceng order:",L)

asend_decend(50,80,90)