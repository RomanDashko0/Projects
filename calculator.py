while True:
    a = float(input("first number: "))
    b = float(input("second number: "))
    operation = input("If you want to leave, just enter. Operation (+ - * /): ")

    if operation == "+":
        print(a+b)

    elif operation == "-":
        print(a-b)

    elif operation == "*":
        print(a*b)

    elif operation == "/":
        print(a/b)

    elif operation == "":
        break

    else:
        print("unknown operation")





    

