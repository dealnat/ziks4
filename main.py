from collections import defaultdict

def calculate_letter_frequencies(file_list):
    # Створюємо словник для збереження частот кожної літери
    letter_frequencies = defaultdict(int)
    ukrainian_alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"

    # Проходимо по кожному файлу у списку
    for file_name in file_list:
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                # Читаємо вміст файлу та обробляємо його
                content = file.read().lower()  # Перетворюємо текст у нижній регістр

                # Видаляємо всі символи пунктуації окрім пробілу
                content = ''.join(char for char in content if char in ukrainian_alphabet or char == ' ')

                # Рахуємо частоти літер
                for char in content:
                    if char != ' ':
                        letter_frequencies[char] += 1

        except FileNotFoundError:
            print(f"Файл '{file_name}' не знайдено")

    # Обчислюємо загальну кількість літер у тексті
    total_letters = sum(letter_frequencies.values())

    # Виводимо результати
    print("Частоти літер українського алфавіту:")
    for letter in ukrainian_alphabet:
        frequency = letter_frequencies[letter]
        percentage = (frequency / total_letters) * 100 if total_letters > 0 else 0
        #print(f"Літера '{letter}': {frequency} ({percentage:.2f}%)")
        print(f"{letter};{percentage/100}")

files_to_analyze = ['shyfr.txt']  
calculate_letter_frequencies(files_to_analyze)
