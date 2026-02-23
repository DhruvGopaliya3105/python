

#       *        
#     *   *      
#   *       *    
# * * * * * * * 

# for i in range(1,5):
#     for j in range(1,8):
#         if i==4 or i+j==5 or j-i==3:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print(" ")            




# * * * * * * *  
#   *       *    
#     *   *      
#       *

# for i in range(1,5):
#     for j in range(1,8):
#         if i==1 or i==j or i+j==8:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print(" ")  




#             * * * * * * *  
#           *           *  
#         *           *  
#       *           *  
#     *           *  
#   *           *  
# * * * * * * *  
    

# for i in range(1,8):
#     for sp in range(1,8-i):
#         print(" ",end=" ")
#     for j in range(1,8):
#         if i==1 or i==7 or j==1 or j==7:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print(" ")                                 





# * * * *  
#  * * *  
#   * *  
#    *  
#   * *  
#  * * *  
# * * * * 

# for i in range(4,0,-1):
#     for sp in range(1,5-i):
#         print(" ",end="")
#     for j in range(1,i+1):
#         print("*",end=" ") 
#     print(" ") 
      
# for i in range(2,5):
#         for sp in range(1,5-i):
#             print(" ",end="")
#         for j in range(1,i+1):
#             print("*",end=" ")
#         print(" ") 

# D D D D  
#  C C C  
#   B B  
#    A  
#   B B  
#  C C C  
# D D D D

# for i in range(4,0,-1):
#     for sp in range(1,5-i):
#         print(" ",end="")
#     for j in range(1,i+1):
#         print(chr(65+i-1),end=" ")
#     print(" ")
# for i in range(2,5):
#     for sp in range(1,5-i):
#         print(" ",end="")
#     for j in range(1,i+1):
#         print(chr(65+i-1),end=" ")
#     print(" ")   




#       *        
#     *   *      
#   *       *    
# *           *  
#   *       *    
#     *   *      
#       *     


# for i in range(1,8):
#     for j in range(1,8):
#         if i+j==5 or j-i==3 or i-j==3 or  i+j==11:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print(" ")                             
      
      
#       1        
#     2   2      
#   3       3    
# 4 4 4 4 4 4 4  

# for i in range(1,5):
#     for j in range(1,8):
#         if i==4 or i+j==5 or j-i==3:
#             # print(i,end=" ")
#         else:
#             print(" ",end=" ")
#     print(" ") 



#       4 
#     3   3 
#   2       2 
# 1 1 1 1 1 1 1 


    
# for i in range(4, 0, -1):

#     # spaces
#     for j in range(i - 1):
#         print("  ", end="")

#     # numbers
#     for j in range(1, 8 - 2 * (i - 1)):
#         if i == 1 or j == 1 or j == 7 - 2 * (i - 1):
#             print(i, end=" ")
#         else:
#             print("  ", end="")

#     print()







#       A        
#     B   B      
#   C       C    
# D D D D D D D  


# for i in range(1,5):
#     for j in range(1,8):
#         if i==4 or i+j==5 or j-i==3:
#             print(chr( 65+i-1),end=" ")
#         else:
#             print(" ",end=" ")
#     print(" ") 












