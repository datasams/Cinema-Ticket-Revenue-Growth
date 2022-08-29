#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Program to calculate Revenue Growth of Ticket sales, given a new discount age inputed by user.

data = {
    "100-90": 25, "42-01": 48, "55-09": 12, "128-64": 71, "002-22": 18, 
    "321-54": 19, "097-32": 33, "065-135": 64, "99-043": 80, "111-99": 11, 
    "123-019": 5, "109-890": 72, "132-123": 27, "32-908": 27, "008-09": 25, 
    "055-967": 35, "897-99": 44, "890-98": 56, "344-32": 65, "43-955": 59, 
    "001-233": 9, "089-111": 15, "090-090": 17, "56-777": 23, "44-909": 27, 
    "13-111": 21, "87-432": 15, "87-433": 14, "87-434": 23, "87-435": 11, 
    "87-436": 12, "87-437": 16, "94-121": 15, "94-122": 35, "80-089": 10, 
    "87-456": 8, "87-430": 40
}

# Take in new discount age from user
age = int(input())

# Calculate Original revenue
original_revenue = 0

for ages in data:
    if data[ages] < 18:
        original_revenue = original_revenue + 5
    else:
        original_revenue = original_revenue + 20

# Calculate New revenue
new_revenue = 0

for ages in data:
    if data[ages] < age:
        new_revenue = new_revenue + 5
    else:
        new_revenue = new_revenue + 20
        
# Calculate and output revenue growth
    
revenue_growth = ((original_revenue - new_revenue) / new_revenue * 100)
print("Revenue Growth = ", revenue_growth, "%")


# In[ ]:




