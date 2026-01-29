# 1. Write a program using nested if to check whether a number is positive,
# negative, or zero, and if positive, also check whether it is even or odd.
# n = int(input("enter a number = "))
# if(n>=0):
#     if(n>0):
#         if(n%2==0):
#             print("even")
#         else:
#             print("odd")
#     else:
#         print("zero")     
# else:
#     print("negative")   

# 2.  Write a program using nested if to find the greatest among three numbers.          

# a = int(input("enter a number"))
# b = int(input("enter a number"))
# c = int(input("enter a number"))
# if(a>b and a>c):                    # by elif method
#     print("a is greter among three")
# elif(b>c and b>a):
#     print("b is greater among three")
# else:
#     print("c is greater among three")        


# by nested if method

# a = int(input("enter a number"))
# b = int(input("enter a number"))
# c = int(input("enter a number"))
# if(a>b):
#     if(a>c):
#         print("a is greater among three")
#     else:
#         print("c is greater among three")
# else: 
#     if(b>c):
#         print("b is greater among three")
#     else:
#         print("c is greater among three")  

#  3. Write a program using nested if to check whether a student has passed or
#  failed, and if passed, assign a grade based on marks.

# marks = int(input("enter marks = "))
# if(marks>=40):
#     print("status:passed")
#     if(marks>=90):
#         print("grade A++")
#     elif(marks>=80):
#         print("grade A")
#     elif(marks>=70):
#         print("grade B")
#     else:
#         print("grade C")  
# else:
#     print("status:failed")
                      
    
#  4. Write a program using nested if to check whether a person is eligible to
# vote, and if eligible, check whether they are a first-time voter.

# age = int(input("enter your age = "))
# # voted_before = input("yes/no")
# if(age>=18):
#     print("eligible to vote")
#     voted_before = input("yes/no")
#     if(voted_before=="no"):
#         print("you are first time voter")
#     else:
#         print("you are not a first time voter")
# else:
#     print("not eligible to vote")            

# 5. Write a program using nested if to check whether a number is divisible by 5
#  and if yes, check whether it is also divisible by 10.

# n1 = int(input("enter number"))
# if(n1%5==0):
#     if(n1%10==0):
#         print("it is divisible by 5 and 10 both")
#     else:
#         print("it is divisible by only 5 ") 
# else:
#     print("not divisible by 5 ")           

# 6.  Write a program using nested if to check whether a character is an
# alphabet, and if it is an alphabet, check whether it is a vowel or consonant.

# ch = input("enter any character = ")
# if(ch>='a' and ch<='z'):   # take only lower case
#             if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
#                 print("vowel")
#             else:
#                 print("consonant")
# else:
#     print("invalid input")  

# ch = input("enter any character = ")                  
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# vowel = 'aeiou'
# if(ch==alphabet):
#     if(alphabet==vowel):
        # print("vowel")                (method 2 for this) 
#     else:
#         print("consonant")
# else:
#     print("invalid input")    

  # 7. Write a program using nested if to check whether a person is eligible for a
# job based on age, and if eligible, check whether they have the required
# qualification. 

# age = int(input("enter your age = "))
# if(age>=18):
#     has_qualification = input("y/n")
#     if(has_qualification=='y'):
#         print("eligible for job and has a required qualification")  
#     else:
#         print(" eligible but has no required qualification") 
# else:
#     print("under age sorry ") 

     
# 8.  Write a program using nested if to check whether a number is greater than
# 50, and if yes, check whether it is also greater than 100. 

# num1 = int(input("enter any number = "))
# if(num1>50):
#     if(num1>100):
#         print("num1 is greater than 50 and 100 both")
#     else:
#         print("num1 is only greater than 50")
# else:
#     print("num1 is less than 50")                   

# 9.  Write a program using if-elif-else to check whether a number is positive,
# negative, or zero.

# n = int(input("enter any number = "))
# if(n>0):
#     print("possitive")
# elif(n==0):
#     print("zero") 
# else:
#     print("negative")       

#10. Write a program using elif to assign grades based on marks:
# A (90–100), B (80–89), C (70–79), D (60–69), F (below 60).

# marks = int(input("enter marks"))
# if(marks>=90 and marks<=100):
#     print("status:grade A")
# elif(marks>=80 and marks<=89):
#     print("status:grade B")
# elif(marks>=70 and marks<=79):
#     print("status:grade C")
# elif(marks>=60 and marks<=69):
#     print("status:grade D")
# else:
#     print("status:fail")                


# 11. Write a program using elif to check whether a given day number (1–7)
# corresponds to Monday–Sunday.

# day = int(input("enter a day number (1-7)"))
# if(day==1):
#     print("monday")
# elif(day==2):
#     print("tuesday")
# elif(day== 3):
#     print("wednesday")
# elif(day==4):
#     print("thurusday")
# elif(day== 5):
#     print("friday")
# elif(day==6):
#     print("saturday")
# elif(day==7):
#     print("sunday") 
# else:
#     print("invalid day number")                           

# 12. Write a program using elif to find the largest among three numbers.

# a = int(input("enter first number = "))
# b = int(input("enter second number = "))
# c = int(input("enter third number =  "))
# if(a>b and a>c):
#     print(" largest number" ,a )
# elif(b>c and b>a):
#     print("largest number" , b)
# else:
#     print("largest number" , c)       
 
#  13. Write a program using elif to check whether a year is a leap year or not.

# year = int(input("enter year"))
# if(year%4==0):
#     print("leap year")
# elif(year%100==0):
#     print("not a leap year")
# elif(year%400==0):
#     print("leap year") 
# else:
#     print("not a leap year")      

