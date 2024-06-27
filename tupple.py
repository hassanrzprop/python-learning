# tupple is like list but we can't add anything in the tupple.it is immutable.
tupple=("ali","waqar","hassan","Wakeel")
# it can be get only by index
print(tupple[2])
# looping supported
for item in tupple:
    print(item)

# slice is possible in Tuple 
halfList=tupple[2:4]
print(halfList)



# write a program to check the duplication of the item 
nums = (10, 20, 30, 40, 50, 60, 60, 70, 80)
nums_list=list(nums)
unique_elements = []

duplicates=[]
for num in nums_list:
    if num in unique_elements:
        duplicates.append(num)
    else:
        unique_elements.append(num) 
print(unique_elements)
print(duplicates)           