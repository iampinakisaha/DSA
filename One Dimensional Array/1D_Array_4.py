# 4. Insert value in an array using insert() method

#importing array module
from array import *

#creating insert function which inserts an array element in a given position
def InsertArray(arr,index,value):

    if index < 0 or index > len(arr):
        print("ArrayIndexOutOfBound:", end = " ")
        return -1
    else:
        arr.insert(index,value)
        return arr
 
if __name__ == "__main__":
    a = [1,2,3,4,5]
    myarray = array("i",a)

    print(InsertArray(myarray,6,10))