# 8. Remove last array element using pop() method

#importing array module
from array import *

#creating insert function which Remove last array element using pop() method
def PopArray(arr):

    arr.pop()
    return arr
 
if __name__ == "__main__":

    
    a = [1,2,3,4,5]
    myarray = array("i",a)
    print(f"Before pop() : {myarray}")
    print(f"After pop(): {PopArray(myarray)}")