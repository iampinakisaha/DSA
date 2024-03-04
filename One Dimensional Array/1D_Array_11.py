# 11. Get array buffer information through buffer_info() method

#importing array module
from array import *

myarray = array("i",[1,2,3,4,3,5])

print(myarray.buffer_info())
