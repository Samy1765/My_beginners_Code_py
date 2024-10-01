largest = 0
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num=int(num)
        #print(num)
       
    except:
        print("Invalid input")
        continue
        
        
    if largest<num:
            largest=num
    elif smallest==None or smallest>num:
            smallest=num
            

print("Maximum is", largest)
print("Minimum is", smallest)