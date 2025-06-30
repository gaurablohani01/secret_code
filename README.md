# 🔐 Text Encoder/Decoder

This Python program encodes and decodes words using a simple text obfuscation technique. It's useful for fun transformations or basic word scrambling.

## 📌 Features

- **Encoder:**
  - If the word has 3 or more letters:
    - Moves the first letter to the end
    - Adds 3 random characters at the beginning and 3 at the end
  - If the word has less than 3 letters:
    - Reverses the word

- **Decoder:**
  - If the word has 3 or more letters:
    - Removes 3 characters from the start and end
    - Moves the last letter of the result to the front
  - If the word has less than 3 letters:
    - Reverses the word

## ⚙️ How to Use

1. Run the script in a Python environment.
2. Choose an option from the menu:
    ```
    1. Encoder
    2. Decoder
    ```
3. Input the text when prompted.


