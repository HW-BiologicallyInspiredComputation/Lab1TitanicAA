import pandas as pd

df = pd.read_csv("data/train.csv")

df.drop(columns=['Name', 'Ticket', 'Cabin'], inplace=True)

df['Sex'] = df['Sex'].map({'female': 0, 'male': 1})
df['Embarked'] = df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})

df.dropna(subset=['Age'], inplace=True)

num_rows = df.shape[0]
print(num_rows)

df.dropna(subset=['Embarked'], inplace=True)

print(df.head(50))

num_rows = df.shape[0]
print(num_rows)


