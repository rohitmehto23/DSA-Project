#!/usr/bin/env python
# coding: utf-8

# In[2]:


#TAKING INPUT FROM USER

name = input("what is your name ? ")
print("welcome", name)


# In[ ]:


# program to add inputs
sub1 = int(input("mark sub1: "))
sub2 = int(input("mark sub2: "))
total = sub1 + sub2
print("The total mark is: ", total)


# In[ ]:


# AREA OF TRIANGLE

b = float(input("enter base: "))
h = float(input("enter height: "))
area = 1/2 * b * h
print(area)
     


# In[1]:


# area of triangle (if perimeter is given)

a = float(input("enter length of 1st side: "))   # 3
b = float(input("enter length of 2nd side: "))   # 4
c = float(input("enter length of 3rd side: "))   # 5

# calculate semi-perimeter
s = (a+b+c)/2
# calculate Area
area = (s*(s-a) * (s-b) * (s-c)) ** 0.5
print("\nArea of the triangle is : ", area)


# In[2]:


# IF ELSE CODE


# WRITE A PYTHON PROGRAM TO TELL THE TEMPERATURE BY INPUT

temp = int(input("enter any values"))
if temp > 30:
    print("it's a hot day")
elif temp > 25:
    print("it's a pleasant day")
elif temp > 25:
    print("it's a cold day")
else:
    print("it's a chilly day")
print("it's a beautiful day")


# In[3]:


# GRADE QUESTION
# MAKE A PYTHON PROGRAM USING IF ELSE TO TELL THE GRADES ACCORDING TO THE PERCENTAGE OF MARKS. (USE INPUT FUNCTION)


# calculate percentage
a = float(input("marks a: "))
b = float(input("marks b: "))
c = float(input("marks c: "))
d = float(input("marks d: "))
e = float(input("marks e: "))

percentage = (a+b+c+d+e)/500*100
print(f"The percentage is: {percentage} %")

# input percentage
percentage = float(input("enter marks in percentage: "))
if percentage > 95:
    print("A+")
elif percentage > 90:
    print("A")
elif percentage > 80:
    print("B+")
elif percentage > 70:
    print("B")
elif percentage > 60:
    print("C+")
elif percentage > 50:
    print("C")
elif percentage > 40:
    print("D+")
elif percentage > 33:
    print("D")
else:
    print("F")
     


# In[4]:


#  GROSS SALARY OF A PERSON CONSIDERING THE FOLLOWING INFORMATION.
basic = int(input("what is basic: "))
hra = 0.20 * basic
da = 0.50 * basic
pf = 0.11 * basic
print(hra)
print(da)
print(pf)
if basic > 10000:
    allowance = 1700
elif basic > 5000:
    allowance = 15000
else:
    allowance = 1300
print("The allowance is: ", allowance)

gs = basic + hra + da + allowance - pf
print("The gross salary is :" , gs)
     


# In[5]:


#  calculator

first = input("Enter first number : ")
second = input("Enter second number : ")
first = int(first)
second = int(second)
print("----press keys for operator (+,-,*,/,%)----------")
operator = input("Enter operator : ")
if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    print(first * second)
elif operator == "/":
    print(first / second)
elif operator == "%":
    print(first % second)
else:
    print("Invalid Operation")
     


# In[6]:


# DEF FUNCTIONS

# write program to print "HELLO WORLD" using def function.

def myfunction():
    print("Hello World")
myfunction()


# In[7]:


# WRITE A PYTHON PROGRAM TO PRINT HAPPY BIRTHDAY WISH 3 TIMES USING DEF FUNCTION.

def myfunction():
    print("Happy birday to you !may god bless you !Happy birthday to you !")
myfunction()
myfunction()
myfunction()


# In[22]:


# define addition 
def addn():
    print(8+9)
addn()    


# In[23]:


# define substraction
def subs():
    print(65-37)
subs()    


# In[24]:


# define multiplication
def mult():
    print(8*4)
mult()


# In[25]:


# define division
def dev():
    print(68/34)
dev() 


# In[26]:


def add(num1,num2):
    sum=num1+num2
    print(sum)
