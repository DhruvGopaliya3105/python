
# 1  
# 1 2  
# 1 2 3  
# 1 2 3 4 

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print(" ") 

# 1  
# 2 2
# 3 3 3
# 4 4 4 4

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print(" ")  

# 4  
# 3 3
# 2 2 2
# 1 1 1 1     

# for i in range(4,0,-1):
#     for j in range(1,6-i):
#         print(i,end=" ")
#     print(" ")  

# 1  
# 2 3
# 4 5 6
# 7 8 9 10  

# temp = 1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(temp,end=" ")
#         temp+=1
#     print(" ")

# 10  
# 9 8
# 7 6 5
# 4 3 2 1

# n = 4
# temp = n*(n+1)//2
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(temp,end=" ")
#         temp-=1
#     print(" ") 

# 1  
# 3 5
# 7 9 11
# 13 15 17 19               

# temp = 1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(temp,end=" ")
#         temp+=2
#     print(" ")  

# 19  
# 17 15
# 13 11 9
# 7 5 3 1  

# n = 4
# temp = n*(n+1)-1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(temp,end=" ")
#         temp-=2
#     print(" ")  


# 2
# 4 6
# 8 10 12
# 14 16 18 20

# temp = 2
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(temp,end=" ")
#         temp+=2
#     print(" ")  


# 20
# 18 16
# 14 12 10
# 8 6 4 2

# n = 4
# temp = n*(n+1)
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(temp,end=" ")
#         temp-=2
#     print(" ")

# 1 2 3 4  
# 1 2 3
# 1 2
# 1

# for i in range(1,5):
#     for j in range(1,6-i):
#         print(j,end=" ")
#     print(" ")  


# 1 1 1 1  
# 2 2 2
# 3 3
# 4

# for i in range(1,5):
#     for j in range(1,6-i):
#         print(i,end=" ")
#     print(" ")


# 4 4 4 4  
# 3 3 3
# 2 2
# 1

# for i in range(4,0,-1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print(" ")          
  
  
# 1 2 3 4  
# 5 6 7
# 8 9
# 10

# temp = 1
# for i in range(1,5):
#     for j in range(1,6-i):
#         print(temp,end=" ")
#         temp+=1
#     print(' ') 

# 10 9 8 7  
# 6 5 4
# 3 2
# 1

# temp = 10
# for i in range(1,5): 
#     for j in range(1,6-i):
#         print(temp,end=" ")
#         temp-=1
#     print(" ")  


# 1 3 5 7  
# 9 11 13
# 15 17
# 19

# temp = 1
# for i in range(1,5):
#     for j in range(1,6-i):
#         print(temp,end=" ")
#         temp+=2
#     print(" ")    


# 19 17 15 13  
# 11 9 7
# 5 3
# 1
# temp = 19
# for i in range(1,5):
#     for j in range(1,6-i):
#         print(temp,end=" ")
#         temp-=2
#     print(" ")   

# 2 4 6 8  
# 10 12 14
# 16 18
# 20             

# temp = 2
# for i in range(1,5):
#     for j in range(1,6-i):
#         print(temp,end=" ")
#         temp+=2
#     print(" ") 

# 20 18 16 14  
# 12 10 8
# 6 4
# 2

# n = 4
# temp = n*(n+1)
# for i in range(1,5):
#     for j in range(1,6-i):
#         print(temp,end=" ")
#         temp-=2
#     print(" ") 

#       1  
#     2 1
#   3 2 1
# 4 3 2 1  

# for i in range(1,5):
#     for sp in range(1,5-i):
#         print(" ",end=" ")
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print(" ")                  


#       1  
#     2 2
#   3 3 3
# 4 4 4 4

# for i in range(1,5):
    # for sp in range(1,5-i):
    #     print(" ",end=" ")
    # for j in range(1,i+1):
    #     print(i,end=" ")
    # print(" ")    
    
#       4  
#     3 3
#   2 2 2
# 1 1 1 1
    
# for i in range(4,0,-1):
#     for sp in range(1,i):
#         print(" ",end=" ")
#     for j in range(1,6-i):
#         print(i,end=" ")
#     print(" ")  

#       1  
#     2 3
#   4 5 6
# 7 8 9 10              

# temp = 1
# for i in range(1,5):
#     for sp in range(1,5-i):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print(temp,end=" ")
#         temp+=1
#     print(" ") 

#       10  
#     9 8
#   7 6 5
# 4 3 2 1   

