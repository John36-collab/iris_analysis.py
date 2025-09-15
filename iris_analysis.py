#-------------------------------------
Firstly python -m pip install pandas matplotlib seaborn scikit-learn
# -------------------------------------
# Iris Data Analysis and Visualization
# -------------------------------------

# Step 1: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Step 2: Load Dataset
try:
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
    print(" Dataset loaded successfully.\n")
except Exception as e:
    print(f" Error loading dataset: {e}")

# Step 3: Explore Dataset
print("  First 5 rows of the dataset:")
print(df.head())

print("\n  Data Info:")
print(df.info())

print("\n  Missing values:")
print(df.isnull().sum())

# No missing values in Iris dataset, so we don't need to clean here

# Step 4: Basic Data Analysis
print("\n  Descriptive Statistics:")
print(df.describe())

# Group by species and get mean of each feature
print("\n  Mean values grouped by species:")
grouped = df.groupby('species').mean()
print(grouped)

# Step 5: Data Visualization

# Set style
sns.set(style="whitegrid")

# 1. Line Chart (Simulated time series using index)
plt.figure(figsize=(8, 5))
plt.plot(df.index, df['sepal length (cm)'], label='Sepal Length')
plt.plot(df.index, df['petal length (cm)'], label='Petal Length')
plt.title("Line Chart of Sepal and Petal Length Over Index")
plt.xlabel("Index")
plt.ylabel("Length (cm)")
plt.legend()
plt.tight_layout()
plt.show()

# 2. Bar Chart: Average petal length per species
plt.figure(figsize=(6, 4))
sns.barplot(x='species', y='petal length (cm)', data=df, estimator='mean')
plt.title("Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.tight_layout()
plt.show()

# 3. Histogram: Distribution of Sepal Width
plt.figure(figsize=(6, 4))
plt.hist(df['sepal width (cm)'], bins=15, color='skyblue', edgecolor='black')
plt.title("Histogram of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# 4. Scatter Plot: Sepal Length vs Petal Length
plt.figure(figsize=(6, 4))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df)
plt.title("Scatter Plot of Sepal vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend()
plt.tight_layout()
plt.show()

# Step 6: Observations
print("\n  Observations:")
print("- Iris setosa has noticeably shorter petal length than other species.")
print("- Sepal width is more variable than petal width.")
print("- There is a strong positive correlation between sepal and petal lengths.")
