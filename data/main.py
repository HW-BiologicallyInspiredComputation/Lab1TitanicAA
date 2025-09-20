import pandas as pd
import numpy as np

df = pd.read_csv("data/train.csv")

df.drop(columns=['Name', 'Ticket', 'Cabin'], inplace=True)

df['Sex'] = df['Sex'].map({'female': 0, 'male': 1})
df['Embarked'] = df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})

df.dropna(subset=['Age'], inplace=True)

num_rows = df.shape[0]

df.dropna(subset=['Embarked'], inplace=True)
df['Embarked'] = df['Embarked'].astype(int)

print(df.head(20))

num_rows = df.shape[0]
print(num_rows)

# Convert DataFrame to NumPy array
df_numpy = df.to_numpy()
print("\nNumPy array shape:", df_numpy.shape)
print("\nFirst 5 rows of NumPy array:")
print(df_numpy[:5])


