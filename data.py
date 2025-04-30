import pandas as pd

# Load the Titanic training dataset
train_df = pd.read_csv("/mnt/data/train.csv")
train_df.head()

from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

# Set styles
sns.set(style="whitegrid")

# Start writing the EDA notebook content
eda_content = """
# Titanic Dataset - Exploratory Data Analysis (EDA)

## 1. Data Overview

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("train.csv")

# Basic info
df.info()
df.describe(include="all")
df.isnull().sum()
