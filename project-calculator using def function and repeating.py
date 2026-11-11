def calculator():
    while True:
        print("Welcome to the calculator!")
        print("please enter two numbers")
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

        except ValueError:
         print("Invalid input! Please enter valid numbers.")
        
    
        print("Choose an operation:")
        print("1. Addition")
        print("2. Subtraction") 
        print("3. Multiplication")
        print("4. Division")
        try:
            operation = int(input("Enter the operation number (1-4): "))
            if operation == 1:
                result = num1 + num2
                print(f"The result of {num1}+{num2} is: {result}")
            elif operation==2:
                result = num1 - num2
                print(f"The result of {num1}-{num2} is: {result}")
            elif operation==3:
                result = num1 * num2
                print(f"The result of {num1}*{num2} is: {result}")
            elif operation==4:
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    result = num1 / num2
                    print(f"The result of {num1}/{num2} is: {result}")
            else:
                print("Invalid operation selected!")

            again=input("Aur calculation karna hai (yes/no): ")
            if again.lower() != "yes":
                print("Thank you for using the calculator!")
                break
       
       
        except ValueError:
            print("Invalid input! Please enter a valid operation number.")

calculator()