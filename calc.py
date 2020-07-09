def mathCalc(): 
    operators = ["+","-","*","/","exit"]
    operator = ""
    while operator not in operators:
        operator = input("What operation (+ - * /)?  ")
        if operator == "exit":
            exit()
    number1 = int(input("First Number? "))
    number2 = int(input("Second Number? "))
    if operator == "+":
        print("Answer: " + str(number1 + number2))
    elif operator == "-":
        print("Answer: " + str(number1 - number2))
    elif operator == "*":
        print("Answer: " + str(number1 * number2))
    elif operator == "/":
        print("Answer: " + str(number1 / number2))
    else:
        exit()

def tipCalc():
    print('Welcome to the Tip Calculator')
    operator = ""
    number1 = float(input("What is the price? "))
    number2 = float(input("What is the tax percentage? "))
    print("\nRESULTS: \nThe tax is: $" + str(round(100*(number1 * number2 * .01))/100))
    print("The final bill is $" + str(round(100*(number1 * number2 * .01 + number1))/100))

def averageCalc(): 
    print("Welcome to the GCD/LCM Calculator")

def main():
    print("--------------------------------------------------------------------------")
    print('Welcome to the Calculator! \nHere is the main menu: \n\t1. Math Calculator\n\t2. Tax Calculator\n\t3. Average Calculator  ')
    option = int(input("Which calculator option would you like to choose? (Input a number) "))
    print("--------------------------------------------------------------------------")
    if option == 1: 
        mathCalc()
    if option == 2: 
        taxCalc()
    if option == 3: 
        averageCalc()
main()

