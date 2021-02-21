print("\nLooping Calculator Program")

#FUNCTIONS
#Main menu function definition
def mainMenuLoader():
    """
    Print main menu options to screen

    Parameters:
        None
    Returns:
        Nothing
    """

    print("\n*************"
          "\n* Main Menu *"
          "\n*************"
          "\n1. Calculate the sum"
          "\n2. Calculate the product"
          "\n3. Calculate the exponent"
          "\n4. Calculate the modulo"
          "\nq. Exit program")
    return

#Functions to take float inputs for x and y
def xFloatCollector():
    """
    Casts input as float

    Parameters:
        None
    Returns:
        Nothing
    """
    global x
    x = float(input("Pick a number (it can be a decimal or an integer) and press [ENTER]: "))
    return
   
def yFloatCollector():
    """
    Casts input as float

    Parameters:
        None
    Returns:
        Nothing
    """
    global y
    y = float(input("Pick a number (it can be a decimal or an integer) and press [ENTER]: "))
    return

#Functions to take int inputs for x and y
def xIntCollector():
    """
    Casts input as integer

    Parameters:
        None
    Returns:
        Nothing
    """
    global x
    x = int(input("Pick a positive integer and press [ENTER]: "))
    return
    
def yIntCollector():
    """
    Casts input as integer

    Parameters:
        None
    Returns:
        Nothing
    """
    global y
    y = int(input("Pick a positive integer and press [ENTER]: "))
    return


#Addition function definition
#Note: the variable "answer" is assigned to a value that can be manipulated up until the point at which the final solution is obtained.
def sum(x,y):
    """
    Adds x and y

    Parameters:
        x (float)
        y (float)
    Returns:
        answer (float): x+y
    """
    answer = x + y
    return answer

#Product function definition
def prod(x,y):
    """
    Multiplies x and y

    Parameters:
        x (float)
        y (int)
    Returns:
        answer (float): x*y
    """
    answer = 0
    #As for loop counts up to y, the value of x is added each time
    for i in range(0,y):
        answer = answer + x
    return answer

#Exponent function definition
def exp(x,y):
    """
    Returns x**y

    Parameters:
        x (int)
        y (int)
    Returns:
        answer (int): x**y
    """
    #Special cases when input is 0
    if(y == 0):
        answer = 1
    elif(x == 0):
        answer = 0
    else:
        #As the exponent (y) increases, answer is multiplied by x input using prod(x,y) function from above
        answer = x
        for i in range(1,y): 
            answer = prod(x,answer)
    return answer

#Modulo function definition
#Value of y is repeatedly subtracted from x until answer=0 or answer<0. If answer<0 then value of y is added to give the solution
def modulo(x,y):
    """
    Returns x%y

    Parameters:
        x (float)
        y (float)
    Returns:
        answer (float): x%y
    """
    answer = x
    while(answer >= 0):
        answer = answer + -y
    if(answer == 0):
        answer = 0
    elif(answer < 0):
        answer = answer + y
    return answer



#MAIN BODY
mainMenuLoader()
menuItem = input("\nMake a selection and press [ENTER] ")

#Menu items: nested if-statment within while loop to avoid performing unnecessary calculations if user selects q
while(menuItem != "q"):

    #Menu item 1
    if(menuItem == "1"):
        #No further restrictions required, input can be any real number
        xFloatCollector()
        yFloatCollector()
        solution = sum(x,y)
        print("\nSOLUTION: " + str(x) + " + " + str(y) + " = {:.2f}".format(solution))
        print("\nReturning to Main Menu...")

    #Menu item 2
    elif(menuItem == "2"):
        xFloatCollector()
        yIntCollector()
        #Condition to ensure both x and y are positive
        while(x < 0 or y < 0):
            print("\nThat doesn't seem right!")
            print("Try again...\n")
            xFloatCollector()
            yIntCollector()
        #If condition is satisfied, come out of while loop and perform calculation
        solution = prod(x,y)
        print("\nSOLUTION: " + str(x) + " * " + str(y) + " = {:.2f}".format(solution))
        print("\nReturning to Main Menu...")
        
    #Menu item 3
    elif(menuItem == "3"):
        xIntCollector()
        yIntCollector()
        #Condition to ensure both x and y are positive
        while(x < 0 or y < 0):
            print("\nThat doesn't seem right!")
            print("Try again...\n")
            xIntCollector()
            yIntCollector()
        #Special case when inputs are 0
        if(x == 0 and y == 0):
            print("\nWe'll leave that one to the mathematicians...")
            print("\nReturning to Main Menu...")
        #If conditions are satisfied, perform calculation 
        else:
            solution = exp(x,y) 
            print("\nSOLUTION: " + str(x) + "^" + str(y) + " = {:.0f}".format(solution))
            print("\nReturning to Main Menu...")
            
    #Menu item 4
    elif(menuItem == "4"):
        xFloatCollector()
        yFloatCollector()
        #Condition to ensure that x and y are both positive and x > y   
        while(x <= 0 or y <= 0 or x < y):
            print("\nThat doesn't seem right!")
            print("Try again...\n")
            xFloatCollector()
            yFloatCollector()
        #If conditions are satisfied, perform calculation
        solution = modulo(x,y)
        print("\nSOLUTION: " + str(x) + " % " + str(y) + " = {:.2f}".format(solution))
        print("\nReturning to Main Menu...")
       
    #Error message: if neither 1, 2, 3, 4 or q is selected
    else:
        print("\nError!")
        print("Please try again...")

    mainMenuLoader()
    menuItem = input("\nMake a selection and press [ENTER] ")

#If q is selected:
print("\nExiting program...")
exit()