#call
add(30,80)


# In[2]:


def mult(num1,num2):
    mult=num1*num2
    print(mult)
mult(23,63)


# In[3]:


def dev(num1,num2):
    dev=num1/num2
    print(dev)
dev(45,5)


# In[4]:


#define a program that returns a multiple of 8 for every number inserted
def mult(num1):
    mult=num1*8
    print(mult)
mult(2)    


# In[ ]:


# create a function that check either a given integer is negetive , positive or zero ?
def check_integer(n):
    if n>0:
        print("positive")
    elif n<0:
        print("negetive")
    else:
        print("zero")
    
num=int(input("enter an integer: "))
result=check_integer(num)
  


# In[ ]:


i=int(input('enter total '))
fact=1
while(i>0):
    fact=fact*i
    i=i-1
print("factorial is ", fact)


# In[ ]:


i=int(input('enter number '))
while i!= -1:
      i=int(input('enter number '))


# In[ ]:


import array 
from array import*
def pairwise_swap(arr):
    n=len(arr)
   
    for i in range (0,n-1):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

                
array1=array('i',[64,65,27,36,82,93,56,82,54,35])
pairwise_swap(array1)
print("n")
print(array1)


# In[ ]:


import array 
from array import*
def pairwise_swap(arr):
    n=len(arr)
   
    for i in range (0,n-1):
        for j in range(0,n-i-1):
            if arr[j] < arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

                
array1=array('i',[64,65,27,36,82,93,56,82,54,35])
pairwise_swap(array1)
print("n")
print(array1)


# In[ ]:


# Q-create an array containing 10 numbers break the array into two parts and print individual sub-arrays 
array2=[1,2,34,53,6,7,23,43,56,65]
sub_array1=array2[:5]
sub_array2=array2[5:]
print('sub_array 1:',sub_array1)
print('sub_array 2:',sub_array2)


# In[ ]:


import array 
from array import*
def pairwise_swap(array):
    n=len(arr)
   
    for i in range (0,n-1):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

                
arr=array('i',[64,34,25,12])
pairwise_swap(arr)
print("n")
print(arr)


# In[ ]:


# python program to split a given array into 3 equal parts
array2=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
sub_array1=array2[:5]
sub_array2=array2[5:10]
sub_array3=array2[10:]
print('sub_array 1:',sub_array1)
print('sub_array 2:',sub_array2)
print('sub_array 3:',sub_array3)


# In[ ]:


import array 
from array import *
def selection_sort(array):
    n=len(arr)
   
    for i in range (0,n-1):
        min_value=i
        for j in range(i+1,n):
            if arr[j] < arr[min_value]:
                min_value=j          
        arr[i],arr[min_value]=arr[min_value],arr[i]

                
arr=array('i',[34,72,432,232,1,3,5])
selection_sort(arr)
print(arr)


# In[ ]:


# construct array containing 4 integers and find the sum and difference of two largest numbers?
import array 
from array import *
array = array('i',[1,5,3,7])
array_sorted=sorted(array)
print(array_sorted)
sum = array_sorted[-1]+array_sorted[-2]
print('the sum is:',sum)
diff=array_sorted[-1]-array_sorted[-2]
print('the difference is: ',diff)


# In[ ]:


#array containing 4 integers find the sum and difference of two largest numbers?
import array 
from array import*
array = array('i',[1,2,3,4])
print(array)
lagest1=float('inf')
lagest2=float('inf')
i=0
whilei<len(array):
    if array[i]>largest1:
        largest1


# In[ ]:


# Ques - construct an array contraing 5 integers wap a progrm to cal the max product possible of th integer?
import random
array=[random.randint(,9) for _ in range(5)]
arr=sorted(array)
print(arr)
product = arr[-1]*arr[-2]*arr[-3]*arr[-4]*arr[-5]
print(product)


# In[ ]:


# ques - construct an array containing 6 array divide the array into two parts and rejoin the sub elements with 0 in the middle?
import array 
from array import *
sub_1=None
sub_2= None
def divide(array):
    global sub_1,sub_2
    mid=len(a)//2
    sub_1=a[:mid]
    sub_2=a[mid:]




