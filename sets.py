# a set is like tuple and list but conatains all unique elements and no repition is allowed
studentEmails={"test@test.com","test@test2.com","test@test.com"}
# it will automatically remove the duplicated item
print(studentEmails)

# add data
studentEmails.add("hassan32425")
print(studentEmails)


# update
studentEmails.update("test@test.com","s")
print(studentEmails)

# remove
studentEmails.remove("test@test2.com")
print(studentEmails)


# EX: remove all repetative elements from the list 
contList=[10,10,20,30,40,50,50,60,70,60,70,80,90,100]
uniqueList= list(set(contList))
uniqueList.sort()
print(uniqueList)




# union method on set has also sign " | "
set1={1,2,3,4}
set2={5,6,7,8}
union_set=set1.union(set2)
print(union_set)

sign_union= set1 | set2
print(sign_union)


# intersection method and it can also be done by using $ operator
set3={1,2,3,4,5,6}
set4={2,4,6,8,10}

intersectionSet= set3.intersection(set4)
print(intersectionSet)
intersectionSign= set3 & set4
print(intersectionSet)