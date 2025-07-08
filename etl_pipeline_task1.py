# etl_pipeline_task1.py

import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Sample dataset
data = {
    'age': [25, np.nan, 35, 28, 52],
    'salary': [50000, 60000, np.nan, 58000, 62000],
    'city': ['New York', 'Los Angeles', 'New York', np.nan, 'Chicago'],
    'purchased': ['Yes', 'No', 'Yes', 'No', 'Yes']
}
df = pd.DataFrame(data)

# Separate features and target
X = df.drop(columns=['purchased'])
y = df['purchased']

# Identify column types
categorical_cols = X.select_dtypes(include=['object']).columns.tolist()
numerical_cols = X.select_dtypes(include=['int64', 'float64']).columns.tolist()

# Pipelines for transformation
numeric_transformer = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(handle_unknown='ignore'))
])

# ColumnTransformer
preprocessor = ColumnTransformer([
    ('num', numeric_transformer, numerical_cols),
    ('cat', categorical_transformer, categorical_cols)
])

# Fit and transform
X_processed = preprocessor.fit_transform(X)

# Show results
print("Original Data:")
print(df)

print("\nProcessed Feature Shape:", X_processed.shape)
print("Sample Processed Features (first 3 rows):")
print(X_processed[:3])
