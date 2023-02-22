# python3

import sys
import threading


def compute_height(n, parents):
    
    # Write this function
    #max_height = 0
   
    trees = [[] for _ in range(n)]
    root = None

    for i, par in enumerate(parents):
        if par == -1:
            root = i
        else:
            trees[par].append(i)

    def maxheight(node):
        if not trees[node]:
            return 1
        else:
            height = [maxheight(x) for x in trees[node]]
            return 1 + max(height)
    #return max_height
    return maxheight(root)




def main():
    # implement input form keyboard and from files
    imp = input("Enter 'I' or 'F' : ")
    if "I" in imp:
        # input number of elements
        n = int(input())
        # input values in one variable, separate with space, split these values in an array
        pon = list(map(int, input().split()))
    elif "F" in imp:
        # let user input file name to use, don't allow file names with letter a
        # account for github input inprecision
        #while True:
        path = '/DA-testa/tree-height-from-empty-AlinaKrasnova171RMC069/tree/main/test/'
        file = input("Enter file name: ")
        folder = path + file
        if "a" not in file:
            try:
                with open(folder) as fl:
                    n = int(fl.readline())
                    pon = list(map(int, fl.readline().split()))
            except FileNotFoundError:
                print("Error: file not found ")
                return

        else:
            print("Error")

        
    else:
        print("Enter 'I' or 'F' : ")
        return

    
    # call the function and output it's result
    print(compute_height(n, pon))
# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
