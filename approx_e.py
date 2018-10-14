##
## Approximation of the quantity exp(x) function
## Juliette Vintrou , id = 118 105 792
## Wednesday 10th October 2018
## CS 4801 - Introduction to Python , UCC
## Assignment 2
##


## Definition of the function

def approx_e(x):
    """
    This function give us the approximation of the quantity exp(x)

    Input : x (float)
    Output : res (float)
    
    Example:  res = approx_e (1)
    
    exp(x) :1
    The following approximation is : 2.7182818284590455

    """

    MAX = 151
    factorial = 0
    prod = 0
    res = 0

    for i in range (0,MAX) :
        if i == 0 :
            factorial = 1
            prod = 1
            res = res + (prod)/factorial 
        else :
            factorial = i * factorial
            prod = x * prod
            res = res + (prod)/factorial
            
    return res

## Start the program with a printing function        
print("cs 4801 , assigmnemt 2 : approximation exponential")

## Ask the user to enter parameters
print("Enter an exponential that you want to know the approximation")
x = float((input("exp(x) :")))

## Call the function 
res = approx_e(x)

print("The following approximation is : "+ str(res))


