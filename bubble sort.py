'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

'''class MethodOverride1:
    def display(self):
        print("method involved from base class")
class MethodOverride2:
    def diplay(self):
        print("method involved from derived class")
obj=MethodOverride2()
obj.diplay()'''
'''class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def shownnumber(self):
        print(f"{self.real}i+{self.imag}j")
    def __add__(self,num2):
        newreal=self.real+num2.real
        newimag=self.imag+num2.imag
        return Complex(newreal,newimag)
num1=Complex(1,6)
num1.shownnumber()
num3=Complex(2,5)
num3.shownnumber()
num4=num1.__add__(num3)
num4.shownnumber()'''
'''def fib(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)
n=int(input())
fib(n)'''
'''def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1)+fib(n-2)
n=int(input())
print(fib(n))'''
'''def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
arr=list(map(int,input().split(",")))
target=int(input())
print(linear_search(arr,target))'''

'''def binary_search(arr,target):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1
arr=list(map(int,input().split(",")))
target=int(input())
print(binary_search(arr,target))'''
def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
           if arr[j]>arr[j+1]:
             arr[j],arr[j+1]=arr[j+1],arr[j]
arr=list(map(int,input().split(",")))
bubble_sort(arr)
print("sorted array:",arr)
            