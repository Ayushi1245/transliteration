import os
import random

def transliterate(text):
    mapping = {
        # Vowels (Standalone)
        'अ': 'a', 'आ': 'aa', 'इ': 'i', 'ई': 'i', 'उ': 'u', 'ऊ': 'u',
        'ऋ': 'ri', 'ए': 'e', 'ऐ': 'ai', 'ओ': 'o', 'औ': 'au',

        # Consonants (Adding "a" at the end)
        'क': 'ka', 'ख': 'kha', 'ग': 'ga', 'घ': 'gha', 'च': 'cha', 'छ': 'chha','ड़': 'dh','क़': 'q','फ़':'f','ड़': 'd',
        'ज': 'ja', 'झ': 'jha', 'ट': 'ta', 'ठ': 'tha', 'ड': 'da', 'ढ': 'dha','ढ़': 'rha', 'फ़': 'fa','ग़': 'gha', 'ज़': 'za',
        'त': 'ta', 'थ': 'tha', 'द': 'da', 'ध': 'dha', 'न': 'na', 'प': 'pa','क़': 'qa', 'ख़': 'kha','ढ़':'rha','ज़':'za',
        'फ': 'pha', 'ब': 'ba', 'भ': 'bha', 'म': 'ma', 'य': 'ya', 'र': 'ra',
        'ल': 'la', 'व': 'va', 'श': 'sha', 'ष': 'sha', 'स': 'sa', 'ह': 'ha',
        'ण': 'na','ख़':'kha',

        # Nukta-based Characters
         'क़': 'qa', 'ख़': 'kha', 'ग़': 'gha', 'ज़': 'za', 'ड़': 'ṛa', 'ढ़': 'ṛha', 'फ़': 'fa',

        # Special Ligatures
        'क्ष': 'ksha', 'त्र': 'tra', 'ज्ञ': 'gya', 'श्र': 'shra',

        # Matras (Vowel Modifiers)
        'ा': 'aa', 'ि': 'i', 'ी': 'i', 'ु': 'u', 'ू': 'oo',
        'े': 'e', 'ै': 'ai', 'ो': 'o', 'ौ': 'au',

        # Special Characters
        'ं': 'n', 'ँ': 'n', 'ः': 'h', '्': ''  # Halant removes inherent "a"
    }

    transliterated_text = ""
    i = 0
    while i < len(text):
        char = text[i]

        # Handle Special Ligatures First
        if i < len(text) - 1 and (char + text[i + 1]) in mapping:
            transliterated_text += mapping[char + text[i + 1]]
            i += 2
            continue

        # Handle Matras
        if char in mapping:
            if char in "ािीुूेैोौंःँ":
                transliterated_text = transliterated_text.rstrip("a")  # Remove inherent "a"
            transliterated_text += mapping[char]

        # Handle Halant (्) for Half-Letters
        elif char == '्':
            transliterated_text = transliterated_text.rstrip("a")  # Remove last "a" for half-letters

        else:
            transliterated_text += char  # Keep unknown characters unchanged

        i += 1

    # Remove extra "a" at the end of each word
    words = transliterated_text.split()
    words = [word[:-1] if word.endswith("a") else word for word in words]
    transliterated_text = " ".join(words)

    # Introduce random 'n' to 'm' errors (10% chance)
    transliterated_text = "".join("m" if ch == "n" and random.random() < 0.1 else ch for ch in transliterated_text)

    return transliterated_text

def transliterate_folder(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):  # Process only text files
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            with open(input_path, "r", encoding="utf-8") as infile:
                hindi_text = infile.read()

            romanized_text = transliterate(hindi_text)

            with open(output_path, "w", encoding="utf-8") as outfile:
                outfile.write(romanized_text)

    print("✅ Transliteration completed for all files in the folder!")


# Example Usage
input_folder = "input_folder"
output_folder = "transliterated_texts_nuktas_cm"
transliterate_folder(input_folder, output_folder)