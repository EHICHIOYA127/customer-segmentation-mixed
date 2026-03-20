import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

customer_age = []
customer_gender = []
customer_annual_income = []
customer_spending_score = []
customer_monthly_visits = []
customer_preferred_product = []

cust_seg = pd.read_csv('customer_segmentation_mixed.csv')

# This command shows us how many users visited the site from different sources in different months.
df.groupby(['month', 'utm_source']).id.count()\
.reset_index()\
.pivot(columns='month', index='utm_source', values='id')
    
    
orders = pd.read_csv('orders.csv')
pricey_shoes = orders.groupby('shoe_type').price.max()
print(pricey_shoes)
print(type(pricey_shoes)) 
    
   
cust_seg.head(20) 


cust_seg.info()
 
 
plt.hist(cust_seg['Age'], bins=10)
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

# Calculate the average age
avg_age = cust_seg['Age'].mean()

print('The average age of the customers is: {} years.'.format(round(avg_age, 2)))

cust_seg.groupby('Gender')['Gender'].count()


# Calculate the average annual income
avg_annual_income = cust_seg['Annual_Income'].mean()

print('The Average Annual Income of the customers is:  {} dollars.'.format(round(avg_annual_income, 2)))


# Calculate the average monthly visits
avg_monthly_visits = cust_seg['Monthly_Visits'].mean()

print('The Average Monthly Visits of the customers is:  {} times per month.'.format(round(avg_monthly_visits, 2)))


# Calculate the average spending score
avg_spending_score = cust_seg['Spending_Score'].mean()

print('The Average Spending Score of the customers is:  {} dollars.'.format(round(avg_spending_score, 2)))


Product_counts = cust_seg.groupby('Preferred_Product').Age.count().reset_index()
print(Product_counts)



