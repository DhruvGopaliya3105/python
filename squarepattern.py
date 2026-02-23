
# 1 2 3 4  
# 1 2 3 4  
# 1 2 3 4  
# 1 2 3 4

# for i in range(1,5):
#     for j in range(1,5):
#         print(j,end=" ")
#     print(" ") 


# 1 1 1 1  
# 2 2 2 2  
# 3 3 3 3
# 4 4 4 4

# for i in range(1,5):
#     for j in range(1,5):
#         print(i,end=" ")
#     print(" ")  

# 4 4 4 4  
# 3 3 3 3  
# 2 2 2 2
# 1 1 1 1  

# for i in range(4,0,-1):
#     for j in range(1,5):
#         print(i,end=" ")
#     print(" ")    


# 4 3 2 1  
# 4 3 2 1  
# 4 3 2 1
# 4 3 2 1

# for i in range(1,5):
#     for j in range(4,0,-1):
#         print(j,end=" ")
#     print(" ")  

  
# 1 3 5 7  
# 1 3 5 7  
# 1 3 5 7
# 1 3 5 7


# for i in range(1,5):
#     temp=1
#     for j in range(1,5):                 direct method by a variable
#         print(temp,end=" ")
#         temp+=2
#     print(" ")  

# for i in range(1,5):
#     for j in range(1,8,2):                  by slicing method give it a range in j change in j line
#         print(j,end=" ")
#     print(" ")      

# 7 5 3 1  
# 7 5 3 1  
# 7 5 3 1
# 7 5 3 1

# n = 4
# for i in range(1,5):
#     for j in range(2*n-1,0,-2):               by slicing method 
#         print(j,end=" ")
#     print(" ")    

# for i in range(1,5):
#     for j in range(7,0,-2):                     by slicing  method without n  
#         print(j,end=" ")
#     print(" ")  

# for i in range(1,5):
#     temp = 7
#     for j  in range(1,5):                          by a third variable
#         print(temp,end=" ")
#         temp-=2
#     print(" ")  


# 2 4 6 8  
# 2 4 6 8  
# 2 4 6 8
# 2 4 6 8

# for i in range(1,5):
#     for j in range(2,9,2):
#         print(j,end=" ")
#     print(" ")  

# 8 6 4 2  
# 8 6 4 2  
# 8 6 4 2
# 8 6 4 2

# for i in range(1,5):
#     for j in range(8,1,-2):
#         print(j,end=" ")
#     print(" ")        


# 1 2 3 4  
# 5 6 7 8  
# 9 10 11 12
# 13 14 15 16

# temp = 1
# for i in range(1,5):
#     for j in range(1,5):
#         print(temp,end=" ")
#         temp+=1
#     print(" ") 

# 16 15 14 13  
# 12 11 10 9  
# 8 7 6 5
# 4 3 2 1 

# n = 4
# temp = n*n
# for i in range(1,5):
#     for j in range(1,5):
#         print(temp,end=" ")
#         temp-=1
#     print(" ") 

# 1 3 5 7  
# 9 11 13 15  
# 17 19 21 23
# 25 27 29 31      

# temp = 1
# for i in range(1,5):
#     for j in range(1,5):
#         print(temp,end=" ")
#         temp+=2
#     print(" ") 

# 31 29 27 25  
# 23 21 19 17  
# 15 13 11 9
# 7 5 3 1   

# n = 4
# temp = n*n*2-1
# for i in range(1,5):
#     for j in range(1,5):
#         print(temp,end=" ")
#         temp-=2
#     print(" ")  

# 2 4 6 8  
# 10 12 14 16  
# 18 20 22 24
# 26 28 30 32  

# temp = 2
# for i in range(1,5):
#     for j in range(1,5):
#         print(temp,end=" ")
#         temp+=2
#     print(" ") 


# 32 30 28 26  
# 24 22 20 18  
# 16 14 12 10
# 8 6 4 2  
 
# n = 4
# temp = n*n*2
# for i in range(1,5):
#     for j in range(1,5):
#         print(temp,end=" ")
#         temp-=2
#     print(" ") 


# A B C D  
# A B C D  
# A B C D
# A B C D

# for i in range(1,5):
#     for j in range(1,5):
#         print(chr(65+j-1),end=" ")
#     print(" ")   

# A A A A  
# B B B B  
# C C C C
# D D D D    

# for i in range(1,5):
#     for j in range(1,5):
#         print(chr(65+i-1),end=" ")
#     print(" ")   

# D C B A  
# D C B A  
# D C B A
# D C B A

# for i in range(1,5):
#     for j in range(4,0,-1   ):
#         print(chr(65+j-1),end=" ")
#     print(" ")  

# D D D D  
# C C C C  
# B B B B
# A A A A

# for i in range(4,0,-1):
#     for j in range(1,5):
#         print(chr(65+i-1),end=" ")
#     print(" ")   

# P O N M  
# L K J I  
# H G F E
# D C B A    

# n = 4
# temp = n*n
# for i in range(1,5):
#     for j in range(1,5):
#         print(chr(65+temp-1),end=" ")
#         temp-=1
#     print(" ")    


# A B C D  
# E F G H  
# I J K L
# M N O P

# temp = 1
# for i in range(1,5):
#     for j in range(1,5):
#         print(chr(65+temp-1),end=" ")
#         temp+=1
#     print(" ")      

