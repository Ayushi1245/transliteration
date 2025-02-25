import os
from indic_transliteration import sanscript

def transliterate_file(input_file_path, output_file_path):
    # Read the content of the input file
    with open(input_file_path, 'r', encoding='utf-8') as input_file:
        devanagari_text = input_file.read()

    # Transliterate the text from Devanagari to Roman script
    roman_text = sanscript.transliterate(devanagari_text, sanscript.DEVANAGARI, sanscript.HK)  # Using HK (Harvard-Kyoto) scheme

    # Write the transliterated text to the output file
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(roman_text)

    print(f"Transliteration complete for {input_file_path}. Output written to {output_file_path}")

def transliterate_folder(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.txt'):  # Process only text files
            input_file_path = os.path.join(input_folder, filename)
            output_file_path = os.path.join(output_folder, f"transliterated_{filename}")

            transliterate_file(input_file_path, output_file_path)

# Example usage
input_folder = 'Hindi-Hinglish'  # Replace with your input folder path
output_folder = 'output_folder_code_mixed'  # Replace with your desired output folder path
transliterate_folder(input_folder, output_folder)