#1 Print all elements of a 2D list row-wise.
# li = [[1,2,3],[4,5,6]]
# for i in range(len(li)):  #row loop
#     for j in range(len(li[i])):  #column loop
#         print(li[i][j])
    
# 2 Print all elements column-wise.        
# li = [[1,2,3],[4,5,6]]
# for j in range(3):        # column loop using slicing put limit 3 so it ended at 2 it is exclusive 
#     for i in range(len(li)):       # row loop
#         print(li[i][j])

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

# li = [[1,2,3],[4,5,6]]
# for j in range(len(li[0])):        # column loop    j start from 0 bcz it is column wise
#     for i in range(len(li)):       # row loop
#         print(li[i][j])

# 3 Find the sum of all elements in a 2D list.
# li = [[1,2,3],[4,5,6]]
# sum = 0
# for i in range(len(li)):
#     for j in range(len(li[i])):
#         sum  = sum+ (li[i][j])
# print(sum)  

# li = [[1,2,3],[4,5,6]]
# sum = 0
# for i in li:
#     for j in i:
#         sum+=j
# print(sum)        
              

# 4 Find the maximum element in a 2D list.

# li = [[1,2,3],[4,5,6]]
# maxl = li[0][0]
# for i in range(len(li)):
#     for j in range(len(li[i])):
#         if li[i][j]>maxl:
#             maxl=li[i][j]
# print(maxl)  

# li = [[1,2,3],[4,5,6]]
# maxli = 1
# for i in li:
#     for j in i:
#         if j>maxli:
#             maxli = j
# print(maxli)            
      

# 5 Find the minimum element in a 2D list. 
# li = [[1,2,3],[4,5,6]]
# minl = 10
# for i in range(len(li)):
#     for j in range(len(li[i])):
#         if li[i][j]<minl:
#             minl=li[i][j] 
# print(minl)             

# 6 Count total number of elements in a 2D list.

# li = [[1,2,3],[4,5,6]]
# count = 0
# for i in range(len(li)):
#     for j in range(len(li[i])):
#         count+=1
# print(count) 


# 9 Find the sum of each row.
# li = [[1,2,3],[4,5,6]]
# sum1 = 0
# sum2 = 0
# for i in range(len(li)):
#     for j in range(len(li[i])):
#         if i==0:
#             sum1 += li[i][j]
#         elif i==1:
#             sum2 += li[i][j]           
# print("first row sum","second row sum",sum1,sum2)   


# li = [[1,2,3],[4,5,6],[7,8,9]]
# for i in range(len(li)):
#     for j in range(len(li[i])):
#         if i==j:
#             print(li[i][j])          

# li = [1,2,3],[4,5,6],[7,8,9]
# larli = 1
# for i in li:
#     for j in i:
#         if j>larli:
#             larli= j
# print(larli)  

# li = []
# for i in range(1,101):
#     if i%2==0:
#         li.append(i)
# print(li)                  

# list comprehension is a concise way to generate a list by using for loop and some condition
# syntax 
# [expression for expression in range()some condition]
# generate a list of odd number from 1 to 100

# num = [x for x in range(1,101) if x%2!=0]
# print("odd numbers",num)

# num = [ x*x for x in range(1,11)  ]
# print(num)

# li = ["apple","car","elephant","dog","cat"]
# new = []
# for word in li:
#     if len(word)<4:
#         new.append(word)
# print(new)

# li = ["apple","car","elephant","dog","cat"]
# n = [word for word in li if len(word)<4]
# print(n)


# i1 = [1,2,3,4,5,6,7,8,10,12,15,17]
# n = [number for number in i1 if number>10]
# print(n)

# generate the list of odd numbers from 100 t0 1

# in shallow copy the preference of the outer objexts are different and inner objexts references ae same.

# in deep copy the nested object are also copied it doesnot change 


       

