import time 
from colorama import Fore, Back, Style
firstTime = True

# main menu loop 
def loop():
    time.sleep(1.5)
    print(chr(27) + "[2J")
    print("--------------------------------------------------------------------------")
    opt = int(input(Fore.BLUE + Back.WHITE + "Would you like to go back to the main menu? \n" +  Style.RESET_ALL + "\n\t1. Yes, please! \n\t2. No, I would like to exit. \n\nInput an option number: "))
    if opt == 1: 
        main()
    elif opt == 2: 
        print(chr(27) + "[2J")
        print("--------------------------------------------------------------------------")
        print(Fore.BLUE + Back.WHITE + "Thank you for using our calculator. Have a great day! :)" + Style.RESET_ALL)
        print("--------------------------------------------------------------------------")
        exit()
    else: 
        loop()

# basic math operations calculator 
def mathCalc(): 
    time.sleep(1)
    print(chr(27) + "[2J")
    print(Fore.RED + Back.WHITE + 'Welcome to the Math Calculator\n' +  Style.RESET_ALL )
    operators = ["+","-","*","/","%", "**", "exit"]
    operator = ""
    while operator not in operators:
        operator = input("What operation (+ - * / ** %)?  ")
        if operator == "exit":
            exit()
    number1 = int(input("First Number? "))
    number2 = int(input("Second Number? "))
    if operator == "+":
        print(Fore.RED + Back.WHITE + "Answer:" +  Style.RESET_ALL + " " + str(number1 + number2))
    elif operator == "-":
        print(Fore.RED + Back.WHITE + "Answer:" +  Style.RESET_ALL + " " + str(number1 - number2))
    elif operator == "*":
        print(Fore.RED + Back.WHITE + "Answer:" +  Style.RESET_ALL  + " " + str(number1 * number2))
    elif operator == "/":
        print(Fore.RED + Back.WHITE + "Answer:" +  Style.RESET_ALL  + " " + str(number1 / number2))
    elif operator == "**":
        print(Fore.RED + Back.WHITE + "Answer:" +  Style.RESET_ALL  + " " + str(number1 ** number2))
    elif operator == "%":
        print(Fore.RED + Back.WHITE + "Answer:" +  Style.RESET_ALL  + " " + str(number1 ** number2))
    loop()

# tax calculator
def taxCalc():
    time.sleep(1)
    print(chr(27) + "[2J")
    print(Fore.RED + Back.WHITE + 'Welcome to the Tax Calculator\n' +  Style.RESET_ALL )
    operator = ""
    number1 = float(input("What is the price? "))
    number2 = float(input("What is the tax percentage? "))
    print(Fore.RED + Back.WHITE + "\nRESULTS:" + Style.RESET_ALL + "\nThe tax is: $" + str(round(100*(number1 * number2 * .01))/100))
    print("The final bill is $" + str(round(100*(number1 * number2 * .01 + number1))/100))
    time.sleep(1.5)
    loop()

# average calculator
def averageCalc(): 
    time.sleep(1)
    print(chr(27) + "[2J")
    print(Fore.RED + Back.WHITE + 'Welcome to the Average Calculator\n' +  Style.RESET_ALL )
    num = int(input("How many numbers would you like to average? "))
    sum = 0 
    for i in range(0, num): 
        n = float(input("\tNumber " + str(i+1) + ": "))
        sum += n 
    print("The sum of all your values is "+ str(sum) + ". The calculated average is " + Fore.RED + Back.WHITE + str(sum/num) + Style.RESET_ALL  + ".")
    loop()

# main menu  
def intro(x):
    print("--------------------------------------------------------------------------")
    time.sleep(1.5)
    print(chr(27) + "[2J")
    if x == 0:
        print(Fore.GREEN + Back.WHITE + "Welcome to the Calculator!" +  Style.RESET_ALL)
        print("\nHere is the Main Menu: \n\t1. Math Calculator\n\t2. Tax Calculator\n\t3. Average Calculator\n\t4. PEMDAS Calculator  ")
    if x == 1: 
        print(Fore.GREEN + Back.WHITE + 'Welcome back to the Calculator!\n'  + Style.RESET_ALL + '\nHere is the main menu: \n\t1. Math Calculator\n\t2. Tax Calculator\n\t3. Average Calculator\n\t4. PEMDAS Calculator  ')

# shunting yard algo for PEMDAS
def pemdasCalc():
    print(Fore.RED + Back.WHITE + 'Welcome to the PEMDAS Calculator\n' +  Style.RESET_ALL )
    expression = input("Math Expression (put a space between everything) : ")
    numbers = []
    operator = []
    expresslist = expression.split(" ")
    operators = ["+","-","*","/"]
    fast = ["*","/"]
    slow = ["+","-"]
    i = 0
    while i < len(expresslist):
        if not expresslist[i] in operators:
            numbers.append(float(expresslist[i]))
        if expresslist[i] in operators:
            operator.append(expresslist[i])
        elif len(operator) > 0:
            if operator[-1] in fast:
                if operator[-1] == "*":
                    numbers.append(float(numbers.pop(-1)) * numbers.pop(-1))
                if operator[-1] == "/":
                    a = numbers.pop(-1)
                    b = numbers.pop(-1)
                    numbers.append(float(b / a))
                operator.pop(-1)
        i += 1
    while len(operator) > 0:
        a = numbers.pop(-1)
        b = numbers.pop(-1)
        operation = operator.pop(-1)
        if  operation == "+":
            numbers.append(a + b)
        if operation == "-":
            numbers.append(b - a)
    print(numbers[0])

# main func to run calculator 
def main():
    global firstTime
    if firstTime: 
        intro(0)
        firstTime = False
    else: 
        intro(1)
    option = input("\nWhich calculator option would you like to choose (input an option #) ?  ")
    print("--------------------------------------------------------------------------")
    if option == "1": 
        mathCalc()
    if option == "2": 
        taxCalc()
    if option == "3": 
        averageCalc()
    if option == "4": 
        pemdasCalc()
    if option == "exit": 
        exit()
    else: 
        main()

main()

