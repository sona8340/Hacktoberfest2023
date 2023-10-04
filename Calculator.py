while(True):
    print("what type of operation you want to perform?\n"
          "type + for addition\n"
          "type - for subtraction \n"
          "type * for multiplication\n"
          "type / for division\n"
          "type ** to raise the power\n")
    operator = input("Enter operator:")
    num1 = int(input("Enter your first number:\n"))
    num2 = int(input("Enter your second number:\n"))
    print("Answer:")
    if operator == "+":
        if num1 == 56 and num2 == 9:
            print(77)
        else:
            print(num1 + num2)
    elif operator == "/":
        if num1 == 56 and num2 == 6:
            print(4)
        else:
            print(num1 / num2)
    elif operator == "*":
        if num1 == 45 and num2 == 3:
            print(555)
        else:
            print(num1 * num2)
    else:
        print(num1 - num2)
    i = input("Do you want to use it again.Y/N:")
    if i == "N"or "n":
        break
    if i == "Y" or "y":
        continue

