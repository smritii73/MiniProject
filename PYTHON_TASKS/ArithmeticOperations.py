def ArithmeticOperations():
    try:
        n1=float(input("Enter the 1st Number:"))
        n2=float(input("Enter the 2nd Number:"))
        
        sum=n1+n2;
        difference=n1-n2
        product=n1*n2
        if n2!=0:
            quotient = n1/n2
            remainder = n1%n2
        else:
            quotient="Divide by Zero Error"
            remainder="Divide by Zero Error"
        print("RESULTS")
        print(f"Addition of 2 numbers:{(int)(sum)}")
        print(f"Difference between 2 numbers:{(int)(difference)}")
        print(f"Product of 2 numbers:{(int)(product)}")
        print(f"Quotient of 2 numbers:{quotient}")
        print(f"Remainder of 2 numbers:{remainder}")
        
    except ValueError: print("Invalid Input")
    
if __name__ == "__main__": ArithmeticOperations()
