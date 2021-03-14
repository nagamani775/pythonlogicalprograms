#to take an integer from the keyboard and print words 
#15==>ONE FIVE 
list=['ZERO','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE']
n=int(input("enter an integer"))
if n<=9:
    print(list[n])
elif n<=99:
    print(list[n//10]+" "+list[n%10])
else:
    print("pls enter a n integer")

