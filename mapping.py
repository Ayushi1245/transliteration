import os


def transliterate(text):
    mapping = {
        # Vowels
        'अ': 'a', 'आ': 'aa', 'इ': 'i', 'ई': 'ii', 'उ': 'u', 'ऊ': 'oo',
        'ऋ': 'ri', 'ए': 'e', 'ऐ': 'ai', 'ओ': 'o', 'औ': 'au',

        # Consonants
        'क': 'k', 'ख': 'kh', 'ग': 'g', 'घ': 'gh', 'च': 'ch', 'छ': 'chh',
        'ज': 'j', 'झ': 'jh', 'ट': 't', 'ठ': 'th', 'ड': 'd', 'ढ': 'dh',
        'त': 't', 'थ': 'th', 'द': 'd', 'ध': 'dh', 'न': 'n', 'प': 'p',
        'फ': 'ph', 'ब': 'b', 'भ': 'bh', 'म': 'm', 'य': 'y', 'र': 'r',
        'ल': 'l', 'व': 'v', 'श': 'sh', 'ष': 'sh', 'स': 's', 'ह': 'h',

        # Special Ligatures
        'क्ष': 'ksh', 'त्र': 'tra', 'ज्ञ': 'gya', 'श्र': 'shra',

        # Matras (Vowel Modifiers)
        'ा': 'aa', 'ि': 'i', 'ी': 'ii', 'ु': 'u', 'ू': 'oo',
        'े': 'e', 'ै': 'ai', 'ो': 'o', 'ौ': 'au',

        # Special Characters
        'ं': 'm', 'ँ': 'm~', 'ः': 'h', '्': ''  # Halant removes inherent "a"
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

        # Handle Matras Modifying Previous Consonant
        if char in mapping:
            if char in "ािीुूेैोौंःँ":
                transliterated_text = transliterated_text.rstrip("a")  # Remove inherent "a"
            transliterated_text += mapping[char]

        # Handle Halant (्) for Half-Letters
        elif char == '्':
            transliterated_text = transliterated_text.rstrip("a")  # Remove last "a"

        else:
            transliterated_text += char  # Keep unknown characters unchanged

        i += 1

    return transliterated_text


def transliterate_folder(input_folder, output_folder):
    """Transliterates all text files in a folder and saves them in the output folder."""

    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Process all `.txt` files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            # Read the Hindi text file
            with open(input_path, "r", encoding="utf-8") as file:
                hindi_text = file.read()

            # Transliterate the text
            romanized_text = transliterate(hindi_text)

            # Save the transliterated text
            with open(output_path, "w", encoding="utf-8") as file:
                file.write(romanized_text)

            print(f"Processed: {filename}")


# Example Usage
input_folder = "poetry_datasets"  # Folder with Hindi text files
output_folder = "transliterated_texts"  # Folder for transliterated files
transliterate_folder(input_folder, output_folder)
print("✅ Transliteration complete!")