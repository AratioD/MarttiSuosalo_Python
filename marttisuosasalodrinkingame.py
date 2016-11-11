
if __name__ == "__Martti_Suosalo_Drinking_Game__":
    print "Automatic test description demo"


""" Please read the full specification from Specification.py file """

""" VARIABLES********************************************************************************************************"""
# *VARIABLE DEFINITION: Variable "turnCalculator" starts from 0 and end up until the game ends.
# *OPERATIONS: (YES/NO): Yes, there is only plus "+" operation.
# *LIMITATIONS (YES/NO): YES, variable "howManyRounds" defines end round of the game.
# *PRINTING (YES/NO): YES, value is visible factor of the game.
# **********************************************************************************************************************
turnCalculator = 0
# **********************************************************************************************************************

# *VARIABLE DEFINITION: Variable runs in a loop between one player and "variable
# *OPERATIONS: (YES/NO): YES, There is minus "-" and plus "+" operations depending the conditions presented in the specification.
# *LIMITATIONS (YES/NO): YES, Variable "playerAmount" sets a higher limit.
# *PRINTING (YES/NO): YES, Variation "player" will printed out during the program's running.
# **********************************************************************************************************************
player = 0
# **********************************************************************************************************************

# *VARIABLE DEFINITION: Variable runs in a loop between one player and "variable
# *OPERATIONS: (YES/NO):There is minus "-" and plus "+" operations depending the conditions presented in the specification.
# *LIMITATIONS (YES/NO): NO, variable is limit.
# *PRINTING (YES/NO): YES, at beginning of the programm.
playerAmount = input("How many players you would like to have?  ")
# **********************************************************************************************************************

# *VARIABLE DEFINITION: Variable runs in a loop between one player and "variable
# *OPERATIONS: There is minus "-" and plus "+" operations depending the conditions presented in the specification.
# *LIMITATIONS (YES/NO): YES, Variable "playerAmount" sets a higher limit.
# *PRINTING (YES/NO):
howManyRounds = input("How many rounds you would like to have?  ")
# **********************************************************************************************************************


# *VARIABLE DEFINITION: Variable runs in a loop between one player and "variable
# *OPERATIONS: (YES/NO):There is minus "-" and plus "+" operations depending the conditions presented in the specification.
# *LIMITATIONS (YES/NO): NO, variable is limit.
# *PRINTING (YES/NO):
# i enables the loop from 1 to 100
# j enables the loop from 101 to 1000
# k enables the loop from 1001 to 10000
i = 1
j = 1
k = 1
# **********************************************************************************************************************
""" END OF THE VARIABLES*********************************************************************************************"""

""" FUCNTIONS********************************************************************************************************"""


# CHANGE NUMBER TO STRING:**********************************************************************************************
def changeNumberToStrings(n):
    num_str = str(n)
    sum = 0
    for i in range(0, len(num_str)):
        sum += int(num_str[i])
    return sum


pass


# RULES OF DIRECTION: DETERMINES ASCENDING OR DESCENDING DIRECTION******************************************************
def rulesOfDirections():
    global player
    global i
    global turnCalculator

    if i % 2 == 0:
        descendingCalculator()
    else:
        ascendingCalculator()


pass


# DESCENDING CALCULATOR*************************************************************************************************
def descendingCalculator():
    global turnCalculator
    global player
    global playerAmount

    if player == 1:
        player = playerAmount
    else:
        player -= 1

    turnCalculator += 1
    printOutTheOutput()


pass


# ASCENDING CALCULATOR**************************************************************************************************
def ascendingCalculator():
    global turnCalculator
    global player
    global playerAmount

    if player == playerAmount:
        player = 1
    else:
        player += 1
    turnCalculator += 1
    printOutTheOutput()


pass


# PRINT OUT THE OUTPUT**************************************************************************************************
def printOutTheOutput():
    global str_of_num
    global turnCalculator
    global player

    # This change turncalculator to string because it is easier discover number seven inside the variable
    str_of_num = str(turnCalculator)

    # The main condition which makes game to game
    if turnCalculator % 7 == 0 or '7' in str_of_num or changeNumberToStrings(turnCalculator) == 7:
        name = '"Martti Suosalo"'
        print "P:", player, "      ", name, ""
    else:
        print "P:", player, "      ", turnCalculator, ""


pass
"""ENF OF FUCNTIONS**************************************************************************************************"""

# MAIN PROGRAMM*********************************************************************************************************
while turnCalculator <= howManyRounds - 1:

    #  A loop from 1 to 10000
    if turnCalculator == 10 * i + i and turnCalculator <= 100:
        i += 1
        rulesOfDirections()
    else:
        rulesOfDirections()

    # A lopp from 101 to 1000  
    if turnCalculator == 100 * j + 10 * j + j and turnCalculator > 100 and turnCalculator <= 1000:
        j += 1
        rulesOfDirections()
    elif (turnCalculator > 100):
        rulesOfDirections()

    # A lopp from 1000 to 10000
    if turnCalculator == 1000 * k + 100 * k + 10 * k + k and turnCalculator > 1000 and turnCalculator <= 10000:
        k + 1
        rulesOfDirections()
    elif (turnCalculator > 1000):
        rulesOfDirections()
# END*******************************************************************************************************************
