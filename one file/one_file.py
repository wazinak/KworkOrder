import pandas as pd
import glob

# Получаем список всех файлов CSV в текущем каталоге
csv_files = glob.glob('*.csv')

# Создаем пустой список для хранения DataFrames
dfs = []

# Читаем каждый файл CSV и добавляем его в список DataFrames
for file in csv_files:
    dfs.append(pd.read_csv(file))

# Объединяем все DataFrames в один
df = pd.concat(dfs, ignore_index=True)

# Сохраняем DataFrame в Excel-файл
df.to_excel('parser.xlsx', index=False)
