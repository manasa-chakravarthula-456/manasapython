'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

'''class Solution:
    def majorityElement(nums):
      c=0
      candidate=0
      for num in nums:
        if c==0:
            candidate=num
            c+=1
        elif candidate==num:
            c+=1
        else:
            c-=1
      return candidate
    print(majorityElement([2,2,1,1,2,2]))'''
    
def kk(nums):
    k=[]
    s=""
    for num in nums:
        s+=str(num)
    i=int(s)+1
    z=str(i)
    for ch in z:
        k.append(int(ch))
    print(k)
nums=[9,9,9]
kk(nums)