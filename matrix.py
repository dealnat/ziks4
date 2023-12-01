import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Завантаження даних з CSV файлу з біграмами та їхньою кількістю
# Припустимо, що CSV файл містить стовпці 'біграма' і 'кількість'
file_path = 'bieneida.csv'
data = pd.read_csv(file_path)

# Створення матриці для теплової карти
alphabet = ['а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я']
heatmap_data = pd.DataFrame(index=alphabet, columns=alphabet).fillna(0)

# Заповнення матриці кількостями біграм
for index, row in data.iterrows():
    first_char = row['Bigram'][0]
    second_char = row['Bigram'][1]
    heatmap_data.at[first_char, second_char] = row['Count']

# Створення теплової карти
plt.figure(figsize=(12, 8))
sns.heatmap(heatmap_data, annot=True, fmt='g', cmap='coolwarm')
plt.xlabel('Другий символ')
plt.ylabel('Перший символ')
plt.title('Теплова карта біграм')
plt.show()
