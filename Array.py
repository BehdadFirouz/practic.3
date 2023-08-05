import random
n=int(input("chand adad mikhahid  "))
min=int(input("adad shoro adad  "))
max=int(input("adad payan adad  "))
if n>max+1-min :
    print("ERROR")
else :
    array=[]
    for i in range(n):
        a=random.randint(min , max)
        if not (a in array):
            array.append(a )
    print(array)