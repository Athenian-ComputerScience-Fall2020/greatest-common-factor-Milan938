# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  None

def find_gcf(x,y):   # Do not change function name!
    factor = x
    while factor > 0:
        if (x%factor) == 0:
            if (y%factor) == 0:
                return factor

        factor = factor - 1
    

    



if __name__ == '__main__':
    # Test your code with this first
    # Change the argument to try different values
    print(find_gcf(21, 14))

    # After you are satisfied with your results, use input() to prompt the user for two values:
    #x = int(input("Enter a number: "))
    #y = int(input("Enter another number: "))

