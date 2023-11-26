class CaesarCipher:

#Bards comments:

#This refactored code adheres to the principles of Clean Code and OOP by:

#Encapsulating data and behavior: The CaesarCipher class encapsulates the data (seed number) and behavior (encrypt, decrypt) related to the Caesar cipher.

#Using descriptive names: The class name CaesarCipher clearly indicates the purpose of the class, and the method names encrypt and decrypt are self-explanatory.

#Using appropriate data structures: The class uses a dictionary to store the accent removal mapping, which is an efficient way to handle string replacements.

#Handling errors gracefully: The _validate_text method checks the input text for validity and raises an exception if it's not a string.

#Using consistent indentation and spacing: The code is indented consistently and uses appropriate spacing to improve readability.

#Separating concerns: The code separates the text cleaning, encryption, and decryption logic into separate methods, making the code more modular and maintainable.



    def __init__(self, seed_number):
        self._seed_number = seed_number

    def encrypt(self, text):
        self._validate_text(text)
        cleaned_text = self._clean_text(text)
        encrypted_text = self._encrypt_text(cleaned_text)
        return encrypted_text

    def decrypt(self, text):
        self._validate_text(text)
        decrypted_text = self._decrypt_text(text)
        return decrypted_text

    def _validate_text(self, text):
        if not isinstance(text, str):
            raise TypeError("Input text must be a string")

    def _clean_text(self, text):
        accent_removal_map = {
            "ÁÀÃÂÇáàãâç": "AAAACaaaac",
            "ÉÊéêÍíÑÓÔÕñóôõ": "EEeeIiNOOOnoooUUuu",
        }

        for accent_chars, replacement_chars in accent_removal_map.items():
            for accent_char, replacement_char in zip(accent_chars, replacement_chars):
                text = text.replace(accent_char, replacement_char)

        return text

    def _encrypt_text(self, text):
        encrypted_text = ""

        for char in text:
            try:
                ascii_code = ord(char) + self._seed_number
                if ascii_code > 127:
                    ascii_code = ascii_code % 127

                encrypted_char = chr(ascii_code)
            except (ValueError, TypeError):
                encrypted_char = char

            encrypted_text += encrypted_char

        return encrypted_text

    def _decrypt_text(self, text):
        decrypted_text = ""

        for char in text:
            try:
                ascii_code = ord(char) - self._seed_number
                if ascii_code < 0:
                    ascii_code = ascii_code % 127 + 127

                decrypted_char = chr(ascii_code)
            except (ValueError, TypeError):
                decrypted_char = char

            decrypted_text += decrypted_char

        return decrypted_text
