#  FUNCTIONS is used to stop the flow of execution and make it useful for later
print("line 1")
print("line 2")
def func():
    print("line 3")
    def nestedFunc():
        print("line 4")
    print("line 5")
    nestedFunc()
print("line 6")
print("line 7")

func()


# function parametering using paranthesis where c can be used if don't receive the value from the parameter
def addition(a,b,c=3):
    addRes=a+b+c
    print(addRes)
addition(5,10,5)    


# using return
def sum(a,b):
    c= a +b 
    # print(locals())   **to see locals data
    return c;
# without return type it will show none to c variable because data won't let go.
result =sum(10,10)
print(result)
addaToAdd=sum(result,20)
print(addaToAdd)
# print(globals())  to see globals data

# write a program that takes two number as input and return there sum
num1= int(input("Enter First Number -->"))
num2= int(input("Enter Second Number -->"))
res=num1 + num2 ;
print(res)