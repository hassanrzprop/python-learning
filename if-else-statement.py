# if 10>5:
#     print("hello world")
# # exercise ***take  a number from user and print if wheter it is even or odd. if it is even check it is greater than 50
# num1=int(input("Enter Your Number-->"))
# if num1%2==0 and num1>0 :
#     if num1<50:
#         print("It is even Number less than 50")
#     else:
#         print("even number is greater than 50")
# elif num1==0:
#     print("Number is zero")        
# else:
#     print("It is odd")




# write a program that takes user input of three numbers and find the largest one
num2=int(input("Enter First Number -->"))
num3=int(input("Enter Second Number -->"))
num4=int(input("Enter Third Number -->"))
if num2>num3 and num2>num4:
    print(f"Largest NUmber is {num2}")
elif num3>num2 and num3>num4:
    print(f"Largest Number is {num3}")
else:
    print(f"Largest Number is {num4}")        