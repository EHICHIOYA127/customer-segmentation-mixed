# CUSTOMER'S SEGREGATION

To understand the behaviour of the customers visiting a shoping mall, we implemented a unsupervised machine learning model to segregate the customers and performing various analysis such as:

* Find out the average age of the customers in the dataset.
* Analyze the average annual income.
* find out the total number of male and female in the dataset.
* Figure out what the average monthly visists by the customers in the dataset
* Figure out the average spending score of the customers in the dataset


Next, I decide to look through 'customer_segmentation_mixed.csv' and acquaint myself with the data. Things I look for are the following:
* The names of columns and rows
* Any noticeable missing data
* Types of values (numerical vs. categorical)

Investigating these will allow me to think more critically about my analysis I do as well as plan out how I will import the data into my Python file. 


## The dataset contains 350 rows and 6 columns. The columns are:

* age: int64 (350 non-null) - a numeric variable indicating the age of the customers.
* annual_income: int64 (350 non-null) - a numeric variable indicating the customers yearly income.
* spending_score: int64 (350 non-null) - a numeric variable indicating the spending of the cusstomers.
* monthly_visits: int64 (350 non-null) - a numerical variable indcating how many times a customer visited.
* gender: object (350 non-null) -a binary categorical variable indicating the gender of the customers.
* preferred_product: object (350 non-null)  categorical variable indicating the product each customer is interested in.

We can also use the describe() method to get a summary of the numerical columns in the data frame.


## Visualizing the data
Finally, we can create visualizations to get a better understanding of the data. For example, we can use a histogram to visualize the distribution of a numerical column (age).