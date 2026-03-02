#1 Problem Statement: Remove elements that occur more than once and keep only unique elements.
# Input:
# nums = [1, 2, 2, 3, 4, 4, 5]
# Output:
# [1, 3, 5]

# nums = [1,2,2,3,4,4,5]
# uniquel = []    # to put the value into this list              
# for i in range(len(nums)):    
#     count = 0   # for every iteration it starts from 0 not update that is why we put inside the loop
#     for j in range(len(nums)): #in one i iteration it starts from 0 to len(nums) 
#         if nums[i]==nums[j]:   # for check i and j are they equal or not but at once count is there
#          count+=1
#     if count==1: #if it is one then its append otherwise skip
#         uniquel.append(nums[i]) 
# print(uniquel)      
# 0r by this built in method count we know 
  
# nums = [1, 2, 2, 3, 4, 4, 5]

# result = []

# for n in nums:              
#     if nums.count(n) == 1: 
#         print((n))  
#         result.append(n)

# print(result)




# 2 Problem Statement: A list contains numbers from 1 to n with one number missing. Find the missing
# number.
# Input:
# nums = [1, 2, 4, 5, 6]
# Output:
# 3

# nums = [1,2,4,5,6]
# for i in range(1,7):       #using slicing for missing value 1 to 7 one by one
#     if i not in nums:
#         print("missing part ",i)

#3 Problem Statement: Remove all negative numbers and return the updated list.
# Input:
# nums = [3, -1, 5, -7, 8, -2]
# Output:
# [3, 5, 8]

# nums = [3,-1,5,-7,8,-2]
# newli= []
# for i in range(len(nums)):    # len start from 1 to last 
#     if nums[i]>0: # if it is greater then 0 then its append bcz i want to remove the negative no
#         newli.append(nums[i])
#     else:
#         continue              if it is negative then skip tha!t value
# print(newli)        


# nums = [3,-1,5,-7,8,-2]
# newli = []                     # direct by membership operator without nums or len
# for i in nums:
#     if i>0:
#         newli.append(i)
# print(newli)        
        
#4 Problem Statement: Check whether the list reads the same forward and backward.
# Input:
# nums = [1, 2, 3, 2, 1]
# Output:
# # Palindrome

# nums = [1, 2, 3, 2, 1]
# num1 = []
# for i in range(len(nums)-1,-1,-1): # -1 bcz len is 5 but index upto 4   using slicing
#     num1.append(nums[i])
#     # if num1==nums:
#     #     print("its a palindrome")   # in this inside the loop its check after evry value then it shows not a palindrome
#     # else:
#     #     print("not a palindrome") 
# if num1==nums:
#     print("it is a palindrome")    # outer loop means after covering all the iteration it shows result 
# else:
#     print("not a palindrome") 

    
    
# nums = [1, 2, 3, 2, 1]

# left = 0
# right = len(nums) - 1

# while left < right:
#     if nums[left] != nums[right]:
#         print("Not Palindrome")
#         break                    #not check if one doesnot match then its break directly without checking every one to lat
#     left += 1
#     right -= 1
# else:
#     print("Palindrome")


# 5 Problem Statement: Find all pairs of elements whose sum equals the target value.
# Input:
# nums = [2, 4, 3, 5, 7]
# target = 7
# Output:
# (2, 5)
# (4, 3)

# nums = [2,4,3,5,7]
# target = 7 
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i] + nums[j]==target:
#             print(nums[i],nums[j])




# 6 Problem Statement: Merge two lists into one and remove duplicate elements.
# Input:
# list1 = [1, 2, 3]
# list2 = [3, 4, 5]
# Output:
# [1, 2, 3, 4, 5]

# list1 = [1, 2, 3]
# list2 = [3, 4, 5]
# list3 = []
# for i in range(len(list1)):
#     if list1[i] not in list3:
#         list3.append(list1[i])
# for j in range(len(list2)):
#     if list2[j] not in list3:
#         list3.append(list2[j]) 
# print(list3)  

      
# 7 Problem Statement: Print all index positions where the target element occurs.
# Input:
# nums = [5, 2, 7, 2, 9, 2]
# target = 2
# Output:
# nums = [5, 2, 7, 2, 9, 2]
# target = 2
# newli = []
# for i in range(len(nums)):
#     if nums[i]==target:
#         newli.append(i)
# print(newli) 

# Problem 8 Statement: Rotate the list one position to the left. The first element moves to the end.
# Input:
# nums = [10, 20, 30, 40, 50]
# Output:
# [20, 30, 40, 50, 10]



       