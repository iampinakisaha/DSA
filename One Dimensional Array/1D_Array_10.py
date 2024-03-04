# 10. Reverse a python array using reverse() method

#importing array module
from array import *

#creating function which Reverse a python array using reverse() method
def ReverseArray(arr):
    arr.reverse()
    return arr
    
 
if __name__ == "__main__":
    myarray = array("i",[1,2,3,4,3,5])
    
    print(ReverseArray(myarray))