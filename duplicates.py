list=eval(input("enter list"))
for i in range(len(list)):
    for j in range(len(list)):
        if i==j:
            list.remove(list[j])
            
print(list)
    
    