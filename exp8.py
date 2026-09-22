import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
df = pd.read_csv("student.csv")
df["Extracurricular"] = df["Extracurricular"].map({"Yes": 1, "No": 0})
X = df.drop("Result", axis=1)
y = df["Result"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
print("Decision Tree Classifier")
print("------------------------")
print("Accuracy:", accuracy)
print("\nConfusion Matrix:")
print(cm)