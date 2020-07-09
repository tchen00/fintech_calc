import time 
from colorama import Fore, Back, Style
firstTime = True

def loop():
    time.sleep(1.5)
    print("--------------------------------------------------------------------------")
    opt = int(input("Would you like to go back to the main menu? \n\t1. Yes, please! \n\t2. No, I would like to exit. \nInput an option number: "))
    if opt == 1: 
        main()
    elif opt == 2: 
        print("--------------------------------------------------------------------------")
        print("Thank you for using our calculator. Have a great day! :)")
        print("--------------------------------------------------------------------------")
        exit()

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
    loop()

def taxCalc():
    print('Welcome to the Tax Calculator')
    operator = ""
    number1 = float(input("What is the price? "))
    number2 = float(input("What is the tax percentage? "))
    print("\nRESULTS: \nThe tax is: $" + str(round(100*(number1 * number2 * .01))/100))
    print("The final bill is $" + str(round(100*(number1 * number2 * .01 + number1))/100))
    loop()

def averageCalc(): 
    print("Welcome to the Average Calculator")
    num = int(input("How many numbers would you like to average? "))
    sum = 0 
    for i in range(0, num): 
        n = float(input("\tNumber " + str(i+1) + ": "))
        sum += n 
    print("The sum of all your values is "+ str(sum) + ". The calculated average is " + str(sum/num) + ".")
    loop()

def intro(x):
    print("--------------------------------------------------------------------------")
    if x == 0:
        print(Fore.GREEN +'Welcome to the Calculator! \nHere is the main menu: \n\t1. Math Calculator\n\t2. Tax Calculator\n\t3. Average Calculator  ' + Style.RESET_ALL)
    if x == 1: 
        print('Welcome back to the Calculator! \nHere is the main menu: \n\t1. Math Calculator\n\t2. Tax Calculator\n\t3. Average Calculator  ')

def main():
    global firstTime
    if firstTime: 
        intro(0)
        firstTime = False
    else: 
        intro(1)
    option = int(input("Which calculator option would you like to choose? (input an option #) "))
    print("--------------------------------------------------------------------------")
    if option == 1: 
        mathCalc()
    if option == 2: 
        taxCalc()
    if option == 3: 
        averageCalc()
main()

