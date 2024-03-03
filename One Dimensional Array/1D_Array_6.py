# 6. Add items from list into array using fromlist() method

#importing array module
from array import *

#creating extend() function which extends an array  in a given array
def FromListArray(arr,list1):
    arr.fromlist(list1)
    return arr
    
 
if __name__ == "__main__":
    mylist = [6,7,8,9,10]

    myarray = array("i",[1,2,3,4,5])
    myarray1 = FromListArray(myarray,mylist)

    print(myarray1)