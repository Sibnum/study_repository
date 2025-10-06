class CipherMaster:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def cipher(self, original_text, shift):
        result = []
        for letter in original_text:
            if letter.lower() in self.alphabet:
                original_symbol_index = self.alphabet.find(letter.lower())
                cipher_symbol_index = (original_symbol_index + shift) % 33
                result.append(self.alphabet[cipher_symbol_index])
            else:
                result.append(letter)
        return ''.join(result)

    def decipher(self, cipher_text, shift):
        result = []
        for letter in cipher_text:
            if letter.lower() in self.alphabet:
                cipher_text = self.alphabet.find(letter.lower())
                original_symbol_index = (cipher_text - shift) % 33
                result.append(self.alphabet[original_symbol_index])
            else:
                result.append(letter)
        return ''.join(result)


cipher_master = CipherMaster()
print(cipher_master.cipher(
    original_text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2
))
print(cipher_master.decipher(
    cipher_text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3
))
