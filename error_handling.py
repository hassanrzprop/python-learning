# there are three types of error
# 1)syntax error (handled by compiler)
# 2)LOGICAL  error(handled with the help of other programmers)
# )runtime error(can be handled using method given below)

try:
    sum=23+2
except Exception  as e:
    print('"WARNING:"ERROR duing sum',e)
else:
    print("Workes when there is no error")
finally:
    print("it runs all the time")          



# example 
num1=int(input("Enter number1-->"))
num2=int(input("Enter number2-->"))

try:
    div=num1/num2
except Exception as e:     # we can also used other specified functions to handle the specific error like valueError function 
    print("ERROR:",e); 

else:
    print(div);
finally:
    print("used for some cases where we need to run code for both the conditions")