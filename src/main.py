import pandas as pd

english_alphabet = "abcdefghijklmnopqrstuvwxyz"
upper_english_alphabet = english_alphabet.upper()
russian_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
upper_russian_alphabet = russian_alphabet.upper()
index_to_english_char = dict(enumerate(english_alphabet))
english_char_to_index = dict({(c, i) for i, c in index_to_english_char.items()})
index_to_big_english_char = dict(enumerate(english_alphabet.upper()))
big_english_char_to_index = dict({(c, i) for i, c in index_to_big_english_char.items()})
index_to_russian_char = dict(enumerate(russian_alphabet))
russian_char_to_index = dict({(c, i) for i, c in index_to_russian_char.items()})
index_to_big_russian_char = dict(enumerate(russian_alphabet.upper()))
big_russian_char_to_index = dict({(c, i) for i, c in index_to_big_russian_char.items()})
english_characters = set(english_alphabet)
upper_english_characters = set(upper_english_alphabet)
russian_characters = set(russian_alphabet)
upper_russian_characters = set(upper_russian_alphabet)
max_decode_number = max(len(english_alphabet), len(russian_alphabet))
input_file_name = "data/input.csv"
output_file_name = "data/result.csv"

def main():
    input_dataset = pd.read_csv(input_file_name)
    keys = []
    decoded_emails = []
    decoded_addresses = []
    for row in input_dataset.itertuples():
        email, address = row.email, row.address
        for key in range(max_decode_number):
            decoded_email = decode(email, key)
            decoded_address = decode(address, key)
            if "кв." in decoded_address and "д." in decoded_address:
                return
        keys.append(key)
        decoded_emails.append(decoded_email)
        decoded_addresses.append(decoded_address)
    pd.DataFrame({"email" : decoded_emails, "address" : decoded_addresses, "key" : keys}).to_csv(output_file_name)

def decode_char(char: str, key: int) -> str:
    if char in english_characters:
        return translate_with_dictionaries(char, key, index_to_english_char, english_char_to_index)
    if char in russian_characters:
        return translate_with_dictionaries(char, key, index_to_russian_char, russian_char_to_index)
    if char in upper_english_characters:
        return translate_with_dictionaries(char, key, index_to_big_english_char, big_english_char_to_index)
    if char in upper_russian_characters:
        return translate_with_dictionaries(char, key, index_to_big_russian_char, big_russian_char_to_index)
    return char

def translate_with_dictionaries(char, key, index_to_char, char_to_index) -> str:
    return index_to_char[(char_to_index[char] - key) % len(index_to_char)]

def decode(string: str, key: int):
    decoded : str = ""
    for char in string:
        decoded += decode_char(char, key)
    return decoded

if __name__ == "__main__":
    main()
