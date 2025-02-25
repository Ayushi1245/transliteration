import os
from indic_transliteration.sanscript import transliterate, DEVANAGARI, ITRANS

# Input & Output folders
input_folder = "poetry_datasets"
output_folder = "romanized_files"

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    file_path = os.path.join(input_folder, filename)

    if os.path.isfile(file_path) and filename.endswith(".txt"):  # Check if it's a text file
        output_path = os.path.join(output_folder, filename)

        # ✅ Check if the file is actually being read
        with open(file_path, "r", encoding="utf-8") as infile:
            hindi_text = infile.read().strip()

        if not hindi_text:
            print(f"⚠️ WARNING: {filename} is empty! Skipping...")
            continue

        print(f"🔹 Processing: {filename}")
        print(f"📜 Original Text: {hindi_text[:100]}...")  # Show first 100 chars

        # ✅ Transliterate Devanagari to Roman
        roman_text = transliterate(hindi_text, DEVANAGARI, ITRANS).lower()

        if not roman_text.strip():
            print(f"⚠️ WARNING: No output for {filename}! Check transliteration function.")
            continue

        # ✅ Check if the output is correct
        print(f"📝 Romanized Text: {roman_text[:100]}...")  # Show first 100 chars

        # ✅ Save transliterated text
        with open(output_path, "w", encoding="utf-8") as outfile:
            outfile.write(roman_text)

        print(f"✅ Transliterated: {filename} → {output_path}\n")

print("🎉 Batch transliteration complete!")