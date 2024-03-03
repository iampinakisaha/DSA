# 7. Remove any array element using remove() method

#importing array module
from array import *

#creating extend() function which extends an array  in a given array
def RemoveArray(arr,element):
    if element not in arr:
        print("Array element not found", end=" ")
        return -1
    else:
        arr.remove(element)
        return arr
    
 
if __name__ == "__main__":
    myarray = array("i",[1,2,3,4,3,5])
    print(f"Array:{myarray}")
    element = int(input("enter the element you want to remove: "))
    
    print(RemoveArray(myarray,element))