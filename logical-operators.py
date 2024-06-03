#  --------comparison operator----------

#  assign operator is =
num1=2
num2=5

#  comparison operator is ==
#  -equal operator
result:bool=num1 == num2
#  not equal operator
result1= num1 != num2
print(result1)

# greator than    2) greator than or equal to.    3)less than       4)less than or equal to

print(num1>num2)
print(num1>=num2)
print(num1<num2)
print(num1<=num2)


#  --------logical operators----------
#          ***and*****  all values should be true 
result2=num2>num1 and num1>num2
print(result2)


#    ****or****  which holds single value true it would be true
result3=num2>num1 or num1>num2
print(result3)

# ***not***    reverses the operation of the result
result4= (num1+2>num2 and num2<= 2 or num1**num2)
print(result4, " expression test")


# membership operators is used to find the included find in variable or list there are 2 operators
userName="Hassan Raza"
locate="s"
result5=locate in userName; result6= locate not in userName
print(result5)





# "is" idetity operator
equal="Hassan Raza"
res=equal is userName; res1=equal is not userName
print(res); print(res1)