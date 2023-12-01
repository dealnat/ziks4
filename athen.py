import re
# Функція для знаходження оберненого числа (модульна оберненість)
def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None
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
# Функція для шифрування тексту за афінним шифром українським алфавітом
def encrypt(text, key):
    a, b = key
    encrypted_text = ""
    alphabet = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
    for char in text:
        if char.isalpha() and char in alphabet:
            char_index = alphabet.index(char)
            encrypted_index = (a * char_index + b) % len(alphabet)
            encrypted_text += alphabet[encrypted_index]
        else:
            encrypted_text += char
    return encrypted_text

# Функція для дешифрування тексту за афінним шифром українським алфавітом
def decrypt(text, key):
    a, b = key
    decrypted_text = ""
    alphabet = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
    a_inverse = mod_inverse(a, len(alphabet))
    if a_inverse is None:
        return "Неможливо знайти обернене число для дешифрування"
    for char in text:
        if char.isalpha() and char in alphabet:
            char_index = alphabet.index(char)
            decrypted_index = (a_inverse * (char_index - b)) % len(alphabet)
            decrypted_text += alphabet[decrypted_index]
        else:
            decrypted_text += char
    return decrypted_text

key = (7, 3)  # Встановлюємо ключ шифрування (a, b)
text = extract_clean_text("afin.txt")
# Шифруємо текст
#encrypted_text = encrypt(text, key)
#print("Зашифрований текст:", encrypted_text)

#decrypted_text = decrypt(encrypted_text, key)
#print("Розшифрований текст:", decrypted_text)