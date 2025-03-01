import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Assuming we have the data loaded from an Excel file
# For this example, I'll create a sample dataset based on the rows you've shown
# In a real scenario, you would load your data from Excel: df = pd.read_excel('your_file.xlsx')

# Create sample data based on the excel sheet you provided
data = {
    'Feature_1': [1.00082, 0.85141, -1.07369, 0.604097, 0.245499, 0.945633, -0.30434, -0.21673, 0.450812, 0.63687],
    'Feature_2': [-0.78167, -1.3158, 0.458318, 1.361007, -0.25519, 0.504365, -0.31293, -0.25922, 0.209686, -0.67101],
    'Feature_3': [-0.84763, -0.46595, -0.71481, 0.064791, -1.70462, -0.5413, 0.618556, 0.124385, 0.457542, -1.09584],
    'Feature_4': [0.818595, 0.822989, 1.794525, 0.765437, -0.08313, -1.97682, 1.985676, -0.82829, 0.433748, -1.10445],
    'Feature_5': [0.921936, 0.041542, 1.544841, 1.47772, 0.823423, -0.49522, 0.123529, 0.120199, -1.7719, 0.433542],
    'Target': [0, 0, 1, 1, 1, 0, 1, 0, 0, 0]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Split features and target
X = df.drop('Target', axis=1)
y = df['Target']

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