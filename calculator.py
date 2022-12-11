def add(x,y):
    return x+y
    def substract(x,y):
     return x-y
     def multiply(x,y):
        return x*y
        def division(x,y):
            return x/y
            print("select operator")
            print("1.add")
            print("2.substract")
            print("3.multiply")
            print("4.division")
            while true:
                choice=("enter choice from 1 2 3 4")
                if choice in ('1','2','3','4'):
                 num1=input("enter first no")
                 num2=input("enter secound no")
                 if choice=='1':
                    print(num1,"+",num2,"=",add(num1,num2))
                    if choice =='2':
                        print(num1,"-",num2,"=",substract(num1,num2))
                        if choice =='3':
                         print(num1,"*",num2,"=",multiply(num1,num2))
                         if choice =='4':
                          print(num1,"/",num2,"=",division(num1,num2))

                        next_calculation=input("lets do next calculation? (yes/no):")
                        if next_calculation=="no":
                            break
                        else:
                            print("input input")



