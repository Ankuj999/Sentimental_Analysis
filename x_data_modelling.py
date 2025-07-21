import numpy as np
import pandas as pd
df = pd.read_csv("./x_sentiment_output_self.csv")

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(df["clean_text"])
y = df["sentiment"]

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

from sklearn.metrics import confusion_matrix

y_pred = model.predict(X_test)
y_test_binary = np.where(y_test == "Positive", 1, 0)
y_pred_classes = np.where(y_pred == "Positive", 1, 0)  # Convert probabilities to class labels

print(confusion_matrix(y_test_binary, y_pred_classes))