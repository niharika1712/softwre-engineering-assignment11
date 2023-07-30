"""
python3
Title: Calculate Fermat's Last Theorem Near Misses
Filename: nearmiss.py
Necessary files: N/A
Created external files: nearmisses.exe, it is an executable file for windows platform
Name: Niharika Akula, Nikhilesh Yadav Vanguru
Email: NiharikaAkula@lewisu.edu, NikhileshYadavVang@lewisu.edu
Course, Sections: Software Engineering - SU23-CPSC-60500-002
Date: 07-29-2023
Program Explanation: calculate near misses with user input using Farmat's Last Theorem formula
    of the form (x, y, z, n, k) in the formula x^n + y^n = z^n, where x, y, z, n, k
    are positive integers, 2< n <12, 10 <= x <= k, and 10 <= y <= k 
Resource : N/A
"""

def NearMisses():
    """
    Calculate near misses using the Fermat's Last Theorem formula x^n + y^n = z^n,
    and display the minimum miss on the screen to the user
    """
    # get user input of the limit values
    n = int(input("\nEnter Exponent value: "))
    while n>11 or n<3:
        # check if exponent value is between 2 and 12
        n = int(input("Re-enter the Exponent value in between 2 and 12: "))

    k = int(input("Enter Limit value: "))
    while k<11:
        # check if Limit value is bigger than 10
        k = int(input("Re-enter the Limit Value bigger than 10: "))
    
    print("Results of near misses\n")

    # initialize relative miss variable with value of -1 wbfore calculation
    relative_miss = -1
    # loop for first variable x of method x^n + y^n = z^n
    for x in range(10, k):
        # loop for the second variable y of method x^n + y^n = z^n
        for y in range(10, k):
            # calculate (x^n + y^n)
            xy = pow(x, n) + pow(y, n)
            # get z and z+1
            z = int(pow(xy, 1/n))
            # exponent vlue of z
            ze = pow(z, n)
            # exponent vlue of z+1
            z1e = pow(z+1, n)
            # calculate miss and relative miss
            miss = min( xy - ze, z1e - xy)
            relative_miss2 = miss / xy

            # dsiplay to the screen for every small relative miss
            if relative_miss == -1 or relative_miss > relative_miss2: 
                # get the minimum relative miss
                relative_miss = relative_miss2
                print(f"x: {x}\ty: {y}\tz: {z}\tMiss: {miss}\tRelative Miss: {round(relative_miss*100,2)}%")
    
    # display the final result
    print("\nFinal Result Near Miss: \n") 
    print(f"x: {x}\ty{y}\tz: {z}\tMiss: {miss}\tRelative Miss: {round(relative_miss*100,2)}%")

    wait = input("\nEnter any key for Exit: ")


# start the program by calling the calculation method
NearMisses()