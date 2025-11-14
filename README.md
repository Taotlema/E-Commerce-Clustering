# E-Commerce-Clustering

This GitHub repository was built for a Data Mining Class at UNCC, where I (Ayemhenre Isikhuemhen) focused on exploring and implementing clustering techniques. 

## Introduction

There was once a time when I applied and interviewed for a Data Analyst role at a company. As a part of the interview process, I was tasked with mining a data file for a hypothetical E-commerce company. With the end goal of not only displaying my data and ML skills but also finding significant insight about the consumer, given the data. At the time, I didn't know much about machine learning, but I have since grown and am interested in applying clustering techniques to mine insights. Ultimately, as I conduct this project, the question I want to answer goes as follows. **What can clustering tell us about consumer behavior, and how does applying this technique inform product and data decision-making**

### Clustering Overview
Before further discussing the project, I would like to take a moment to talk about what clustering is and how it works. Clustering is an unsupervised machine learning technique that specializes in grouping unlabeled data into what we call clusters. These clusters are thus formed based on the similarities between different data points. It can be best imagined as the computer naturally discovering how the data behaves unlike supervised machine learning that requires pre-labeled data. Of course, there are many ways for clustering to work; the two used in this project are listed below. 

1) **K-Means:**  
Breaks down data using a "mean" (statistics) to generate a k value of separate and distinct clusters. This physically minimizes variance and is known to be a fast and efficient form of clustering. K-means typically is great for working on spherical clusters. While this technique is good for large datasets, it does struggle with high-dimensional data.

2) **Agglomerative Clustering:**  
This technique focuses on building a hierarchy of clusters by iteratively merging clusters or groups with similarities. Effectively, clustering by a top-down approach of what elements are the most similar. This is indeed a more computationally expensive process, but it is great for trying to capture more complex and hidden relationships within a dataset. Though its output is quite sensitive to outliers within the dataset.

There's a lot of potential with these techniques; however, not only are you choosing your bread, but also your poison.  

## Understanding the Data

The data used was provided by Method during their interview process. They kindly provided an index on the variables in the dataset that goes as follows:

- **CustomerID:** Unique customer ID
- **Churn:**	Churn Flag
- **Tenure:**	Tenure of customer in organization
- **PreferredLoginDevice:**	Preferred login device of customer
- **CityTier:**	City tier
- **WarehouseToHome:**	Distance in between warehouse to home of customer
- **PreferredPaymentMode:**	Preferred payment method of customer
- **Gender:**	Gender of customer
- **HourSpendOnApp:**	Number of hours spend on mobile application or website
- **NumberOfDeviceRegistered:**	Total number of deceives is registered on particular customer
- **PreferedOrderCat:**	Preferred order category of customer in last month
- **SatisfactionScore:**	Satisfactory score of customer on service
- **MaritalStatus:**	Marital status of customer
- **NumberOfAddress:**	Total number of added added on particular customer
- **Complain:**	Any complaint has been raised in last month
- **OrderAmountHikeFromlastYear:**	Percentage increases in order from last year
- **CouponUsed:**	Total number of coupon has been used in last month
- **OrderCount:**	Total number of orders has been places in last month
- **DaySinceLastOrder:**	Day Since last order by customer
- **CashbackAmount:**	Average cashback in last monthg

The dataset used for this project was largely clean and didn't have a lot of issues; however, I would still need to modify it to optimize it for use in clustering. When modifying this dataset, I focused on filling missing values, particularly filling in numerical values with medians, and categorical values with mode. I would also drop the customer ID column since it wouldn't be very relevant for clustering. 

While typically, clean up is what is needed to simply visualize or generate tables from data, clustering requires one more technique known as **PCA**. It is used to reduce the dimensionality, or in other terms, the complexity of data while preserving the variance necessary for cluster distinction. Ultimately, using PCA helps transform the original dataset into something more useful when applying **K-means** and **Algorithmic** algorithms.

### Past Data Investigation
Prior to learning machine learning techniques, I relied heavily on using visualizations such as pie charts, box plots, and tables to understand data behavior within any given dataset. For the e-commerce data in particular, I was able to identify the following:

- About 71% of customers preferred using their phone to engage with the hypothetical e-commerce platform. Despite most phone users being 2.3x more likely to have multiple devices. Suggesting a strong preference for mobile accessibility.
- Debit Cards and Credit Cards made up a large share of preferred payment methods. There is no notable difference between complaint rates between the two payment methods.
- Coupon usage was explored and regularly used across all payment types, which would show room for deeper customer engagement via discounts and consumer deals.

Ultimately, however, strictly relying on visualizations only provided grounds to make suggestions rather than make decisions based on concrete decision-making. While visualizations are best suited for storytelling, I would like to see how reliable clustering can be to make high-level business and product decisions. 
   
## Clustering Investigation

### Visualization

### K-Means

### Algorithmic

### Data Impact and Conclusion

## References
1) Python Software Foundation. (2023). Python 3.x. Retrieved from https://www.python.org/
2) McKinney, W. (2023). pandas: Python Data Analysis Library. Retrieved from https://pandas.pydata.org/
3) Hunter, J. D. (2007). Matplotlib: A 2D graphics environment. Computing in Science & Engineering, 9(3), 90-95.
4) Waskom, M. L. (2021). seaborn: statistical data visualization. Journal of Open Source Software, 6(60), 3021.

