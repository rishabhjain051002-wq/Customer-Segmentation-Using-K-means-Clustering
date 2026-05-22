# CUSTOMER-SEGMENTATION-USING-CLUSTERING
### README for Customer Segmentation Project

---

#### Project Overview

This project involves customer segmentation based on key attributes such as **Gender**, **Age**, **Annual Income**, and **Spending Score** using the **KMeans Clustering Algorithm**. The goal is to group customers into distinct clusters to understand their behaviors and patterns better. By using unsupervised machine learning techniques, we identify different customer segments that can help businesses target specific groups for personalized marketing strategies.

---

#### Project Details

**Data Columns:**
- **CustomerID**: Unique identifier for each customer.
- **Gender**: Gender of the customer (Male/Female).
- **Age**: Age of the customer in years.
- **Annual Income (k$)**: The annual income of the customer in thousands of dollars.
- **Spending Score (1-100)**: A score assigned to customers based on their spending behavior (from 1 to 100).
- **Age Group**: The age category assigned based on predefined ranges: `19-30`, `31-45`, `46-60`, `60+`.
- **Cluster**: The cluster label assigned to each customer based on KMeans clustering.

The dataset consists of customer information, where each customer is categorized into one of the five clusters, identified using KMeans clustering. The clusters represent groups of customers with similar characteristics in terms of age, income, and spending behavior.

---

#### Objectives

- **Customer Segmentation**: Use KMeans clustering to divide customers into distinct groups based on age, income, and spending score.
- **Exploratory Data Analysis (EDA)**: Analyze the data and gain insights on customer behavior and segment distribution.
- **Visualization**: Generate visual representations of the clusters to better understand the relationships between age, income, spending score, and cluster assignment.

---

#### Steps Involved

1. **Data Preprocessing**:
    - Clean the dataset by handling missing values, duplicate records, and outliers.
    - Convert categorical variables (Gender) into numerical values if required.

2. **Feature Engineering**:
    - Create an "Age Group" column by segmenting customers into predefined age ranges: `19-30`, `31-45`, `46-60`, and `60+`.

3. **KMeans Clustering**:
    - Apply the KMeans clustering algorithm to group customers into 5 clusters based on their **Age** and **Annual Income**.

4. **Cluster Evaluation**:
    - Use the **Elbow Method** to determine the optimal number of clusters for KMeans.
    - Visualize the clusters using scatter plots, color-coded by cluster labels.

5. **Analysis & Insights**:
    - Analyze the results and interpret the characteristics of each cluster, identifying patterns in spending behavior, income, and age.

---

#### Tools and Libraries Used

- **Python**: Programming language used for analysis and machine learning.
- **pandas**: Data manipulation and analysis library.
- **matplotlib**: Plotting library for data visualization.
- **seaborn**: Statistical data visualization library.
- **scikit-learn**: Machine learning library that includes the KMeans algorithm for clustering.

---

#### Output

The output of this project includes:
- A **cluster label** assigned to each customer, indicating their group.
- **Scatter plots** showing the distribution of customers based on their age and annual income, with color coding based on their cluster labels.
- Insights into customer behavior, such as the relationship between **Annual Income**, **Age**, and **Spending Score**.

---

#### Example Data

| CustomerID | Gender | Age | Annual Income (k$) | Spending Score (1-100) | Age Group | Cluster |
|------------|--------|-----|---------------------|------------------------|-----------|---------|
| 1          | Male   | 19  | 15                  | 39                     | 19-30     | 3       |
| 2          | Male   | 21  | 15                  | 81                     | 19-30     | 4       |
| 3          | Female | 20  | 16                  | 6                      | 19-30     | 3       |
| 4          | Female | 23  | 16                  | 77                     | 19-30     | 4       |
| 5          | Female | 31  | 17                  | 40                     | 31-45     | 3       |
| ...        | ...    | ... | ...                 | ...                    | ...       | ...     |
| 196        | Female | 35  | 120                 | 79                     | 31-45     | 1       |
| 197        | Female | 45  | 126                 | 28                     | 46-60     | 2       |
| 198        | Male   | 32  | 126                 | 74                     | 31-45     | 1       |
| 199        | Male   | 32  | 137                 | 18                     | 31-45     | 2       |
| 200        | Male   | 30  | 137                 | 83                     | 31-45     | 1       |

---

#### How to Run

1. **Clone the Repository**:
   - Clone this repository to your local machine using:
     ```bash
     gh repo clone Himansh9532/CUSTOMER-SEGMENTATION-USING-CLUSTERING
     ```

2. **Install Dependencies**:
   - Make sure to install the required libraries:
     ```bash
     pip install -r requirements.txt
     ```

3. **Run the Analysis**:
   - Run the Python script or Jupyter notebook to see the customer segmentation and visualizations.
     ```bash
     python app.py
     ```

---

#### Future Work

- **Dynamic Clustering**: Explore different clustering algorithms (e.g., DBSCAN, Agglomerative Clustering) to compare results.
- **Additional Features**: Use additional customer attributes such as location, transaction history, etc., to improve segmentation.
- **Advanced Visualization**: Create interactive visualizations with tools like Plotly or Dash for deeper analysis.

---



This `README.md` file provides an overview of the project, how to run it, and the steps involved in the analysis. You can adjust the sections to fit specific project requirements.
