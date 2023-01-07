from array import *
#'i' = INT
#'d' = FLOAT
a =array('d', [1.2,3.4,20.6,7.8,9.10])
a.append(5)
print("a= ", a)

b =array('i', [1,2,3,4,5,6,7,8,9,10])
b.extend([17,13,14])
print("b= ", b)

c =array('i', [1,2,3,4,5,6,7,8,9,10])
c.insert(2, 104)
print("c= ", c)
