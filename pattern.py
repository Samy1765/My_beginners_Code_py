list=["A","B","C","D","E"]
n=int(input("Enter Your Choice : \n1. For  Straight Pryamid\n\n2. For Reverse Straight Pryamid\n\n3. For Reverse Pryamid\n\n4. For Reverse Straight Pryamid\n\n5. For Same Word Pryamid\n\n6. For Same Word Reverse Pryamid  : "))

match(n):
  
  case 1:
    for i in range(1,5):
      print(list[0:i])
      
  case 2:
    for i in range(5,1,-1):
      print(list[0:i])
      

  case 3:
    for i in range(1,5):
      print(list[:i][::-1]) 
  
   
  case 4: 
    for i in range(5,1,-1):
      print(list[:i-1][::-1])  
     

  case 5:
    for i in range(0,5):
        print(list[i]*(i+1))
     

  case 6:
    for i in range(4,0,-1):
      print(list[i-1]*(i))