#ans 1 
#numpy is a python libraryused for working with arrays and mathematical operations.
#advantages: faster than python lists,uses less memory.

#ans 2
#np.array()

#ans 3
# import numpy as np
# arr= np.arange(1, 11)
# print(arr)

#ans 4
# import numpy as np
# arr =np.arange(2,21,2)
# print(arr)

#ans 5
# import numpy as np
# arr = np.array([10,20,30,40,50])
# print(arr)

#ans 6
# import numpy as np
# arr =np.array([10,20,30,])
# print(arr.dtype)

#ans 7
# import numpy as np
# arr =np.array([5,10,15,20,25])
# print(arr.size)

#ans 8
# import numpy as np 
# arr= np.array([[1,2,3],[4,5,6]])
# print(arr)

#ans 9
#python list -slower,more memory,cannot perform vector operation directly
#numpy array -faster,less memory, supports vector operations

#ans 10
# import numpy as np
# arr = np.zeros(5)
# print(arr)

#ans 11
# the .shape attribute is used to find the dimensions of a numpy array.

#ans 12
# import numpy as np
# arr=np.array([[1,2,3],[4,5,6]])
# print(arr.shape)

#ans 13
# import numpy as np
# arr =np.arange(1,13)
# print(arr.reshape(3,4))

#ans 14
# import numpy as np
# arr =np.arange(1,13)
# print(arr.reshape(2,6))

#ans 15
#if reshape dimension do not match the total number of elements,python raise a value error

#ans 16
# import numpy as np
# arr= np.array([1,2,3,4,5,6])
# arr2= arr.reshape(2,3)
# print(arr2)

#ans 17
# import numpy as np
# arr = np.arange(1,9)
# arr= arr.reshape(4,2)
# print(arr)

#ans 18
# import numpy as np
# arr=np.arange(1,13)
# print("original shape:",arr.shape)
# print("reshaped shape:",arr.reshape(3,4))

#ans 19
#np.concatenate function is used to join two numpy array.

#ans 20
# import numpy as np
# arr1= np.array([1,2,3])
# arr2=np.array([4,5,6])
# arr= np.concatenate((arr1,arr2))
# print(arr)

#ans 21
# import numpy as np
# arr1 =np.array([[1,2],[3,4]])
# arr2 =np.array([[5,6],[7,8]])
# result =np.vstack((arr1,arr2))
# print(result)

#ans 23
#concatenate()- joins existing array ,number of dimension remain same , used for simple joining 
#np.stack -joins arrays by creating a new axis ,number of dimension inc by 1, used to create a new dimension

#ans 24
#np.split function used to split a numpy array

#ans 25
# import numpy as np 
# arr= np.array([1,2,3,4,5])
# print(np.array_split(arr,3))

#ans 27
# matplotlib is a python library used for creating graphs,charts ,and data visualizations

#ans 28
#plt.plot() used to draw a line graph

#ans 33
# for i in range (1,6):
#     print("*" * i)

#ans 34
# for i in range(5,0,-1):
#     print("*" * i)

#ans 35
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j, end="")
#     print()    

#ans 36
# for i in range(1,6):
#     for j in range(i):
#         print(chr(65+j), end="")
#     print()    

#ans 37
# for i in range(1,6):
#     print(str(i) *i)

#ans 38
# for i in range (1,6):
#     print(" "*(5-i)+ "*"*(2*i-1))

#ans 39
# for i in range(5,0,-1):
#     print(" "*(5-i)+ "*"*i)

#ans 40
n=5

for i in range(1,n+1):
    print(" "*(n-i)+"*"*(2*i-1))

for i in range(n-1,0,-1) :
    print(" "*(n-i)+"*"*(2*i-1))   

                
