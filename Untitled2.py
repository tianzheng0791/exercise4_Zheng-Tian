#!/usr/bin/env python
# coding: utf-8

# # Zheng Tian
# 
# ## 25/02/2023

# In[11]:


x = lambda num1,num2: num1*num2
x(5,6)


# In[12]:


import math
def area_of_circle(radius):
    area = math.pi * radius ** 2
    return area

print(area_of_circle(10))


# In[13]:


def calculator(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 / num2
    else:
        return "Invalid operator."
result = calculator(2, 5, '/')
print(result)


# In[14]:


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
r = Rectangle(5, 10)
area = r.area()
print(area)


# In[15]:


class Shape:
    def __init__(self, name, length):
        self.name = name
        self.length = length
    
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, name, length):
        super().__init__(name, length)
    
    def area(self):
        return self.length ** 2
    
    def describe(self):
        print("This is a:", self.name)

s = Square('square', 5)
print("The area is:")
print(s.area())
print(s.describe())


# In[ ]:




