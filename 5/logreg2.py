import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Load the data from CSV file
# Assuming the CSV file has headers Feature_1, Feature_2, Feature_3, Feature_4, Feature_5, Target
df = pd.read_csv('5/Question5_Multi_Class_Dataset 1.csv')

# Split features and target
X = df.iloc[:, :4]  # Select all rows, first 5 columns (features)
y = df.iloc[:, 4]   # Select all rows, 6th column (target)

# Alternative way to split if the column names are as expected:
# X = df[['Feature_1', 'Feature_2', 'Feature_3', 'Feature_4', 'Feature_5']]
# y = df['Target']

# Split the dataset into 75% training and 25% testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Train the logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

# Round to 3 digits after the decimal point
accuracy = round(accuracy, 3)
precision = round(precision, 3)
recall = round(recall, 3)
f1 = round(f1, 3)

print(f"Accuracy: 0,{int(accuracy*1000)}")
print(f"Precision: 0,{int(precision*1000)}")
print(f"Recall: 0,{int(recall*1000)}")
print(f"F1 Score: 0,{int(f1*1000)}")