import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 1. Processed Dataset Load Karein
df = pd.read_csv('creditcard_processed.csv')

# Features (X) aur Target (y) alag karein
X = df.drop(['Class'], axis=1)
y = df['Class']

# 2. Train aur Test Sets Mein Split Karein
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 3. Model Train Karein (Class Weight Balanced ke sath taaki fraud cases detect ho sakein)
model = RandomForestClassifier(
    n_estimators=100, random_state=42, class_weight='balanced'
)
model.fit(X_train, y_train)

# 4. Model Evaluation Check Karein
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

print('=== Model Performance Evaluation ===')
print(classification_report(y_test, y_pred))
print('ROC-AUC Score:', round(roc_auc_score(y_test, y_prob), 4))

# 5. Full Dataset Par Prediction Scores Add Karein (Power BI ke liye)
df['Fraud_Probability'] = model.predict_proba(X)[:, 1]
df['Predicted_Class'] = model.predict(X)

# Risk Level Category Banayein
df['Risk_Level'] = pd.cut(
    df['Fraud_Probability'],
    bins=[-0.01, 0.3, 0.7, 1.0],
    labels=['Low', 'Medium', 'High'],
)

# 6. Output CSV File Save Karein
df.to_csv('creditcard_predictions.csv', index=False)
print(
    "\nModel predictions successfully saved to 'creditcard_predictions.csv'!"
)