# year = int(input("enter year"))
# if(year%4==0 and year%100!=0 or year%400==0):
#     print("leap year")
# else:
#     print("not a leap year")            

# 14. Write a program using elif to classify a person’s age group: Child, Teen, Adult, or
# Senior.

# age = int(input("enter age = "))
# if(age>50):
#     print("senior age")
# elif(age>20):
#     print("adult")
# elif(age>13):
#     print("teen")  
# elif(age>0):
#     print("child")          
# else:
#     print("invalid age")    

# 15. Write a program using elif to check whether a character is a vowel, consonant,
# digit, or special character.

                
#  17. Write a program using elif to check whether a number is divisible by 2, 3, 5, or
# none of them.

# n = int(input("enter number = "))
# if(n%2==0):
#     print("it is divisible by 2")
# elif(n%3==0):
#     print("it is divisible by 3")
# elif(n%5==0):
#     print("it is divisible by 5")
# else:
#     print("it is divisible by none of them")  
 
# 18. Write a program using elif to convert a numeric month value (1–12) into the month
# name.

# month_value = int(input("enter month value = (1-12) "))
# if(month_value==1):
#     print("january")
# elif(month_value==2):
#     print("february")
# elif(month_value==3):
#     print("march")
# elif(month_value==4):
#     print("april")
# elif(month_value==5):
#     print("may")
# elif(month_value==6):
#     print("june")
# elif(month_value==7):
#     print("july")
# elif(month_value==8):
#     print("august")
# elif(month_value==9):
#     print("september")
# elif(month_value==10):
#     print("october")
# elif(month_value==11):
#     print("november")
# elif(month_value==12):
#     print("december")
# else:
#     print("invalid month value")                                    
            
#    19. Write a program using elif to check the type of triangle: Equilateral, Isosceles, or
# Scalene.     

# side1 = int(input("enter side1 = "))
# side2 = int(input("enter side2 = "))
# side3 = int(input("enter side3 = "))
# if(side1==side2 and side1==side3):
#     print("equilateral triangle")
# elif(side1==side2 or side2==side3):
#     print("isosceles traingle")
# else:
#     print("scalene triangle")            

# 20. Write a program using elif to determine the season based on month number.

# mv = int(input("enter number(1-12) = "))
# if(mv==1 or mv==2 or mv==3 or mv==10 or mv==11 or mv==12):
#     print("winter season")
# elif(mv==4 or mv==5 or mv==6):
#     print("summer")
# elif(mv==7 or mv==8 or mv==9):
#     print("spring") 
# else:
#     print("invalid input")  










         
# 22. Write a program using elif to check whether a number is one-digit, two-digit,
# three-digit, or more.

# n = int(input("enter number"))
# if(n>=0 and n<10):
#     print("one digit number")
# elif(n>=10 and n<=99):
#     print("two digit number") 
# elif(n>=100 and n<=999):
#     print("three digit number")       
# else:
#     print("more than three digit")


# 23. Write a program using elif to check the result of a student: Distinction, First
# Class, Second Class, Pass, or Fail.

# marks = int(input("enter marks"))         #(distincion means topper of the class aove all)
# if(marks<0 or  marks>100):
#     print("status: invalid marks")
# elif(marks>80):
#     print(" status: first class")
# elif(marks>65):
#     print("status : second class") 
# elif(marks>50):
#     print("pass")
# else:
#     print("fail")                

# 24 .Write a program using elif to convert percentage into grade category.

# percentage = float(input("Enter your percentage: "))

# if (percentage < 0 or percentage >100):
#     print("Invalid percentage")                # lessthan or greater than 100 considered as invlaid percenage

# elif (percentage >= 90):
#     print("Grade: A+")

# elif( percentage >= 75):
#     print("Grade: A")

# elif (percentage >= 60):
#     print("Grade: B")

# elif( percentage >= 50):
#     print("Grade: C")

# elif (percentage >=40):
#     print("Grade: D")

# else:
#     print("Grade: Fail")






















#25.  Write a program using elif to check traffic light action based on color input.

# traffic_light = input("enter light = ")
# if(traffic_light=='red'):
#     print("red signal for wait sometime")
# elif(traffic_light=='green'):
#     print("green signal for go ")
# elif(traffic_light=='yellow'):
#     print("yellow light for go until it turns red")
# else:
#     print("invalid input")  

          
# 26.  Write a program using elif to classify temperature as Cold, Moderate, or Hot.

# temp = float(input("enter temperature = "))
# if(temp>40):
#     print("hot")
# elif(temp>=20):
#     print("moderate") 
# else:
#     print("cold")       


# 28. Write a program using elif to check the type of input number: zero, positive even,
# positive odd, or negative.

# n1 = int(input("enter a number"))
# if(n1>=0):
#     if(n1>0):
#         if(n1%2==0):
#             print("positive even")
#         else:
            # print("positive odd")
#     else:
#         print("zero")
# else:               
#     print("negative")     


# 16. Write a program using elif to build a simple calculator for +, -, *, and /.

# a = int(input("enter fist number = "))
# b = int(input("enter second number = "))
# op = input("enter operator = +,*,/,-")
# if(op=='+'):
#     print("result" ,a+b)
# elif(op=='-'):
#     print("result" ,a-b)
# elif(op=='*'):
#     print("result" ,a*b)
# elif(op=='/'):
#     if(b!=0):
#         print("result" ,a/b)
#     else:
#         print("error ")
# else:
#     print("invalid operator")                        


