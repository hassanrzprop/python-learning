# match operator in replace of if else

n=int(input("Enter Number-->"))
if n>0 and n<8:
    match n:
        case 1: 
            print("Monday")
        case 2: 
            print("Tuesday")
        case 3: 
            print("Wednesday")
        case 4: 
            print("Thursday")
        case 5: 
            print("Friday")
        case 6: 
            print("Saturday")
        case 7: 
            print("Sunday")
else:
    print("Not a Valid Number")             


#for string case

match input("Enter day-->"):
    case "monday":
        print(1)
    case "tuesday":
        print(2)     
    case _:
        print("Default Value")    