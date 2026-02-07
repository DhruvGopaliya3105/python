# 1 Write a program using a while loop to print all digits of a number one by one.
# n = int(input("enter any number = "))
# while n!=0:
#     digit = n%10
#     print(digit)
#     n = n//10      
  

# 2. Write a program to find the sum of digits of a number using a while loop.

# n = int(input("enter any number = "))
# sum = 0
# while n!=0:
#     digit = n%10
#     sum = sum + digit
#     n = n//10
# print(sum)    

# 3. Write a program to count how many digits are in a given number using a while loop.

# n = int(input("enter any number = "))
# count = 0
# while n!=0:
#     count+=1
#     n = n//10
# print(count)  

#   4. Write a program to reverse a number using a while loop.

# n = int(input("enter any number = "))
# rev = 0
# while n!=0:
#     digit = n%10
#     rev = rev*10 + digit
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
        
# 12. Write a program to check whether a number contains a specific digit (for example,5)      
            
# n = int(input("Enter a number: "))
# search = 5   # digit to find
# count = 0

# while n > 0:
#     digit = n % 10
    
#     if digit == search:
#         count += 1
    
#     n = n // 10

# if count > 0:
#     print("Digit found in the number")
# else:
#     print("Digit not found in the number")

# 13. Write a program to calculate the sum of even digits and sum of odd digits separately
# using a while loop.

# n = int(input("enter any number = "))
# evensum = 0
# oddsum = 0
# while n!=0:
#     digit = n%10
#     if digit!=0:
#         if digit%2==0:
#             evensum = evensum+digit
#         else:
#             oddsum = oddsum+digit
#     n = n//10
# print("even digit sum is ",evensum)
# print("odd digit sum",oddsum)                

# 14. Write a program to create a new number by squaring each digit of a given number using
# a while loop.

# 15. Write a program to check whether a number is a perfect number using a while loop.

# num = int(input("Enter a number: "))
# i = 1
# sum_div = 0

# while i < num:          # changed condition
#     if num % i == 0:
#         sum_div = sum_div + i
#     i = i + 1

# if sum_div == num:
#     print("Perfect number")
# else:
#     print("Not a perfect number")

# 16. Write a program to print the Fibonacci series up to N terms using a while loop.

# n = int(input("Enter number of terms: "))

# a = 0
# b = 1
# count = 0

# while count < n:
#     print(a, end=" ")
#     c = a + b
#     a = b
#     b = c
#     count += 1

# 17. Write a program to find the factorial of a number using a while loop.

# n = int(input("enter any fact = "))
# product  = 1
# while n!=0:
#     product = product *n
#     n-=1
# print(product)    
    
# 18. Write a program to calculate the power of a number (a^b) using a while loop.
 
# a = int(input("enter any number = "))
# b = int(input("enter any number = "))
# result = 1
# while b!=0:
#     result = result*a
#     b-=1
# print(result)    
        
# 19. Write a program to find the GCD of two numbers using a while loop.

# a = int(input("enter any number = "))
# b = int(input("enter any number = "))
# while b!=0:
#     r = a%b
#     a =b
#     b = r
#     print("gcd is ",a)

# 20. Write a program to check whether a number is prime using a while loop.= int(input("Enter a number: "))
n = int(input("Enter a number: "))

i = 2
count = 0


while i <= n:
    if n % i == 0:
        count += 1
    i += 1

if count == 1:
    print("Prime number")
else:
    print("Not prime")