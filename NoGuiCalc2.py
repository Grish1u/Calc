# CREATOR : ALBERT - GRI
# Release date : 4/9/2018
# Last updated: 4/25/2018
# Version: 0.5
# Enlarged functionality
    # What was done: 
    # Git tested x3
    # Added a list to keep track of the history of calculations
print ("Simple Non-GUICalc vs 0.5 : Created by Grishak\n-----------------------------")

# Globals
operations_list = ['A', 'a', 'S', 's', 'M', 'm', 'D', 'd'] # choice
c = True # THIS ONE WE MIGHT NOT NEED
results = [] # keeps track of the history of the results in the calculations

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
    
            if inp == operations_list[0] or inp == operations_list[1]:
                determine = False
                print('Your choice is Addition\n')
                num2 = get_float_num()
                result = addition(num1, num2)
                results.append(result)
                result_float_toStr_printer(result)
            elif inp == operations_list[2] or inp == operations_list[3]:
                determine = False
                print('Your choice is Substraction\n')
                num2 = get_float_num()
                result = subtraction(num1, num2)
                results.append(result)
                result_float_toStr_printer(result)
            elif inp == operations_list[4] or inp == operations_list[5]:
                determine = False
                print('Your choice is Multiplication\n')
                num2 = get_float_num()
                result = multiplication(num1, num2)
                results.append(result)
                result_float_toStr_printer(result)
            elif inp == operations_list[6] or inp == operations_list[7]:
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
                results.append(result)
                result_float_toStr_printer(result)
            else:
                determine = True
                print("Your choice wasn't recognised\nPlease try again\n\n")
    elif calc_inp == 'N' or calc_inp == 'n' :
        print('Calculations history: ', str(results))
        print('Thank you for using NoGuicCalc2')
        input('Enter to quit: ')
        break
    else:
        print('Input not recognised')    


# TODO:1
# - Check whether we need the global variable 'c'
