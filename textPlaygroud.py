from refactorByBard import CaesarCipher

textToEncript='Olá! Meu Nome é Bruno'
textToDecript=r"Urg'&Sk{&Tusk&k&Hx{tu"

teste=CaesarCipher(6)
print(teste.encrypt(textToEncript))
print(teste.decrypt(teste.encrypt(textToEncript)))