'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

'''x="madam"
l=0
r=len(x)-1
while l<r:
    if x[1]==x[r]:
        l+=-1
        r-=1
        print("palindrome")
    else:
        print("not a paindrome")'''

'''def check(x):
l=0
r=len(x)-1
while l<r:
    if x[1]!=x[r]:
    return"not a palindrome"
    else:
    l+=-1
    r-=-1
return palindrome'''

'''year=int(input())
if year %4==0 and year%100!=0:
    print("leap year")
elif year %4==0:
    print("leap year")
else:
    print("not a leap year")'''
    
def cupcakes(n,arr):
    sum=0
    for i in range(n):
        if arr[i]>=5:
            sum+=arr[i]
    print(sum)
n=5
arr=[1,2,5,8,3,7]
cupcakes(n,arr)