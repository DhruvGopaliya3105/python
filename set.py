# 1. Create a set of numbers from 1 to 5 and print it.

# s = {1,2,3,4,5}
# print(s)

# 2. Add an element to an existing set.

# s = {1,2,3,4}
# s.add(100)           #add anywhere no ordered is fixed
# print(s)

# 3. Remove an element using remove() and observe what happens if the element does not exist.

# s = {"dhruv","keshav","pintu"}
# s.remove("neha")
# print(s)     # it shows error bcz it is not in the set but this is not in the case of discard

# 4. Remove an element using discard() and compare the behavior with remove().

# s = {"dhruv","neha","monu","sonu"}
# s.discard("hiroshima")
# print(s) # it doesnot show any error bcz discard not show any error if element is present or not 
 
# 5. Find the length of a set 5. Find the length of a set.

# s = {1,2,3,4}
# print(len(s))

# 6. Check if a specific element exists in a set.

# s = {1,2,3,4}          # use membership operator in this
# print(1 in s)

# 7. Clear all elements from a set.

# s = {1,2,3,4}
# s.clear()
# print(s)

# 8. Convert a list with duplicate values into a set to remove duplicates.

# li = [1,2,3,3,2,45,6]
# set1 = set(li)
# print(set1)     # it automatically removes the duplicate items using set constructor
 
# 9. Create an empty set correctly (without using {}).

# s1 = set()       # using set constructor convert
# print(s1)

# 10. Iterate through a set and print each element.

# s1 = {1,2,3,4,5}
# for i in s1:
#     print(i)
    
# s = {1,2,3,47}
# li = list(s)
# print(li)    #with while we cannot do iterate directly with set bcz set is unordered for convert
#             #  into list then we can iterate
# i = 0
# while i<len(li):
#     print(li[i])
#     i+=1

# 11. Given two sets, find their union.

# s1 = {1,2,3,4}
# s2 = {2,3,6,7,8} # it shows all elements but at once not remove duplicated only 1 time it shows
# print(s1.union(s2))

# 12. Given two sets, find their intersection.

# s1 = {1,2,3,4}
# s2  = {1,2,6,7}
# print(s1.intersection(s2))
    
# 13. Find the difference between two sets.

# s1 = {1,2,3,5,6}
# s2 = {1,2,6,5,8,9} # remove all elements which are common in a and b (a-b) gives remaining in a 
# print(s1-s2)
    
# # 14. Find the symmetric difference between two sets.
    
# s1 = {1,2,3,4,8,9}
# s2 = {1,2,4,5,99,10} # only duplicates it shows in both whether union shows all or duplicate at once
# print(s1.intersection(s2))

# 15. Check whether one set is a subset of another.

# s1 = {1,2}
# s2 = {1,2,3,4,5}     #if all th elements are there then it is called subset otherwise not
# print(s1.issubset(s2))

# 16. Check whether one set is a superset of another.

# a = {1,2,3,4}
# b = {2,3,4}  # A set A is a superset of set B if every element of B exists in A.
# print(a.issuperset(b))

# 17 Check whether two sets are disjoint.

# a = {1,2,3}
# b = {4,5,6}    #Two sets are disjoint if they have no common elements between them.
# print(a.isdisjoint(b))

# 18. Update one set with another set.

# a = {1,2,3}
# b = {4,5,2}
# a.update(b)
# print(a)

#19 Remove a random element from a set.

# s1 = {1,2,3,4}
# s2 = s1.pop() it remove one by one 
# s2 = s1.pop()      
# print(s2)
# print(s1)

# 20. Find common elements between three sets.

# s1 = {1,2,3,4,5}
# s2 = {2,3,4}
# s3= {3,4,7}
# print(s1 & s2 & s3)

# 21. Given a sentence, find all unique characters using a set.

# s1 = "this is a sentence"
# uniqueelement = set(s1)
# print(uniqueelement)

# sentence = "this is a sentence"     # for removing spaces
# unique_chars = set(sentence.replace(" " , ""))
# print(unique_chars)

# 22. Count the number of unique words in a paragraph using a set.




# 23. Given two lists, return a list of common unique elements using sets.




# 24 find elements that appear in either of the two set not in both

# s1 = {1,4,5,6,7}
# s2 = {1,3,5,9,99,88,}
# print((s1 ^ s2))

# 25 given a list of number find all duplicates elements using sets

# li = [1,2,3,4,5,5,4,3,7,8,9]
# s1 = set(li)                    # using set constructor
# print(s1)

# 26. Write a program to check if two strings are anagrams using sets.

# s1 = "listen"
# s2 = "silent"
# is_anagram = True
# for c in s1:
#     if c not in s2:
#         is_anagram  = False
# if is_anagram==True:
#     print("its a anagram")
# else:
#     print("its not a anagram")            
        

#27 given a set of numbers removes  all even number

# s1 = {2,3,4,5,6,8,9,12,13,14,15,19}
# result = set()     # we want to make this otherwise it not add in this acc to condition
# for i in s1:
#     if i%2!=0:
#         result.add(i)
# print(result)   

# 28 create a set comprehension and print squares of numbers 1 to 10
# square = {i**2 for i in range(1,11)}
# print(square)     #order may very in set

# 29 from a given set,create a new set contains only number greater than 10

# s = {1,2,3,4,10,11,12,13,44,55,66,7,77}
# s1 = set()
# for i in s:
#     if i>10:
#         s1.add(i)
# print(s1)  

# ->> Remove the duplicate elements or character from string :

# s = "pythonprogramming"
# unique_ele = set()
# unique_word = ' '
# for c in s:
#     if c not in unique_ele:
#         unique_ele.add(c)
#         unique_word+=c
#         print(unique_word)        # one by one show element 

# print(unique_word)   # direct show after completion of all 

# 30. Given multiple sets in a list, find the intersection of all sets.


  


      








 
