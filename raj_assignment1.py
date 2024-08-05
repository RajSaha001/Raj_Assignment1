# -*- coding: utf-8 -*-
"""yub_assignment1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mTdqKHedN6qoAm8gGaQVwBWQB-pdjg8R
"""



"""Iris_Flower dataset"""

import pandas as pd

# Load the dataset
df = pd.read_csv("/content/irish_flower_dataset.csv")

# Display the first few rows of the dataset
print(df.head())

# Check for null values
null_values = df.isnull().sum()
print("Null values in each column:\n", null_values)

# Summarize the dataset
summary = df.describe()
print("Summary of the dataset:\n", summary)

# Check data types of columns
data_types = df.dtypes
print("Data types of columns:\n", data_types)

"""calculating the correlation coefficients among the numerical columns and visualize the data"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
df = pd.read_csv("/content/irish_flower_dataset.csv")

# Calculate correlation matrix
correlation_matrix = df.corr(numeric_only=True)

# Display correlation matrix
print("Correlation matrix:\n", correlation_matrix)

# Visualize the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Matrix of Irish Flower Dataset")
plt.show()

"""Abalone Dataset"""

import pandas as pd

# Load the dataset
df = pd.read_csv("/content/Abalone Dataset.csv")

# Display the first few rows of the dataset
print(df.head())

# Check for null values
null_values = df.isnull().sum()
print("Null values in each column:\n", null_values)

# Summarize the dataset
summary = df.describe()
print("Summary of the dataset:\n", summary)

# Check data types of columns
data_types = df.dtypes
print("Data types of columns:\n", data_types)

"""calculating the correlation coefficients among the numerical columns and visualize the data"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
df = pd.read_csv("/content/Abalone Dataset.csv")

# Calculate correlation matrix
correlation_matrix = df.corr(numeric_only=True)

# Display correlation matrix
print("Correlation matrix:\n", correlation_matrix)

# Visualize the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Matrix of Irish Flower Dataset")
plt.show()

"""Ionosphere Dataset"""

import pandas as pd

# Load the dataset
df = pd.read_csv("/content/ionosphere (1).csv")

# Display the first few rows of the dataset
print(df.head())

# Check for null values
null_values = df.isnull().sum()
print("Null values in each column:\n", null_values)

# Summarize the dataset
summary = df.describe()
print("Summary of the dataset:\n", summary)

# Check data types of columns
data_types = df.dtypes
print("Data types of columns:\n", data_types)

"""calculating the correlation coefficients among the numerical columns and visualize the data"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
df = pd.read_csv("/content/ionosphere (1).csv")

# Calculate correlation matrix
correlation_matrix = df.corr(numeric_only=True)

# Display correlation matrix
print("Correlation matrix:\n", correlation_matrix)

# Visualize the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Matrix of Irish Flower Dataset")
plt.show()

"""Boston Dataset"""

import pandas as pd

# Load the dataset
df = pd.read_csv("/content/boston.csv")

# Display the first few rows of the dataset
print(df.head())

# Check for null values
null_values = df.isnull().sum()
print("Null values in each column:\n", null_values)

# Summarize the dataset
summary = df.describe()
print("Summary of the dataset:\n", summary)

# Check data types of columns
data_types = df.dtypes
print("Data types of columns:\n", data_types)

"""calculating the correlation coefficients among the numerical columns and visualize the data"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
df = pd.read_csv("/content/boston.csv")

# Calculate correlation matrix
correlation_matrix = df.corr(numeric_only=True)

# Display correlation matrix
print("Correlation matrix:\n", correlation_matrix)

# Visualize the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Matrix of Irish Flower Dataset")
plt.show()

"""Wheat Dataset"""

import pandas as pd

# Load the dataset
df = pd.read_csv("/content/Wheat.csv")

# Display the first few rows of the dataset
print(df.head())

# Check for null values
null_values = df.isnull().sum()
print("Null values in each column:\n", null_values)

# Summarize the dataset
summary = df.describe()
print("Summary of the dataset:\n", summary)

# Check data types of columns
data_types = df.dtypes
print("Data types of columns:\n", data_types)

"""calculating the correlation coefficients among the numerical columns and visualize the data"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
df = pd.read_csv("/content/Wheat.csv")

# Calculate correlation matrix
correlation_matrix = df.corr(numeric_only=True)

# Display correlation matrix
print("Correlation matrix:\n", correlation_matrix)

# Visualize the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Matrix of Irish Flower Dataset")
plt.show()