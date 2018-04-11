# CREATOR : ALBERT - GRI
# DATE : 4/8/2018
# Version: 0.1
print ("Simple Non-GUICalc vs 0.1 : Created by Gri\n-----------------------------")

# Globals
operations_list = ['A', 'S', 'M', 'D']
determine = True


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
    float_num = float(input('Enter a number: '))
    return float_num

def result_float_toStr_printer(r):
    print('-------------------\nThe float result is: ' + str(r))

#main flow of the program

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
        num2 = get_float_num()
        result = division(num1, num2)
        result_float_toStr_printer(result)
    else:
        determine = True
        print("Your choice wasn't recognised\nPlease try again\n\n")



# Flow (Program flow)

#while True:
#   calc_inp = input('Calculate Y/N: ')
#    if calc_inp == 'Y' or calc_inp == 'y':
#        flow()
#    else:
#        print('\nThank you for using Non-GUICalc!')
#        input('Press Enter to quit: ')
#        break
# EDITING NOTES:
# ATM: If 'flow()' method is removed and it goes to the global field, deleting the # flow part of the program - it will work, but
# .. it will make only one calculation and the quit automatically
# My Goal: To make it so while user enters 'Y' or 'y' the calculations continue, if the user enters 'N' or 'n' it breaks from the loop and quits
# At the moment the functionality goes to either the - second number's get input or - it might still be the first one
# It doesn't print the result
# ---- It might not get to the part where it says to print the results
# ---- ---- Which means it doesn't get to the If statement in the flow() function

# Possible solutions: Check wheather there is an issue with the acknoledgment of global variables from within the functions(methods)
# PS: Any updates next time : CREATE A NEW FILE and mark as vs 0.2