# temp = 10
# for i in range(1,5):
#     for sp in range(1,5-i):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print(temp,end=" ")
#         temp-=1
#     print(" ")    
    
    
#         1  
#       3  5
#    7  9 11
# 13 15 17 19
# temp = 1
# for i in range(1,5):
#     for sp in range(1,5-i):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print(temp,end=" ")
#         temp+=2
#     print(" ")    

#         19  
#     17 15
#   13 11 9
# 7  5 3 1


# n = 4
# temp = n*(n+1)-1
# for i in range(1,5):
#     for sp in range(1,5-i):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print(temp,end=" ")
#         temp-=2
#     print(" ")   

     


#         2  
#      4  6
#   8  10 12
# 14 16 18 20
 
# temp = 2
# for i in range(1,5):
#     for sp in range(1,5-i):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print(temp,end=" ")
#         temp+=2
#     print(" ") 



#          20  
#       18 16
#   14  12  10
# 8  6   4   2

# n = 4
# temp = n*(n+1)
# for i in range(1,5):
#     for sp in range(1,5-i):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print(temp,end=" ")
#         temp-=2
#     print(" ")  


# 4 3 2 1  
#   3 2 1
#     2 1
#       1

# for i in range(4,0,-1):
#     for sp in range(1,5-i):
#         print(" ",end=" ")
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print(" ")   


# 1 1 1 1  
#   2 2 2
#     3 3
#       4

# for i in range(1,5):
#     for sp in range(1,i):
#         print(" ",end=" ")
#     for j in range(1,6-i):
#         print(i,end=" ")
#     print(" ")   
    
    # 4 4 4 4
    #   3 3 3
    #     2 2
    #       1
    
# for i in range(4,0,-1):
#     for sp in range(1,5-i):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print(i,end=" ")
    # print(" ")
    
    # 1 2 3 4
    #   5 6 7
    #     8 9
    #      10 
    
# temp = 1
# for i in range(1,5):
#     for sp in range(1,i):
#         print(" ",end=" ")
#     for j in range(1,6-i):
#         print(temp,end=" ")
#         temp+=1
#     print(" ")    

# 10 9 8 7
#   6 5 4
#     3 2
#       1

# temp = 10
# for i in range(1,5):
#     for sp in range(1,i):
#         print(" ",end=" ")
#     for j in range(1,6-i):
#         print(temp,end=" ")
#         temp-=1
#     print(" ") 


    # 1 3 5 7
    #   9 11 13
    #     15 17
    #        19

# temp = 1
# for i in range(1,5):
#     for sp in range(1,i):
#         print(" ",end=" ")
#     for j in range(1,6-i):
#         print(temp,end=" ")
#         temp+=2
#     print(" ") 


# 19 17 15 13
#      11 9 7
#         5 3
#          1            
# n = 4         
# temp = n*(n+1)-1
# for i in range(1,5):
#     for sp in range(1,i):
#         print(" ",end=" ")
#     for j in range(1,6-i):
#         print(temp,end=" ")
#         temp-=2
#     print(" ")


#    2 4 6 8
#     10 12 14
#        16 18
#          20
    
# temp = 2    
# for i in range(1,5):
#     for sp in range(1,i):
#         print(" ",end=" ")
#     for j in range(1,6-i):
#         print(temp,end=" ")
#         temp+=2
    # print(" ") 
    
    # 20 18 16 14
    #    12 10 8
    #        6 4
    #          2

# temp = 20
# for i in range(1,5):
#     for sp in range(1,i):
#         print(" ",end=" ")
#     for j in range(1,6-i):
#         print(temp,end=" ")
#         temp-=2
#     print(" ") 

#       A
#     A B
#   A B C
# A B C D

# for i in range(1,5):
#     for sp in range(1,5-i):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print(chr(65+j-1),end=" ")
#     print(" ") 
#       A
#     B B
#   C C C
# D D D D

# for i in range(1,5):
#     for sp in range(1,5-i):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print(chr(65+i-1),end=" ")
#     print(" ") 

#       A
#     B C
#   D E F
# G H I J

# temp = 65
# for i in range(1,5):
#     for sp in range(1,5-i):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print(chr(temp),end=" ")
#         temp+=1
#     print(" ")    

#       A
#     B A
#   C B A
# D C B A

# for i in range(1,5):
#     for sp in range(1,5-i):
#         print(" ",end=" ")
#     for j in range(i,0,-1):
#         print(chr(65+j-1),end=" ")
#     print(" ")                  

li = [1,2,3,4]
li.reverse()
print(li)

li = [1,2,3,4]
print(li[::-1])