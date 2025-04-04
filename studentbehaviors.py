# -*- coding: utf-8 -*-
"""StudentBehaviors.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14CJRbpmZIfXCmFbPSz3_PFWTdLfuEAwo
"""

!wget -q 'https://drive.google.com/uc?export=download&id=1fwz1B2zzBAjlG8fx8qqmJmKK2v9YCDD2' -O "overdrawn.csv"

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Read the dataset
df = pd.read_csv('overdrawn.csv')

# Convert 'DaysDrink' into categorical data
conditions = [
    (df['DaysDrink'] < 7),
    (df['DaysDrink'] >= 14),
    (df['DaysDrink'] >= 7) & (df['DaysDrink'] < 14)
]
categories = [0, 2, 1]

# Apply the conditions to create the categorical data
df['DaysDrink'] = np.select(conditions, categories)

# Splitting features and target variable
X = df[['Age', 'Sex', 'DaysDrink']]
y = df['Overdrawn']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Create and train the Decision Tree classifier
dtree = DecisionTreeClassifier()
dtree.fit(X_train, y_train)

# Make predictions on the testing set
predictions = dtree.predict(X_test)

# Print the accuracy score and confusion matrix
print("Accuracy Score:", accuracy_score(y_test, predictions))
print("Confusion Matrix:")
print(confusion_matrix(y_test, predictions))

from sklearn import tree
import graphviz

# Export the decision tree to a Graphviz dot file
dot_data = tree.export_graphviz(dtree, out_file=None,
                                feature_names=['Age', 'Sex', 'DaysDrink'],
                                class_names=['Not Overdrawn', 'Overdrawn'],
                                filled=True, rounded=True)

# Convert the dot file to a graph and render it
graph = graphviz.Source(dot_data)
graph.render('overdrawn_dt', view=True)

# Define a function to make predictions for new data points
def predict_overdrawn(age, sex, days_drink):
    # Convert days_drink into categorical data
    if days_drink < 7:
        days_drink_cat = 0
    elif days_drink >= 14:
        days_drink_cat = 2
    else:
        days_drink_cat = 1

    # Make a prediction
    prediction = dtree.predict([[age, sex, days_drink_cat]])
    if prediction[0] == 1:
        return "Yes"
    else:
        return "No"

# Queries
queries = [
    (20, 0, 10),  # 20-year-old male, 10 days of drinking
    (25, 1, 5),   # 25-year-old female, 5 days of drinking
    (19, 0, 20),  # 19-year-old male, 20 days of drinking
    (22, 1, 15),  # 22-year-old female, 15 days of drinking
    (21, 0, 20)   # 21-year-old male, 20 days of drinking
]

# Perform predictions for each query
for i, query in enumerate(queries, 1):
    age, sex, days_drink = query
    prediction = predict_overdrawn(age, sex, days_drink)
    print(f"Prediction {i}: Will the student overdraw a checking account? {prediction}")