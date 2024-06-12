studentNames:list=["hassan","ali","Waqar","Muhammad","haider","ali"]


# 1) to add something at the end
# ****ERROR**** because append don't return any value
studentNames.append("Zaifi")



# 2)************** to delete something from end we basically use pop************
#  pop return same value the he delete with the help of index
res1=studentNames.pop(1)
studentNames.pop()
listOfNumbers:list=[1,2,6,3,4,245,46,43,4353,123]


#3) extend keyword add list into the list
# studentNames.extend(listOfNumbers) 
# print(studentNames)


# 4) insert in used to add element anywhere in the list
studentNames.insert(2,"hurairah")
# print(studentNames)


#5) we remove element by using remove with the help of value
studentNames.remove("Waqar")



#6) to find index of a value we use index
output=studentNames.index("ali")



#7) to count the repitition of the value we basically use count builtin function
res2=studentNames.count("ali")
print(res2)



# 8)sort will arrange the list in ascending order
studentNames.sort()
print(studentNames)



# 9) reverse will arrange the list in descending order
studentNames.reverse()
print(studentNames)



# 10)to delete all items from the list we will use clear
# studentNames.clear()
print(studentNames)


# 11) concatination using + sign it will not mofidied the original list
modLIst=studentNames + listOfNumbers
print(modLIst)


# 12) copy is used to copy a list as same it is
result=studentNames.copy()
print(result)


# 13) len is used to find the length of the list
length1=len(studentNames)
print(length1)



# 14) membership operator "in" in list
output1="ali" in studentNames
print(output1)


# 15) nested list list in list
nestedList=["ali","umar","haider",["zia","muzamil","mohsin"]]
print(nestedList[3][2])


# 16)   mulitply
output3=["Hi!"] * 4
print(output3)

# 17) slicing is used to take out specfic part of the list
output5=nestedList[0:3]
print(output5)