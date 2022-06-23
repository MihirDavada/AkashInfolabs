# #Calculate the area of a Rectangle

# w=int(input("Enter the width of the Rectangle : "))
# l=int(input("Enter the length of the Rectangle : "))

# print("The Area of the Rectangle is = ",w*l)


# #Calculate the area of a sqaure
# a=int(input("Enter one side length of a square: "))
# A=a*a #area of a square
# print("The area of a square is : ",A)



# #Calculate the area of an circle
# r=float(input("Enter the radius of circle : "))
# A=3.14*r*r
# print("The area of circle having radius" ,r, "is : ",A)



#Calculate the average of 5 numbers
# n1=int(input("Enter the first value : "))
# n2=int(input("Enter the second value : "))
# n3=int(input("Enter the third value : "))
# n4=int(input("Enter the forth value : "))
# n5=int(input("Enter the fifth value : "))

# Avg=(n1+n2+n3+n4+n5)/5

# print("The average of the given 5 numbers is : ",Avg)


#Check whether number is even or odd.
# num=int(input("Enter an integer : "))

# if num%2==0:
#  print(num, "is an even number")
# else:
#  print(num, "is an odd number")



#Take a year and check whether it is leap year or not
# year=int(input("Enter a year : "))

# if (year % 400 == 0) and (year % 100 == 0):
#  print(year, "is a leap year")
# elif (year % 4 ==0) and (year % 100 != 0):
#     print(year, "is a leap year")
# else:
#  print(year, "is not a leap year")




# #Take a number and check whether it is zero, positive or negative.
# x=int(input("Enter any integer: "))

# if x>=0:
#     if x==0:
#      print(x, "is zero")
#     else:
#      print(x, "is a positive number")
# else:
#  print(x, "is a negative number")

# #Take 2 numbers and display greatest number. (Also check equal number condition)
# a=int(input("Enter the first value: "))
# b=int(input("Enter the second value: "))

# if a==b:
#  print(a, "is equal to" ,b)
# if a>b:
#  print(a, "is greater than" ,b)



# #Take a number and find factorial of that number.
# num = int(input("Enter a number: "))    
# factorial = 1    
# if num < 0:    
#    print(" Factorial does not exist for negative numbers")    
# elif num == 0:    
#    print("The factorial of 0 is 1")    
# else:    
#    for i in range(1,num + 1):    
#        factorial = factorial*i    
#    print("The factorial of",num,"is",factorial)

# #Write a program to swap 2 numbers using third variable.
# a=int(input("Enter the first number: "))
# b=int(input("Enter the second number: "))

# c=a
# a=b
# b=c

# print("The value of a after swapping : ",a)
# print("The value of b after swapping : ",b)


# #Take 2 numbers and find smallest number.
# a=int(input("Enter the first number: "))
# b=int(input("Enter the second number: "))

# if a<b:
#  print(a, "is smallest number")
# else:
#  print(b, "is smallest number")

# #  Take a number check if a number is less than 100 or not. If it is less than 100 then check if it is odd or even
# x=int(input("Enter a number : "))
# if x<100:

#     print(x, "is less than 100")
#     if x%2==0:
#         print(x, "is an even number")
#     else:
#         print(x, "is an odd number")
# else:
#     print(x, "is not less than 100")



# #Take a number to print the square of a number if it is less than 10
# num=int(input("Enter a number : "))

# if num<10:
#  print("Square of " ,num, "is : ",num*num)

# else:
#  print(num, "is not less than 10")

# #Take a number and check whether
# # it is zero, positive or negative using nested IF…ELSE statement .

# x=int(input("Enter any integer: "))

# if x>=0:
#     if x==0:
#      print(x, "is zero")

#     else:
#      print(x, "is a positive number")

# else:
#  print(x, "is a negative number")

# #Write a program to swap 2 numbers without taking third variable.
# a=int(input("Enter the first number: "))
# b=int(input("Enter the second number: "))

# a=a+b
# b=a-b
# a=a-b

# print("The value of a after swapping : ",a)
# print("The value of b after swapping : ",b)

'''Take starting number and ending number from the user and print following series.
Output :-
Enter starting number : 30
Enter ending number : 0
30
27
24
21
18
15
12
9
6
3
0'''

a=int(input("Enter the starting number: "))
b=int(input("Enter the ending number: "))

for i in range(a,-1,-3):
 print(i)