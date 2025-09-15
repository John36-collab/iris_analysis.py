

Iris Data Analysis and Visualization

Overview

This project performs an exploratory data analysis and visualization of the famous Iris flower dataset, which contains measurements of sepal and petal dimensions across three iris species: setosa, versicolor, and virginica.

Dataset Information

The Iris dataset is a well-known multivariate dataset introduced by Ronald Fisher in 1936. It contains:

· 150 observations (50 per species)
· 4 numerical features:
  · Sepal length (cm)
  · Sepal width (cm)
  · Petal length (cm)
  · Petal width (cm)
· 1 categorical target variable (species)

Analysis Steps

1. Data Loading and Preparation

· Successfully loaded the Iris dataset using scikit-learn's built-in data loader
· Created a pandas DataFrame with proper column names
· Added species information as a categorical variable

2. Initial Data Exploration

· Examined the first 5 rows of the dataset
· Checked dataset information and structure
· Verified no missing values in the dataset

3. Statistical Analysis

· Generated descriptive statistics for all numerical features
· Calculated mean values grouped by species for each feature

4. Visualizations Created

· Line Chart: Displayed sepal and petal length values across the dataset index
· Bar Chart: Compared average petal length across the three species
· Histogram: Showed distribution of sepal width measurements
· Scatter Plot: Explored relationship between sepal length and petal length, colored by species

Key Observations

1. Iris setosa has noticeably shorter petal length compared to the other two species
2. Sepal width shows more variability than petal width across all species
3. There is a strong positive correlation between sepal length and petal length
4. The visualizations clearly show distinct clusters corresponding to the different species

Tools Used

· Pandas for data manipulation
· Matplotlib and Seaborn for visualizations
· Scikit-learn for data loading

This analysis provides comprehensive insights into the characteristics of the Iris dataset and demonstrates clear distinctions between the three iris species based on their morphological measurements.
