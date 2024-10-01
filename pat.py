n=int(input("enter the no. of arr= "))
list_1=[]
count=0
while (n>0):
   a=int(input("Enter the no.= "))
   list_1.append(a)
   n=n-1
print(list_1)
list_2=[]
def is_prime(num):
   if (num < 2):
      return False
   for i in range(2,list_1+1):
      if (num%i==0):
         return False
      return True
   
print(is_prime(list_2))