Operations= {"Addition":1,"Subs":2,"Multiply":3, "Division": 4}
try:
    num_1= int(input("Please enter the first number: "))
    num_2 = int(input("Please enter the second number: "))

    print("These are the operations",Operations)

    cal=int(input("Please enter the number of the operation from the dictionary above: ").strip())

    if  cal==1:
       result=num_1+num_2
       print("Your sum is : ",result)
    elif cal==2:
       diff=num_1-num_2
       print("Your difference  is : ",diff)
    elif cal==3:
       times=num_1*num_2
       print("Your multiple is :",times)
    elif cal==4:
       if num_2!=0:
           d=num_1/num_2
           print("Your division is :", d)
       else:
           print("Can't divide by Zero")
    else:
        print("Please enter valid numbers")
except ValueError:
    print("Please enter a valid number")



