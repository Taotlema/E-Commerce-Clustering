# E-Commerce-Clustering

This Github repository was build for a Data Mining Class at UNCC where I (Ayemhenre Isikhuemhen) focused on exploring and implementing clustering techniques. 

## Introduction

There was once a time where I applied and interviewed for a Data Analyst role for a company. As a part of the interview process, I was tasked with mining a data file for a hypothetical E-commerce company. With the end goal of not only displaying my data and ML skills but also find significant insight about the consumer based given the data. At the time, I didn't know much about machine learning, but I have since grown and am interested in applying clustering techniques to mine insights. Ultimately as conduct this project, the question I want to answer goes as following. **What can clustering tells us about consumer behavoir, and how does applying this technique inform product and data decision-making**

### Clustering Overview
Before further discussing the project, I would like to take a moment to talk about what clustering is, and how it works. Clustering is an unsupervised machine learning technique that specializes in grouping unlabeled data into what we call clusters. These cluster are thus formed based on the simmilarities between different data points. It can be best be imagining as the computer naturally discovering how the data behaves unlike supervised machine learning that requires pre-labeled data. Of course, there are many ways for clustering to work, the two used in this project are listed below. 

1) **K-Means:**  
Breaks down data using a "mean" (statistics) to generate a k value of seperate and distinct clusters. This physically minimizes variance, and is known to be a fast and effiecent form of clustering. K-means, typically is great for working on sphereical clusters. While this technique is good for large datasets its does struggle with high-dimensional data.

2) **Agglomerative Clustering:**  
This techniques focuses on building a hierarchy of clusters by iteratively merging cluster or groups with simmilarities. Effectively, clustering by a top down of what elements are the most simmilar. This is indeed a more computationally expesnsice process but it is great for trying to capture more complex and hidden relationships within a dataset. Though its output is quite sensitive to outliers within the dataset.

There's a lot of potiencial with these techniques, however, not only are you choosing your bread, but also your poison.  

## Understanding the Data

The data used was provided by Method during their interview process, they kindly provided an index on the variables in the dataset that go as following:

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

The dataset used for this project was largely clean, and didn't have a lot of issues, however, I would still need to modify it to optimze it for use in clustering. When modifying this dataset, I focused on filling missing values, particularly filling in numerical values with medans, and catagorical values with mode. I would also drop the customer ID column since it wouldn't be very relvant for clustering. 

While typically clean up is what is needed to simply visual or generate tables from data, clustering requires one more technique known as **PCA**. Which is used to reduce the dimensionality or in other terms complexity of data while preserving variance necessary for cluster distinction. Ultimately, using PCA help transformed the orginal dataset into something more useful when applying **K-means** and **Algorithmic** algroithms.

### Past Data Investigation
Prior is learning machine learning techniques, I relied heavily on using visualizations such as pie charts, box plots, and tables to understand data behavoir within any given dataset. For the the e-commerce data in particular, I was able to identify the following:

- About 71% of customers prefered using their phone to engage with the hypothetical e-commerce platform. Despite most phone uses being 2.3x more likely to have muiltiple devices. Sugguesting a strong preference for mobile accessiblity.
- Debit Cards and Credit Cards made up a large share of prefered pament methods. With no notable distinct between complaint rates between the two payment methods.
- Coupon usage was explored and regualrly used across all payment types, which would show room for deeper customer engagement via discounts and consumer deals.

Ultimately, however, strictly relying on visualizations only provided grounds to make sugguestions rather than make decisions based on concrete decision making. While visualizations are best served for story-telling, I would like to see how reliable clustering can be to make high-level business and product decisions. 

### Preprocessing
   
## Clustering Investingation

### PCA

### K-Means

### Algorithmic

### Data Impact and Conclusion

## References
1) Python Software Foundation. (2023). Python 3.x. Retrieved from https://www.python.org/
2) McKinney, W. (2023). pandas: Python Data Analysis Library. Retrieved from https://pandas.pydata.org/
3) Hunter, J. D. (2007). Matplotlib: A 2D graphics environment. Computing in Science & Engineering, 9(3), 90-95.
4) Waskom, M. L. (2021). seaborn: statistical data visualization. Journal of Open Source Software, 6(60), 3021.
