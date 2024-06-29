# Basic Opersstions of String
userName="Hassan Raza-12@\n"
# 1) len used to check the length of the string
charCount=len(userName)
print(charCount)




# 2)"str"  is used to convert anykind of value to string
num=str(202)
print(num+" ali")

boolean=str(False)
print(boolean + " means false")




# 3) concatination is  "+"
print(num + boolean + " :form of concatination in string")




# 4) * is used to repeat the string
print(userName*3)



# 5)Accessing string using index
print(userName[5])




# 6)slicing string part
firstName=userName[0:6]
# we can also give third value in idexing which represent the skiping number of spaces while choosing a value
secondName=userName[0:6:2]
print(firstName)
print(secondName)




# 7)upper and lower cases
realName="       haSSan RaZA        "
print(realName.lower())
print(realName.upper())



# 8) capitalize is used to capital the first character
print(realName.capitalize())

# 9)title is used to capital the first letter after every space
print(realName.title())


# 10)WHITE SPACING HANDLING
# strip is used to remove the spacing from both side of the string
print(realName.strip())
# t remove from left side "lstrip" is used
print(realName.lstrip())
# remove from right is "rstrip" is used
print(realName.rstrip())
name=realName.title().strip()





# 11) to find index of character or substring in the string
cName="ali raza"
print(cName.index("a"))
print(cName.index("raza"))

# 12) to count the repition of char or substring
print(cName.count("a"))



# 13) replace is used to change substring
print(cName.replace("ali","hassan"))

# 14) split is used to change string into list on the basis of delimit(means by giving on which basis it will split.By default it is set for spacing)
splitUsing=cName.split("a")
print(splitUsing)   




# 15)List to string using "join" method
namee=["muhammad","hassan","raza"]
fullName=" ".join(namee).title()
print(fullName)



# 16) Checking prefix(anything with which it is starting any charcter) with startwith and suffix(any character) endswith
print(fullName.startswith("M"))

print(fullName.endswith("a"))




# 17)checking aphlabet,digit and spacing
clas="first year"
print(clas.isalpha())
print(clas.isdigit())
print(clas.isspace()) 



# 18) format to add something
name1="raza"
name2="iqbal"
bigName="hassan {} s/o muhammad zafar {}".format(name1,name2).title()
print(bigName)