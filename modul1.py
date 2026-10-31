# 66188 nr indeksu

# 1
import pandas as pd
import numpy as np

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
print(df.T)

# 6
print(df.head(10))

# 7
print(df.tail(10))

# 8
df.info()

# 9
print(df.shape)

# 10
print(df.describe())

# 11
print(df.describe(include="str"))

# 12
df = df.dropna()
print("Liczba brakujacych wartosci po usunieciu:")
print(df.isnull().sum())

# 13
print(df["math score"])
print(df[["gender", "math score", "reading score", "writing score"]])
print(df.iloc[0])
print(df.iloc[0:5])
print(df.loc[0])
print(df.loc[0:4])
print(df.loc[0:4, "math score"])
print(df.loc[:, ["gender", "math score", "writing score"]])

# 14
print(df[df["math score"] >= 90])

# 15
print(df[(df["math score"] >= 90) & (df["gender"] == "female")])

# 16
print(df[df["parental level of education"].str.contains("college", case=False, na=False)])

# 17
print(df[~df["parental level of education"].str.contains("college", case=False, na=False)])

# 18
df["average score"] = df[["math score", "reading score", "writing score"]].mean(axis=1)
print(df[["math score", "reading score", "writing score", "average score"]])

# 19
df_temp = df.copy()
df_temp["temporary column"] = 1
df_temp = df_temp.drop(columns=["temporary column"])
print(df_temp.head())

# 20
df_renamed = df.rename(columns={"math score": "math_score"})
print(df_renamed.head())

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
wyniki = df.groupby("gender").agg({
    "math score": "mean",
    "reading score": "mean",
    "writing score": ["median", "count"]
})
print(wyniki)

# 31
print("Nazwy kolumn MultiIndex:")
print(wyniki.columns)

# 32
print("Sortowanie według średniej z matematyki:")
print(wyniki.sort_values(by=("math score", "mean"), ascending=False))

# 33
tabela = pd.pivot_table(
    df,
    values="math score",
    index="gender",
    columns="test preparation course",
    aggfunc="mean"
)

print("Tabela przestawna:")
print(tabela)

# 34
print("Indeksy tabeli przestawnej:")
print(tabela.index)

print("Kolumny tabeli przestawnej:")
print(tabela.columns)

# 35
tabela_multi = pd.pivot_table(
    df,
    values=["math score", "reading score"],
    index=["gender", "test preparation course"],
    columns=["lunch"],
    aggfunc="mean"
)

print("Tabela przestawna MultiIndex:")
print(tabela_multi)

# 36
import matplotlib.pyplot as plt

# 37
# %matplotlib inline
# W pliku .py wykresy wyswietlamy za pomoca plt.show()

# 38
tabela.plot(kind="bar")

plt.title("Sredni wynik z matematyki wedlug plci i kursu")
plt.xlabel("Plec")
plt.ylabel("Sredni wynik")

plt.tight_layout()
plt.show()

# 39
df["math score"].plot(kind="hist", bins=10)

plt.title("Rozklad wynikow z matematyki")
plt.xlabel("Wynik")
plt.ylabel("Liczba uczniow")

plt.tight_layout()
plt.show()

# 40
df1 = pd.DataFrame({
    "id": [1, 2],
    "imie": ["Anna", "Jan"]
})

df2 = pd.DataFrame({
    "id": [1, 2],
    "wiek": [20, 22]
})

print("Łączenie za pomocą merge:")
print(pd.merge(df1, df2, on="id"))

print("Łączenie za pomocą concat:")
print(pd.concat([df1, df2], ignore_index=True))