a = array('i',[1,2,3,4,5,6])
divide(a)
print(sub_1)
print(sub_2)

new=array('i',[0])
final = sub_1 + new +sub_2
print(final)


# In[ ]:


# wap to print fibonacci series
n=int(input('enter last number'))
x=0
y=1
z=0
while(z<=n):
    print(z)
    x=y
    y=z
    z=x+y


# In[8]:


# addition of two number :
first = int(input("enter 1st no. :"))
second = int(input("enter 2nd no. :"))
sum = first + second
print("The sum is :" ,sum)


# In[9]:


a = 2
b = 3
print(a+b)
     


# In[10]:


num1 = 2
num2 = 3
sum = num1 + num2
print("sum of two numbers is : ", sum)
     


# In[11]:


num1 = 2
num2 = 3
multiplication = num1 * num2
print("multipication of two numbers is : ", multiplication)


# In[12]:


num1 = 6
num2 = 3
division = num1 / num2
print("division of two numbers is : ", division)
     


# In[13]:


num1 = 2
num2 = 3
sub = num1 - num2
print("sub of two numbers is : ", sub)


# In[14]:


num1 = 10
num2 = 3
modulus = num1 % num2
print("modulus of two numbers is : ", modulus)


# In[15]:


num1 = 23
num2 = 3
floor = num1 // num2
print("floor of two numbers is :" , floor)


# In[16]:


# que 1
a = 2
b= 3
if a > b:
    print("a is greater than b !")
else:
    print("b is greater than a !")
     


# In[17]:


#  elif a==b
     

a = 10
b = 10
if a>b:
    print("a is greater than b !")
elif a==b:
    print("a is equal to b !")
else:
    print("b is greater than a ! ")
     


# In[19]:


#   program to check weather the  given no. is even or odd:
     

a = 3
if (a%2)==0:
    print("a is even")
else:
    print("a is odd")

     

a = 36
if (a%2)==0:
    print("a is even")
else:
    print("a is odd ")


# In[20]:


#  function that check either a given integer is negetive , positive or zero ?
def check_integer(n):
    if n>0:
        print("positive")
    elif n<0:
        print("negetive")
    else:
        print("zero")
    
num=int(input("enter an integer: "))
result=check_integer(num)
  


# In[21]:


#Program to find the factorial

i=int(input('enter total '))
fact=1
while(i>0):
    fact=fact*i
    i=i-1
print("factorial is ", fact)


# In[ ]:


temp=int (input("enter temp "))
if temp>30:
    print("it's a hot day")
print("it's a beautiful day")


# In[ ]:


temp=int (input("enter temp "))
if temp>30:
    print("it's a hot day")
elif temp>20:
    print("it's a pleasent day")
print("it's a beautiful day")


# In[ ]:


temp=int (input("enter temp "))
if temp>30:
    print("it's a hot day")
elif temp>20:
    print("it's a pleasent day")
elif temp>10:
    print("it's a cold day")
print("it's a beautiful day") 


# In[ ]:


temp=int (input("enter temp "))
if temp>30:
    print("it's a hot day")
elif temp>20:
    print("it's a pleasent day")
elif temp>10:
    print("it's a cold day")
else:
    print("it's a chilly day")
print("it's a beautiful day")


# In[ ]:


a= int(input("enter marks of 1st subjects"))
b= int(input("enter marks of 2nd subjects")) 
c= int(input("enter marks of 3rd subjects"))
d= int(input("enter marks of 4th subjects"))
e= int(input("enter marks of 5th subjects"))
total_marks = a+b+c+d+e
percentage=(total_marks)/5
print("the total marks obtained are = ", total_marks)
print("the percentage is = ", percentage, "%")

if percentage>95:
    print("A+")
elif percentage>90:
    print("A")
elif percentage>80:
    print("B+")
elif percentage>70:
    print("B")
elif percentage>60:
    print("C+")
elif percentage>50:
    print("C")
elif percentage>40:
    print("D+")
elif percentage>33:
    print("D")
else:
    print("F")

