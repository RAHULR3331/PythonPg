def calculator():
    while True:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("Type 'stop' to exit")

        choice = input("Enter choice (1/2/3/4) or 'stop' to exit: ")
        
        if choice == 'stop':
            print("Calculator Closed")
            break
        
        if choice not in ('1', '2', '3', '4'):
            print("Invalid input")
            continue

        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))

        if choice == '1':
            print(n1, "+", n2, "=", n1 + n2)
        elif choice == '2':
            print(n1, "-", n2, "=", n1 - n2)
        elif choice == '3':
            print(n1, "*", n2, "=", n1 * n2)
        elif choice == '4':
            if n2 == 0:
                print("Error! Division by zero.")
            else:
                print(n1, "/", n2, "=", n1 / n2)

calculator()
