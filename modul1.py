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

