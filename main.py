import os
import re
from bs4 import BeautifulSoup
from nltk.corpus import stopwords

# Initialize the set of stop words
stop_words = set(stopwords.words('english'))


def clean_text(text):
    # Convert text to lowercase
    text = text.lower()

    # Remove HTML tags
    text = BeautifulSoup(text, "html.parser").get_text()

    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)

    # Remove unwanted special characters (keep necessary punctuation: ?, !, ., ,)
    text = re.sub(r'[^a-z0-9\s?!.,]', '', text)  # Allow lowercase letters, digits, and specified punctuation

    # Normalize spaces and remove extra white spaces
    text = re.sub(r'\s+', ' ', text).strip()

    # Remove stop words
    text = ' '.join(word for word in text.split() if word not in stop_words)

    return text


def clean_files_in_folder(input_folder_path, output_folder_path):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder_path, exist_ok=True)

    for filename in os.listdir(input_folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(input_folder_path, filename)
            try:
                # Read the file with UTF-8 encoding
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                    content = file.read()

                # Clean the text
                cleaned_content = clean_text(content)

                # Write the cleaned content to a new file in the output folder
                cleaned_file_path = os.path.join(output_folder_path, filename)
                with open(cleaned_file_path, 'w', encoding='utf-8') as file:
                    file.write(cleaned_content)

                print(f"Cleaned and saved: {filename} to {output_folder_path}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")


def main():
    input_folder_path = 'clean_folder_code_mixed'  # Replace with your input folder path
    output_folder_path = 'clean_folder_code_mixed'  # Replace with your output folder path
    clean_files_in_folder(input_folder_path, output_folder_path)


if __name__ == "__main__":
    main()