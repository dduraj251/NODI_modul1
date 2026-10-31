# 66188 nr indeksu

# 1
import pandas as pd

# 2
dane = {
    "imie": ["Anna", "Jan", "Ola"],
    "wiek": [20, 22, 21]
}

df_przyklad = pd.DataFrame(dane)

# 3
dane_lista = [
    ["Anna", 20],
    ["Jan", 22],
    ["Ola", 21]
]

df_lista = pd.DataFrame(dane_lista, columns=["imie", "wiek"])

# 4
import kagglehub

sciezka = kagglehub.dataset_download("spscientist/students-performance-in-exams")
print(sciezka)

df = pd.read_csv(f"{sciezka}/StudentsPerformance.csv")

# 5
print(df.head())

# 6
print(df.tail())

# 7
df.info()

# 8
print(df.shape)

# 9
print(df.describe())

# 10
print(df.describe(include="str"))

# 11
print(df.isnull().sum())

# 12
print(df["math score"])

# 13
print(df[["gender", "math score", "reading score", "writing score"]])

# 14
print(df.iloc[0])

# 15
print(df.iloc[0:5])

# 16
print(df.loc[0])

# 17
print(df.loc[0:4])

# 18
print(df.loc[0:4, "math score"])

# 19
print(df.loc[:, ["gender", "math score", "writing score"]])

# 20
print(df[df["math score"] >= 90])

# 21
df.to_csv("StudentsPerformance_zapis.csv", index=False)
print("Ramka danych została zapisana do pliku CSV.")

# 22
print("Średnia ocen z matematyki:", df["math score"].mean())
print("Najwyższa ocena z matematyki:", df["math score"].max())
print("Najniższa ocena z matematyki:", df["math score"].min())

# 23
print("Liczba wierszy:", len(df))

# 24
print("Unikalne wartości w kolumnie gender:")
print(df["gender"].unique())

# 25
print("Liczba rekordów dla każdej płci:")
print(df["gender"].value_counts())

# 26
print("Sortowanie rosnąco według wyniku z matematyki:")
print(df.sort_values(by="math score"))

print("Sortowanie malejąco według wyniku z matematyki:")
print(df.sort_values(by="math score", ascending=False))

# 27
print("10 największych wyników z matematyki:")
print(df.nlargest(10, "math score"))

print("10 najmniejszych wyników z matematyki:")
print(df.nsmallest(10, "math score"))

# 28
print("10 największych wyników z matematyki wśród osób po kursie przygotowawczym:")
df_completed = df[df["test preparation course"] == "completed"]
print(df_completed.nlargest(10, "math score"))

# 29
print("Średnie wyniki według płci:")
print(df.groupby("gender").mean(numeric_only=True))

# 30
print("Statystyki wyników według płci:")
print(df.groupby("gender").agg({
    "math score": "mean",
    "reading score": "mean",
    "writing score": ["median", "count"]
}))