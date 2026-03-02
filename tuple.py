# 1 Create a tuple containing five different numbers and display it.
# n1 = (1,2,3,4,5)
# print(n1)

# 2 Access the first and last element of a tuple.
# n = (1,2,3,4,5)
# print(n[0])
# print(n[-1])

# n = ("dhruv")
# print(n[0])
# print(n[-1])

# 3 Find the total number of elements present in a tuple.

# n = (1,2,3,4,5,6)
# count = 0
# for i in n:
#     count+=1
# print(count)

# n = (1,2,3,4,5)
# count = len(n)
# print(count)    

# 4 Check whether a given value exists inside a tuple.

# n = (1,2,3,4)
# print(1 in n)

# n = (1,2,3,4)
# value = 4
# if value in n:
#     print("it is present")
# else:
#     print("its not present")    
    
# n = (1,2,34,5)
# value = 2
# for i in n:   #for loop checks condition every time so that why it shows print on each iteration
#     if value==i:
#         print("yes it is present")
#         break # i put break bcz if conditon meet then it terminates otherwise it shows 4 times each iteration
#     else:
#         print("sorry it is not present")    

# 5 Concatenate two tuples and print the new tuple.
 
# n1 = (1,2,3)
# n2  = (3,4,5)
# n3 = n1+n2
# print(n3) 

# 6 Repeat a tuple two times using an operator.

# n = (1,2)
# print(n*2)

# n = ("dhruv")
# print(n*2)

# 7 Find the index of a specific element in a tuple.

# n = (1,2,3,4)
# print(n[0])

# n = ("dhruv","keshav")
# print(n[1])

# n = ("dhruv")
# print(n[0])

# 8 Count how many times a particular value appears in a tuple.

# n = (1,2,3,1,2,31,1,1)
# print(n.count(1))

# 9 Slice a tuple to display elements from index 1 to 4.

# n = ("dhruvgopaliya")
# print(n[1:5])

# 10 Iterate through all elements of a tuple using a loop.

# n = (1,2,3,4,5,6)
# for i in n:
#     print(i)

# n = ("dhruv")
# i = 0
# while i<len(n):
#     print(n[i])
#     i+=1