---

# 🌸 Iris Data Analysis and Visualization

This project demonstrates how to **load, explore, analyze, and visualize** the Iris dataset using **Python libraries**:  
- `pandas` for data manipulation  
- `matplotlib` and `seaborn` for visualization  
- `scikit-learn` for accessing the dataset  

The script is organized into **six structured steps**. Below we explain the **syntax** and **structure** used.

---

## 🖥️ Project Steps

### 1. Import Libraries
- **Syntax:**
  ```python
  import pandas as pd
  import matplotlib.pyplot as plt
  import seaborn as sns
  from sklearn.datasets import load_iris

import keyword loads external libraries.

as is used to create a shorthand alias (pd, plt, sns).

Libraries serve different purposes: data handling (pandas), plotting (matplotlib, seaborn), and dataset loading (scikit-learn).



---

2. Load Dataset

The dataset is loaded inside a try-except block:

try: runs the code normally.

except Exception as e: catches errors and prints them safely.


load_iris() loads the Iris dataset.

pd.DataFrame() converts the data into a table-like structure.

pd.Categorical.from_codes() maps numerical codes to species names.

print() is used to show confirmation or errors.



---

3. Explore Dataset

Methods used:

.head() → first 5 rows of the dataset

.info() → column types and memory usage

.isnull().sum() → count of missing values


Syntax structure:

object.method() → applies a function (method) to the object (df is a DataFrame).




---

4. Basic Data Analysis

.describe() → summary statistics (mean, std, min, max, quartiles).

.groupby('species').mean() → groups rows by species, then calculates mean of each feature.

Syntax follows method chaining:

df.groupby('species').mean()

groupby() groups data.

.mean() applies aggregation.




---

5. Data Visualization

The script produces four types of plots.

1. Line Chart

plt.plot(x, y, label='...') → plots data lines.

plt.title(), plt.xlabel(), plt.ylabel() → add labels and titles.

plt.legend() → show labels for lines.



2. Bar Chart

sns.barplot(x='species', y='petal length (cm)', data=df, estimator='mean')

x and y define axes.

data=df specifies the source DataFrame.

estimator='mean' means bars represent average values.



3. Histogram

plt.hist(data, bins=15, color='skyblue', edgecolor='black')

bins → number of intervals.

color and edgecolor → customize appearance.



4. Scatter Plot

sns.scatterplot(x=..., y=..., hue='species', data=df)

hue='species' colors points by species.

Shows relationships between two variables.




📌 plt.tight_layout() ensures plots don’t overlap.
📌 plt.show() displays the graph window.


---

6. Observations

Final printed insights:

Setosa has shorter petals than other species.

Sepal width varies more than petal width.

Sepal length and petal length are positively correlated.



---

⚙️ Syntax Highlights

Comments (#): Used to explain code.

Functions (print(), plt.plot()): Perform specific actions.

Objects (df): Variables holding data (e.g., a DataFrame).

Methods (.head(), .describe()): Functions applied to objects.

Chaining (df.groupby().mean()): Multiple methods applied in sequence.

Blocks (try-except): Control flow that handles errors.



---

🚀 How to Run

1. Install required libraries:

pip install pandas matplotlib seaborn scikit-learn


2. Run the Python file in terminal or Jupyter Notebook.


3. Observe printed summaries and generated plots.




---

📊 Summary

This project demonstrates:

Dataset handling with pandas

Statistical analysis with DataFrame methods

Visualization with matplotlib and seaborn

Clean structure using step-wise approach

