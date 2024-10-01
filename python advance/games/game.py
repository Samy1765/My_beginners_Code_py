import json
import os
print("Do You Want TO Set A Multi Choice Game Or Want To Just Play A pre Wirtten: ")
opi=int(input("Enter 1 To Set And 2 To Play: "))
score=0

if(opi==1):
 data=[]
 n=int(input("Enter The No. Of Question You Want TO Add : "))

 for i in range(n):
   qus=input("Enter The Question : ")
   print("Great :")
   k=int(input("Enter No. Of Alternatives : "))
   alt=[]
   for j  in range(k):

      altt=(input("Enter The Alternatives: "))
      alt.append(altt)
   opt=int(input("Enter The Right the answer : "))
   
   quedata={"Question": qus,  "Alternate": alt, "Correct":opt}
   data.append(quedata)
   os.system('cls')
   print("Test File HAve Been Updated Successfully. ")
   
   with open("gameq.json",'w') as file :
    json.dump(data, file, indent=4)
   with open("gameq.json",'r') as file:
    contant=file.read()
    data=json.loads(contant)

if(opi==2):
   with open("questions.json",'r') as file:
    contant=file.read()
    data=json.loads(contant)

for question in data:
   print(question["Question"])
   for index,alternative in enumerate(question["Alternate"]):
      print(index+1,"-",alternative)
      userch=int(input("Enter The No. Of The Option: "))
      if(userch>len(alternative)):
         print("Invalid Choics")
      else:
         question["Users Choice"]=userch
      

if question["Users Choice"]==question["Correct Answer"]:
        score+=1
print(score,"/",len(data))