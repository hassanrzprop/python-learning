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
