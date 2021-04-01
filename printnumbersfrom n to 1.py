#toprint numbers from n to 1
def Number(n):
    for i in range(n,0,-1):
        print(i,end=' ')
n=int(input("enter n value"))
Number(n)