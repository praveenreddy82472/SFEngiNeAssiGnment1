"""
Program Title : Near Misses
Name of the file : Assignment 1
Name of the Programmer: [Thumati Praveen Kumar] [Kasoju Mani Rathnam]
Student Email Address : [praveenkthumati@lewisu.edu] [manirathnamkasoju@lewisu.edu]
Explanation of the Program : the Program searchs for  near miss with the value of n and K. the n value should be between 2 and 12 , and k value should be 
                                greater than 10. if theses two conditions are statisfied then it will search for near misses. it works on the formula given 
                                in the requirement to calculate the near misses
"""


# the n and k values are set to be 1
n_value = 1
k_value = 1

def main1():
    
    while True:
        # getting input from the user
        n_value = int(input("Enter value for n such that 2 < n < 12: "))
        
        # the loop has been create to check the condition
        if ((n_value <= 2) or (n_value >= 12)):
            print("Invalid input! enter a number between 2 and 12")
        else:
                # getting k value from the user 
                k_value= int(input("Enter upper limit k for x and y (k > 10): "))
                if k_value >= 10:
                    past_miss=None 
                    for x in range(10, k_value+1): 
                        for y in range(x,k_value+1): 
                            pow_var = pow(x, n_value) + pow(y, n_value)
                            z = int(pow(pow_var, 1/n_value))
                            pow_of_z = pow(z, n_value)
                            pow_z = pow(z+1, n_value)
                            miss_value = min( pow_var - pow_of_z, pow_z - pow_var)
                            miss_rel = miss_value/pow_var
                            rel_mis = miss_rel
                            print("\nx = {} y = {}  z = {}  Miss = {}  Relative Miss = {}%".format(x, y, z, miss_value, round(rel_mis*100,2)))
                    break
                else:
                    print("Invalid input!!!! enter a number greater than 10")
                    
                    
main1()
