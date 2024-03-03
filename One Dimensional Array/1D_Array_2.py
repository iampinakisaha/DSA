# 2. Access individuat elements through indexes

#importing array module
from array import *

#creating fundtion to return array element on a pertivcular index position
def FindArray(arr,index):

    # if index position greater than or equal to total lenght of the array
    if index >= len(arr):
        print("Array IndexOutofBound:", end= " ")
        return 
    # else return array element in the index position
    else:
        return arr[index]

my_array = array("i",[1,2,3,4,5])

print(FindArray(my_array,5))

