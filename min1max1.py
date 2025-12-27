'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

x=list(map(int,input().split()))
min1=max1=x[0]
for i in range(1,len(x)):
    if x[i]<min1:
        min1=x[i]
    if x[i]>max1:
        max1=x[i]
print(min1,max1)