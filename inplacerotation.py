'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

'''x=[2,5,7,1,9]
x1=min(x)
x2=max(x)
min2=float("inf")
max2=float("-inf")
for i in range(len(x)):
    if x1<x[i]<min2:
        min2=x[i]
    if x2>x[i]>max2:
        max2=x[i]
print(min2,max2)'''

x=[1,2,3,4,5]
l=0
r=len(x)-1
while l<r:
    x[l],x[r]=x[r],x[l]
    l+=1
    r-=1
print(x)