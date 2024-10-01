string = input("Enter Numerical String: ")
num= int(string)
numlist = []
for i in range(len(string)):
    digit = (num // 10**i) % 10
    numlist.append(digit)
print(numlist)

dict={}
for digit in numlist:
    if(digit in dict):
        dict[digit]+=1

    else:
        dict[digit]=1

print(dict)
