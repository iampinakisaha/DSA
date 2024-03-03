# 5. Extend python array using extend() method

#importing array module
from array import *

#creating extend() function which extends an array  in a given array
def ExtendArray(arr1,arr2):

    arr1.extend(arr2)
    return arr1
 
if __name__ == "__main__":
    a = [1,2,3,4,5]
    b= [6,7,8]
    myarray1 = array("i",a)
    myarray2 = array("i",b)

    print(ExtendArray(myarray1,myarray2))