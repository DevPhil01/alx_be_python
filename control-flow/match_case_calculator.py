num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

result = None

match operation: 
    case '+': 
        result = num1 + num2

    case '-': 
        result = num1 - num2
        
    case '*': 
        result = num1 * num2
        
    case '/': 
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"The result is {result}.")
    case _: 
        print( "Invalid operation. Please choose one of (+, -, *, /).")
        
        
if result is not None:
    print(f"The result is {result}.")
    
    
    
