'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

x="madam"
l=0
r=len(x)-1
while l<r:
    if x[1]==x[r]:
        l+=-1
        r-=1
        print("palindrome")
    else:
        print("not a paindrome")