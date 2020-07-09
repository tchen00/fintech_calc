import time 
from colorama import Fore, Back, Style
firstTime = True

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

def taxCalc():
    time.sleep(1)
    print(chr(27) + "[2J")
    print(Fore.RED + Back.WHITE + 'Welcome to the Tax Calculator\n' +  Style.RESET_ALL )
    operator = ""
    number1 = float(input("What is the price? "))
    number2 = float(input("What is the tax percentage? "))
    print(Fore.RED + Back.WHITE + "\nRESULTS:" + Style.RESET_ALL + "\nThe tax is: $" + str(round(100*(number1 * number2 * .01))/100))
    print("The final bill is $" + str(round(100*(number1 * number2 * .01 + number1))/100))
    loop()

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

def intro(x):
    print("--------------------------------------------------------------------------")
    time.sleep(1.5)
    print(chr(27) + "[2J")
    if x == 0:
        print(Fore.GREEN + Back.WHITE + "Welcome to the Calculator!" +  Style.RESET_ALL)
        print("\nHere is the Main Menu: \n\t1. Math Calculator\n\t2. Tax Calculator\n\t3. Average Calculator  ")
    if x == 1: 
        print(Fore.GREEN + Back.WHITE + 'Welcome back to the Calculator!\n'  + Style.RESET_ALL + '\nHere is the main menu: \n\t1. Math Calculator\n\t2. Tax Calculator\n\t3. Average Calculator  ')

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
    if option == "exit": 
        exit()
    else: 
        main()

main()

