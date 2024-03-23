# 3. Append any value to the array using append() method

#importing array module
from array import *

#creating fundction that appends new element
def AppendArray(arr,element):

    arr.append(6)
    return arr

#creating new array

my_array = array("i", [1,2,3,4,5])

print(AppendArray(my_array,6))