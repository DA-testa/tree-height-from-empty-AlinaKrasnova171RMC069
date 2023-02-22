# python3

import sys
import threading
from tkinter import filedialog
#import tkinter as log


def compute_height(n, parents):
    
    # Write this function
    #max_height = 0
    # Your code here
    #return max_height
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

    return maxheight(root)




def main():
    imp = input("Enter 'I' or 'F' : ")
    if "I" in imp:
        n = int(input())
        pon = list(map(int, input().split()))
    elif "F" in imp:
        root = filedialog.Tk()
        root.withdraw()
        f = filedialog.askopenfilename()
        with open(f) as file:
            n = int(file.readline())
            pon = list(map(int, file.readline().split()))
    else:
        print("Enter 'I' or 'F' : ")
        return

    # implement input form keyboard and from files
    
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result

    print(compute_height(n, pon))
# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
