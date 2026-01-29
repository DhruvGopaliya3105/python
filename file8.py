# 1 Write a program using a while loop to print all digits of a number one by one.
# n = int(input("enter any number = "))
# while n!=0:
#     digit = n%10
   
#     n = n//10
#     print(digit)
  

# 2. Write a program to find the sum of digits of a number using a while loop.

# n = int(input("enter any number = "))
# sum = 0
# while n!=0:
#     sum = sum + (n%10)
#     n = n//10
# print(sum)    

# 3. Write a program to count how many digits are in a given number using a while loop.

# int(input("enter any number = "))
# count = 0
# while n!=0:
#     count+=1
#     n = n//10
# print(count)  

#   4. Write a program to reverse a number using a while loop.

# n = int(input("enter any number = "))
# rev = 0
# while n!=0:
#     rev = rev*10 + n%10
#     n = n//10
# print(rev)    

# 5. Write a program to check whether a number is a palindrome using a while loop.

# n = int(input("enter any number = "))
# rev = 0
# original = n
# while original!=0:
#     digit = original%10
#     rev = rev*10 + digit
#     original//=10

# if n==rev:
#     print("it is palindrome")
# else:
#     print("it is not a palindrome")        

# 6. Write a program to find the product of digits of a number using a while loop.

# n = 458
# product = 1
# while n!=0:
#     digit = n %10
#     product = product * digit
#     n = n//10
# print(product )    

# 7. Write a program to find the largest digit in a number using a while loop.

# n = int(input("enter any number = "))
# largest = 0
# while n!=0:
#     digit = n%10
#     if digit>largest:
#         largest = digit
#     n = n//10
# print(largest)    
        
# 8. Write a program to find the smallest digit in a number using a while loop.   

# n = 345
# smallest = 9
# while n!=0:
#     digit = n%10
#     if digit<smallest:
#         smallest = digit
#     n = n//10
# print(smallest)             

# 9. Write a program to check whether a number is an Armstrong number using a while loop.

# n = int(input("enter any number = "))
# sum = 0
# temp =n
# while temp!=0:
#     digit = temp%10
#     sum = sum + (digit**3)
#     temp = temp//10
# if n == sum:
#     print("its a armstrong number ")  
# else:
#     print("not a armstrong number ")      

# 10. Write a program to remove all zeros from a number using a while loop.



# n = int(input("Enter a number: "))

# new_num = 0
# place = 1

# while n != 0:
#     digit = n % 10
#     if digit != 0:
#         new_num = new_num + digit * place
#         place = place * 10
#     n = n // 10
    
# print("new number is ",new_num)    

# 11. Write a program to count how many even and odd digits are present in a number using a
# while loop.

# n = int(input("enter any number = "))
# odd_digit = 0
# even_digit = 0
# while n !=0:
#     digit = n%10
#     if digit!=0:
#         if digit%2==0:
#             even_digit+=1
            
#         else:
#             odd_digit+=1
            
#     n= n//10
# print(even_digit)
# print(odd_digit)            
                
            

