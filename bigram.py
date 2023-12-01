from collections import defaultdict
import re

def extract_clean_text(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read().lower()  # Перетворюємо текст у нижній регістр

            # Видаляємо всі символи пунктуації окрім пробілу
            content = re.sub(r'[^а-яґєії ]', '', content)
            return content
    except FileNotFoundError:
        print(f"Файл '{file_name}' не знайдено")
        return ''

def calculate_bigram_frequencies(text):
    bigram_frequencies = defaultdict(int)
    total_bigrams = 0

    # Підрахунок відносних частот біграм
    for i in range(len(text) - 1):
        if text[i] != ' ' and text[i + 1] != ' ':
            bigram = text[i:i + 2]
            bigram_frequencies[bigram] += 1
            total_bigrams += 1

    # Конвертуємо кількості у відносні частоти
    for bigram in bigram_frequencies:
        bigram_frequencies[bigram] /= total_bigrams

    return bigram_frequencies

def main():
    files_to_analyze = ['shyfr.txt']  # Список файлів для аналізу

    for file_name in files_to_analyze:
        text = extract_clean_text(file_name)
        if text:
            print(f"Аналізуємо файл '{file_name}':")
            frequencies = calculate_bigram_frequencies(text)

            # Виводимо результати (приклад)
            sorted_frequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
            for bigram, frequency in sorted_frequencies[:30]:  # Перші 30 найбільш ймовірних біграм
                print(f"{bigram};{frequency:.6f}")

            # Можна також створити таблицю частот або відобразити іншу інформацію про біграми

if __name__ == "__main__":
    main()
