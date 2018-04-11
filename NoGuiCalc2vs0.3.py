# CREATOR : ALBERT - GRI
# DATE : 4/9/2018
# Version: 0.3
# New to this version: Error fixes
    # What was done: 
    # Added new function is_number, and it is implemented in a way that works in the get_float_num() func
print ("Simple Non-GUICalc vs 0.3 : Created by Gri\n-----------------------------")

# Globals
operations_list = ['A', 'S', 'M', 'D']
c = True


# Funcs / Methods

def addition(n1, n2):
    return(n1+n2)

def subtraction(n1, n2):
    return(n1-n2)

def multiplication(n1, n2):
    return(n1*n2)

def division(n1, n2):
    return(n1/n2)

def get_float_num():
    while True:
        float_num = input('Enter a number: ')
        if is_number(float_num):
            return float(float_num)
        else:
            print('Please enter a numeric value')

def result_float_toStr_printer(r):
    print('-------------------\nThe float result is: ' + str(r))

# Used to determine whether a given value is a number of type float
# Got this function from 'https://stackoverflow.com/questions/354038/how-do-i-check-if-a-string-is-a-number-float'
def is_number(s):
    try:
        float(s) # 
        return True
    except ValueError:
        return False

#main flow of the program
while True:
    determine = True # Helps with making sure that the user puts correct input for an operation - 'A' or 'S' or 'M' or 'D'
    calc_inp = input('Make a calculation? Y/N: ')
    if calc_inp == 'Y' or calc_inp == 'y':
        while determine == True: # Choosing a correct option will make determine to False thus the loop won't apply again
            num1 = get_float_num()
    
            inp = input('A - Addition\nS - Substraction\nM - Multiplication\nD - Division\n------------\nType the letter and press enter: ')
    
            if inp == operations_list[0]:
                determine = False
                print('Your choice is Addition\n')
                num2 = get_float_num()
                result = addition(num1, num2)
                result_float_toStr_printer(result)
            elif inp == operations_list[1]:
                determine = False
                print('Your choice is Substraction\n')
                num2 = get_float_num()
                result = subtraction(num1, num2)
                result_float_toStr_printer(result)
            elif inp == operations_list[2]:
                determine = False
                print('Your choice is Multiplication\n')
                num2 = get_float_num()
                result = multiplication(num1, num2)
                result_float_toStr_printer(result)
            elif inp == operations_list[3]:
                determine = False
                print('Your choice is Division\n')
                num2 = 0
                while True:
                    num2 = get_float_num()
                    if num2 == 0:
                        print("Can't divide by 0")
                    else:
                        break
                result = division(num1, num2)
                result_float_toStr_printer(result)
            else:
                determine = True
                print("Your choice wasn't recognised\nPlease try again\n\n")
    elif calc_inp == 'N' or calc_inp == 'n' :
        print('Thank you for using my calculator')
        input('Enter to quit: ')
        break
    else:
        print('Input not recognised')    


# TODO:1
# - Try larger numbers, try signed and unsigned numbers
# - Test each operation
# - Massive chance for errors with the expected user input - to string, to int, to float etc.
# - TESTING MUCH MORE TESTING
