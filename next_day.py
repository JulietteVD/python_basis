##
## Next day function
## Juliette Vintrou , id = 118 105 792
## Wednesday 10th October 2018
## CS 4801 - Introduction to Python , UCC
## Assignment 2
##


## Definition of the functions

def leap_year(y):
    """
    Return True if this is a leap year

    Leap Year     : 366 days (leap year are divisible by 4 but not
                              by 100 unless it's divisible by 400)

    Input : y (int)
    Output : is_leap_year (boolean)
    
    """
    is_leap_year = False

    if ((y % 4) == 0 ) & (( (y % 100) != 0) or ( (y % 400) == 0)) :
        is_leap_year = True

    return is_leap_year

def next_day(d,m,y):
    """
    This function nex_day returns the following day taking care of the end
    of the month, of the year and leap years.

    31 days    : January (01), March (03), Mai (05), July (07), August (08),
                 October (10), December (12)
    30 days    : April (04), June (06), September (09), November (11)
    28/29 days : February (02)

    Leap Year     : 366 days (leap year are divisible by 4 but not
                              by 100 unless it's divisible by 400)
    Not Leap year : 365 days


    Input  : d , m , y (int, int, int)
    Output : d1, m1 , y1 (int, int, int)

    Example: next_day(28,02,1998)

        day :28
        month :02
        year :1998
        The following day is : 1/3/1998
    
    """
    d_after, m_after , y_after = d , m , y
    leap = leap_year (y)
    
     # If 31st of important month ==> 1st of the following month 
    if (d == 31) & ( m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10) :
        d_after = 1
        m_after = m + 1
        
     # If 31st december ==> 1st january of the following year
    if (d == 31) & (m == 12) :
        d_after = 1
        m_after = 1
        y_after = y + 1
        
     # If 30th of imporant month ==> 1st of the following month
    if (d == 30) & ( m == 4 or m == 6 or m == 9 or m == 11) :
        d_after = 1
        m_after = m + 1
       
     # If not 31st of the important month ==> day +1
    if (d < 31) & ( m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12) :
        d_after = d + 1
      
     # If no 30th of the important month ==> day + 1   
    if (d < 30) & ( m == 4 or m == 6 or m == 9 or m == 11) :
        d_after = d + 1
      
     # If 366 days and february and 29 ==> 1st march   
    if (leap == True) & (m == 2) & (d == 29) :
        d_after = 1
        m_after = m + 1
    
     # If 366 days and february and not 29 ==> day + 1 
    if (leap == True) & (m == 2) & (d < 29) :
        d_after = d + 1
     
     # If 365 days and february and 28 ==> 1st march    
    if (leap == False) & (m == 2) & (d == 28) :
        d_after = 1
        m_after = m + 1

     # If 365 days and february and not 28 ==> day + 1    
    if (leap == False) & (m == 2) & (d < 28) :
        d_after = d + 1
        
    return d_after,m_after,y_after

## Start the program with a printing function        
print("cs 4801 , assigmnemt 2 : next year function")

## Ask the user to enter parameters
print("Which date do you want to enter ?")
d = int(input("day :"))
m = int(input("month :"))
y = int(input("year :"))

## Call the function 
d_after , m_after , y_after = next_day( d , m , y )

print("The following day is : "+ str(d_after)+"/"+str(m_after)+"/"+str(y_after))


