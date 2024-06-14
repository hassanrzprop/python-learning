# for loop is specially designed for list.Mostly we use for loop list but we can also used it as while loop so FOR loop has two syntax
#  ******1)
numbers=[11,22,44,34,2312,123,43,23,12]
# for item in numbers:
#     print(item)

# Now compared it to while loop but in this complexity will increase as compared to for loop
# i=0
# while i<=len(numbers)-1:
#     print("while-->",numbers[i])
#     i+=1


# ********2)
# for index in range(1,9,1):
    # print("Second Syntax-->",index)

# 1) : write a program to find ali from the list and print it ALSO write its indexing
# insted we can also use enamutrate which return both item and index value

namesGiven=["hassan","waqar","zakir","ali","huziafa","mahad"]
for i,name in enumerate(namesGiven):
    # print("Loop running",name)
    if name=="ali":
        # print(name,namesGiven.index(name),i)
        break


# 2) EX: make a new list from existing  list and put values of ehich are in even indexes
inputList=["hassan","waqar","zakir","ali","huziafa","mahad","umar","zaifi"]
newlist=[]
for i,name in enumerate(inputList):
    if i%2!=0:
        newlist.append(name)

# print(newlist)
                         


# ********3) map builtin function syntax
mapTesting=["hassan","waqar","zakir","ali","huziafa","mahad","umar","zaifi"]
def modifingName(namie):
      return f"Hey {namie}!"
newMap=list(map(modifingName,mapTesting))
print(newMap)


# 3) EX: make a list of numbers which is double of the existing list
nums=[10,20,30,40,50,60,70,80,90,100]
newNums=list(map(lambda x:x+2,nums))
print(newNums)
# second way

def adding_list(num):
    return num+2;
addedList=list(map(adding_list,nums))
print(addedList)



# *******4) filter builtin function syntax
# write a program that don't include value of 30
forFilter=[10,20,30,40,50,60,70,80,90,100]
def filterFunction(item):
    if item!=30:
        return item;
newFilteredList=list(filter(filterFunction,forFilter))
print(newFilteredList)