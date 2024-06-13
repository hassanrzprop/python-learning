print("Before While")
i=6
while i>0:
    print("Hello World!",i)
    i-=1
print("After While")

# 1) EX: make talbe of multiple of any number using input and any input count 


markTable=int(input("Enter Table Number-->"))
tableCount=int(input("Enter Table Count-->"))
num=1
while num<=tableCount:
    result=num *markTable
    print(f"{markTable} * {num} = {result}")
    num+=1


# 2) EX:  make new list from existing list but multiple of two to each index
listNUm:list=[10,20,30,40,50,60,70,80,90,100]
newList=[]
i=0
while i<=len(listNUm)-1:
    newList.append(listNUm[i] * 2)
    i+=1
print("Old list of NUmbers-->                ",listNUm)
print("Modified mutiple of 2 Number List-->  ",newList)

# 3) EX: count the number of even and odd numbers in the list [12,23,34,45,567,78,989,87,65,54] and also separaTELY SUM AND EVEN and odd
inputList=[12,23,34,45,567,78,989,87,65,54]
n=0
EvenCount=0
oddCount=0
while n<=len(inputList)-1:
    if inputList[n] %2 ==0:
        sumEven=0
        sumEven+=inputList[n]
        EvenCount+=1
    else:
        oddCount+=1
        sumOdd=0
        sumOdd+=inputList[n]
    n+=1;
print("Total even numbers in thr list-->",EvenCount)
print("Total odd numbers in the list--> ",oddCount)    
print("Sum of even Numbers-->",sumEven)
print("Sum of Odd Numbers--> ",sumOdd)


#  4) EX: write a program to calculate remainder without using remainder sign

def calculate_remainder(dividend, divisor):
    quotient=dividend//divisor
    product=divisor *quotient
    remainder=dividend-product
    print(remainder)
    return remainder;
dividend=int(input("Enter Dividend Number-->"))
divisor=int(input("Enter Divisor Number-->"))
calculate_remainder(dividend,divisor)

