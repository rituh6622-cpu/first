#right triangle

# for i in range (1,6):
#     for j in range (i):
#         print("*" ,end=" ")
#     print()    

#square pattern
# for i in range (5):
#     for j in range(5):
#         print("*" ,end=" ")
#     print()    

#inverted right triangle
# for i in range(6,0,-1):
#     for j in range(i):
#         print("*", end=" ")
#     print()    

#number triangle pattern
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j     ,end=" ")
#     print()

#hollow square pattern
# for i in range (5):
#     for j in range (5):
#         if i==0 or i==4 or j==0 or j==4:
#             print("*", end=" ")
#         else:
#             print(" ",end=" ")
#     print()          
#    
#pyramid triangle
# n=5
# for i in range(1,n+1):
#     print(" "* (n-i)+"*" * (2* i-1))

# #inverted pyramid
# n=5
# for i in range(n,0,-1):
#     print(" " * (n-i) +"*"* (2*i-1))

#diamond pattern
# n=5
# for i in range(1,n+1):
#     print(" "*(n-i) +"*"*(2*i-1))
# for i in range (n-1,0,-1): 
#     print(" "*(n-i)+ "*"* (2*i-1))

#floyd triangle
rows=5
num =1
# for i in range (1,rows + 1):
#     for j in range(i):
#         print(num ,end=" ")
#         num += 1
#     print()    