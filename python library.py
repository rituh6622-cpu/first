# import numpy as np
# print("numpy import successfully")

# import numpy as np
# arr=np.array([1,2,3,4])
# print(arr)
# print(arr.dtype)              #datatype

# import numpy as np
# arr=np.array((1,2,3,4,5))
# print(arr)                      #use tupple to create array

# import numpy as np
# arr=np.array(32)                 # 0-d array
# print(arr)

# import numpy as np
# arr=np.array([1,2,3,4,5])          #1-d array
# print(arr)

# import numpy as np
# arr=np.array([[1,2,3,4],[5,6,7,8]])  #2-d array
# print(arr)

# import numpy as np
# arr=np.array([[[[1,2,3],[4,5,6],[6,7,8]]]])  #3-d array
# print(arr)

# import numpy as np
# a=np.array(40)
# b=np.array([[1,2,3],[4,5,6]])
# print(a .ndim)                           #number of dimensions
# print(b .ndim)

# import numpy as np
# arr= np.array([1,2,3,4,5,6,7,8,9])
#print(arr[5])                             #indexing
#print(arr[2:7])
#print(arr[:6])
#print(arr[5:])
#print(arr[-4:-1])                         #neg slicing
#print(arr[0:6:2])                           #step



# pandas - is a python library used for data manipulation and analysis
# print only the value (no index,no datatype)
# import pandas as pd
# data = [100,200,104]
# series = pd.Series(data)
# print(series.to_string(index=False))

# deafult index - pandas automatically create a index starting from 0
# import pandas as pd
# data=[5,10,15,20]
# series =pd.Series(data)
# print(series)

#custom index - default index replaced with your custom lable:a,b,c
# import pandas as pd
# data=[101,102,104]
# series= pd.Series(data
#                   index=["a","b","c"])
# print(series)


#series with float value
# import pandas as pd
# data=[101.1,102.1,103.1]
# series=pd.Series(data)
# print(series)

#series with string values
# import pandas as pd
# data=["A","B","C"]
# series=pd.Series(data)
# print(series)

#series with boolean value
# import pandas as pd
# data=[True,False,True]
# series=pd.Series(data)
# print(series)

# loc -loc stands for location by lable its read or update using the index lable
# import pandas as pd
# data=[10,20,30]
# series=pd.Series(data,
#                  index=["a","b","c"])
# print(series.loc["b"])

#iloc -index location ,used to access data using the position
# import pandas as pd
# data=[102,103,104]
# series=pd.Series(data,
#                  index=[0,1,2])
# print(series.iloc[1])

#filtering in series - we can filter values based on a condition
# import pandas as pd
# data=[100,101,102,201,202,203]
# series=pd.Series(data,
#                  index=["a","b","c","d","e","f"])
# print(series [series  >= 200]) 

#pandas series with dictionary and updating with loc

#series from dictionary
# import pandas as pd
# data={
#     "A": 201,
#     "B": 202,
#     "C": 203
# }
# series=pd.Series(data)
# print(series)

#updating value using loc
# import pandas as pd
# data={
#     "A": 100,
#     "B": 102,
#     "C": 103
# }
# series=pd.Series(data)
# # update the value for "A"
# series.loc["B"] +=5
# print(series.loc["B"])

#filtering 
# import pandas as pd
# calories={
#     "day 1": 1500,
#     "day 2": 1700,
#     "day 3": 2000
# }
# series=pd.Series(calories)
# print(series[series >=1700])

#creating dataframe - two dimensional labeled table made of rows and columns
# import pandas as pd
# data={
#     "name":["ritu","pooja","shruti"],
#     "age" :[20,20,18] ,
# }
# df =pd.DataFrame(data, index=["student1","student2","student3"])
# print(df)

#accesing rows-loc vs iloc 
# import pandas as pd
# data={
#     "name": ["ritu","pooja","shruti"],
#     "age": [20,20,18],
# }
# df=pd.DataFrame(data, index=["student1","student2","student3"])
# print(df.iloc[1])                 #using iloc
# print(df.loc["student1"])         #using loc


#adding a new column
# import pandas as pd
# data={
#     "name": ["ritu","pooja","shruti"],
#     "age": [20,20,18],
# }
# df=pd.DataFrame(data, index=["student1","student2","student3"])
# df["city"] =["rohtak","gohana","hisar"]
# print(df)

#adding a new row
# import pandas as pd
# data={
#     "name": ["ritu","pooja","shruti"],
#     "age": [20,20,18],
# }
# df=pd.DataFrame(data, index=["student1","student2","student3"])
# new_row= pd.DataFrame([{"name":"shweta","age":19,"city":"hisar"}])
# df= pd.concat([df, new_row])
# print(df)

#adding multiple rows(with custom index)
# import pandas as pd
# data={
#     "name": ["ritu","pooja","shruti"],
#     "age": [20,20,18]
# }
# df=pd.DataFrame(data, index=["student1","student2","student3"])
# new_row= pd.DataFrame([{"name":"shweta","age":19,"city":"hisar"},
#                        {"name":"shivani","age":18,"city":"hisar"}],
#                        index=["student4","student5"])
# df=pd.concat([df ,new_row])   
# print(df)       
# 

#matplotlib -is a powerfull python library that usesd for data visualization ,mainly for creating 2d plot and graphs
#low-level, high customizable but verbose

# import matplotlib.pyplot as plt
# x=[1,2,3,4,5]
# y=[2,4,6,8,10]

# plt.plot(x,y)
# plt.show()

import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[2,4,6,8,10]
plt.plot(x,y)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("simple line plot")
plt.show()






