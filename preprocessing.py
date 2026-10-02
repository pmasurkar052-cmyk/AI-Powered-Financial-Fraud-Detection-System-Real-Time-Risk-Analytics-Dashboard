import pandas as pd
from sklearn.preprocessing import StandardScaler

# 1. Dataset load karein
df = pd.read_csv('creditcard_10k.csv')

print('Dataset Shape:', df.shape)
print('Missing Values:', df.isnull().sum().sum())
print('Class Distribution:\n', df['Class'].value_counts())

# 2. Feature Scaling for 'Amount' and 'Time'
scaler = StandardScaler()
df['Scaled_Amount'] = scaler.fit_transform(df['Amount'].values.reshape(-1, 1))
df['Scaled_Time'] = scaler.fit_transform(df['Time'].values.reshape(-1, 1))

# Purane unscaled columns hata sakte hain ya rakh bhi sakte hain
df = df.drop(['Time', 'Amount'], axis=1)

# Cleaned data ko save karein
df.to_csv('creditcard_processed.csv', index=False)
print(
    '\nPreprocessing complete! Processed file saved as'
    " 'creditcard_processed.csv'."
)