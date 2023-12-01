from collections import defaultdict
import re

def extract_clean_text(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read().lower()  # Перетворюємо текст у нижній регістр

            # Видаляємо всі символи пунктуації окрім пробілу
            content = re.sub(r'[^абвгдєжзийкалмнопірстуфхцчшщьюяґї ]', '', content)
            return content
    except FileNotFoundError:
        print(f"Файл '{file_name}' не знайдено")
        return ''

def calculate_trigram_frequencies(text):
    trigram_frequencies = defaultdict(int)
    total_trigrams = 0

    # Підрахунок відносних частот триграм
    for i in range(len(text) - 2):
        if text[i] != ' ' and text[i + 1] != ' ' and text[i + 2] != ' ':
            trigram = text[i:i + 3]
            trigram_frequencies[trigram] += 1
            total_trigrams += 1

    # Конвертуємо кількості у відносні частоти
    for trigram in trigram_frequencies:
        trigram_frequencies[trigram] /= total_trigrams

    return trigram_frequencies

def main():
    files_to_analyze = ['shyfr.txt']  # Список файлів для аналізу

    for file_name in files_to_analyze:
        text = extract_clean_text(file_name)
        if text:
            print(f"Аналізуємо файл '{file_name}':")
            frequencies = calculate_trigram_frequencies(text)

            # Виводимо результати (приклад)
            sorted_frequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
            for trigram, frequency in sorted_frequencies[:30]:  # Перші 30 найбільш ймовірних триграм
                print(f"{trigram},{frequency:.6f}")

            # Можна також створити таблицю частот або відобразити іншу інформацію про триграми

if __name__ == "__main__":
    main()
