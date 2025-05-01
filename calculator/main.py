import sys
from crayons import red

def reader():
    print("")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("CALCULATOR")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("")

def transform_signal():
    global signal
    global sinal2
    if signal == 1:
        sinal2 = "+"
    elif signal == 2:
        sinal2 = "-"
    elif signal == 3:
        sinal2 = "x"
    elif signal == 4:
        sinal2 = "/"
    else:
        print("ERROR. YOU MUST SELECT AN OPTION BETWEEN 1 and 4.")

def calculation():
    global result
    if signal == 1:
        result = num1 + num2
    elif signal == 2:
        result = num1 - num2
    elif signal == 3:
        result = num1 * num2
    elif signal == 4:
        if num2 == 0:
            print("\nErro: division by zero\n")
            sys.exit()
        else:
            result = num1 / num2

reader()

num1 = float(input("Enter the first number: "))
signal = int(input("Enter one option between 1 and 4: ADD(1), SUBTRACT(2), MULTIPLY(3) ou DIVIDE(4): "))
num2 = float(input("Enter the second number: "))

# THIS PART OF THE CODE IS ONLY FOR VIEWING ON THE CONSOLE
# 
sinal2 = ""
transform_signal()

result = 0
calculation()

print(f"\nYou request to calculate the following {num1} {sinal2} {num2}")
print("")
print(red(f"And the result of the calculation is: {result}"))
print("")


