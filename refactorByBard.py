class CaesarCipher:

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
