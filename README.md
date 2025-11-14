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
I began with direct visualization to understand the data's natural behavior before algorithmic intervention. My initial figures explored the raw feature space, with categorical variable bar charts (output_7_0.png) confirming previous observations. The PreferredLoginDevice distribution revealed mobile users' overwhelming dominance, validating my earlier conclusion about the platform's mobile-centric nature. Other categorical visualizations like MaritalStatus and PreferredPaymentMode displayed notable imbalances that would later inform my cluster interpretation, as certain behavioral patterns appeared more frequently than others.The numerical feature plots (output_8_0.png) revealed different patterns. Almost all numerical features exhibited skewness, with variables like WarehouseToHome and DaySinceLastOrder showing pronounced tails. This suggested potential challenges for distance-based clustering algorithms, as such skewed distributions can compromise cluster boundary integrity. These observations reinforced the necessity of PCA to reduce dimensionality and potentially uncover more robust patterns. The correlation heatmap (output_9_0.png) synthesized these insights, revealing that while correlation between most variables remained weak, meaningful relationships existed—particularly between ordering behaviors and coupon usage. These moderate correlations suggested PCA might effectively consolidate multiple behavioral indicators into unified components, precisely the signal pattern I hoped clustering would identify

### K-Means
After preparing the PCA-transformed dataset, I tackled the question of optimal clustering by implementing K-Means analysis. Looking at output_20_0.png, I observed the Elbow Method plot's distinctive curve flattening near K = 5, while the silhouette scores peaked with a different K value being 2, though both graphs decline in the same direction. Despite the inconsistency with the k value, I found that the algorithmn yielded distinct customer groupings with a healthy distribution - the smallest containing 703 customers and the largest approximately 1300. This relatively even spread indicated well-differentiated segments without any overwhelming the analysis, creating ideal conditions for meaningful behavioral interpretation. Examining the PCA scatter plots with cluster-based coloring revealed compelling separation between groups, despite the dimensional reduction inherent in PCA visualization. That these clusters maintained their coherence even in projected space suggested genuine behavioral patterns rather than statistical artifacts - these customer segments represented authentic differences in user characteristics.

### Algorithmic
To confirm these clusters weren't just artifacts of the K-Means method, I applied Agglomerative Clustering to the same PCA-reduced dataset. This alternative approach constructs clusters hierarchically, progressively combining the nearest groups. The resulting dendrogram (found in the notebook's algorithm section) illustrates this merging process. Despite its complexity due to numerous data points, the visualization reveals distinct "break points"—significant jumps in linkage distance—that correspond remarkably well with our previously identified five-cluster structure. The Agglomerative Clustering results produced segment patterns strikingly similar to our K-Means findings. In both analyses, high-activity customers with consistent purchasing behavior grouped together naturally, while less engaged customers with sporadic ordering patterns formed their own distinct segments. Though the exact cluster boundaries differed between methods—an expected outcome given their different mathematical approaches—the underlying behavioral patterns remained consistent across both techniques, strongly suggesting these customer segments represent genuine structures within the data itself.

### Data Impact and Conclusion
The clustering analysis transformed my understanding of customer behavior from superficial observations to a nuanced framework. The five distinct segments I identified through K-Means and Agglomerative clustering revealed patterns in engagement, satisfaction, ordering habits and platform usage that would have remained invisible otherwise. With these insights, businesses can craft personalized marketing approaches, customize user experiences, and distribute support resources more effectively. Teams gain the ability to flag customers at risk of churning, create targeted promotions, and align product development with actual user needs across different segments. In essence, clustering serves as the crucial connector between raw data points and strategic decision-making, illuminating behavioral patterns that basic visualizations miss.

However, these analytical benefits come with significant ethical considerations. When not handled transparently, segmentation practices can feel like privacy violations to customers. Clusters might inadvertently align with protected characteristics, potentially leading to discriminatory practices or service inequalities. Excessive personalization can create recommendation echo chambers, while categorizing users as "likely to churn" or "low-value" might trigger differential treatment that becomes a self-fulfilling prophecy. To mitigate these risks, organizations should implement regular fairness audits of clustering outputs, maintain transparency about data usage practices, and provide straightforward opt-out mechanisms for personalization. The value of clustering ultimately depends on implementation—balancing analytical power with ethical responsibility to enhance rather than compromise customer experiences.

## References
1) Python Software Foundation. (2023). Python 3.x. Retrieved from https://www.python.org/
2) McKinney, W. (2023). pandas: Python Data Analysis Library. Retrieved from https://pandas.pydata.org/
3) Hunter, J. D. (2007). Matplotlib: A 2D graphics environment. Computing in Science & Engineering, 9(3), 90-95.
4) Waskom, M. L. (2021). seaborn: statistical data visualization. Journal of Open Source Software, 6(60), 3021.

