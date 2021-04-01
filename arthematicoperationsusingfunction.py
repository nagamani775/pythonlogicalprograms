#to perform arthematic operations using functions
def sum(a,b):
    c=a+b
    print(c)
def sub(a,b):
    d=a-b
    print(d)
def mul(a,b):
    e=a*b
    print(e)
def div(a,b):
    f=a/b
    print(f)
def fdiv(a,b):
    g=a//b
    print(g) 
def mod(a,b):
    h=a%b
    print(h) 

sum(45,45)
sub(89,80)
mul(8,9)
div(20,15)
fdiv(5,2)
mod(5,2)


#to perform arthematic operations in one function
def sum_sub_mul_div_fdiv_mod(a,b):
    sum=a+b
    print(sum)
    sub=a-b
    print(sub)
    mul=a*b
    print(mul)
    div=a/b
    print(div)
    fdiv=a//b
    print(fdiv)
    mod=a%b
    print(mod)

sum_sub_mul_div_fdiv_mod(5,2)

#to perform *args in function
def sum(*a):
    sum=0
    for i in a:
        sum=sum+i
        print(i,end=" ")
    print(sum)

sum(10,20,30)

sum(10,20,30)
