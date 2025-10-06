class CipherMaster:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def process_text(self, text, shift, is_encrypt):
        result = []
        if is_encrypt is True:
            for letter in text:
                if letter.lower() in self.alphabet:
                    original_symbol_index = self.alphabet.find(letter.lower())
                    cipher_symbol_index = (original_symbol_index + shift) % 33
                    result.append(self.alphabet[cipher_symbol_index])
                else:
                    result.append(letter)
            return ''.join(result)
        else:
            for letter in text:
                if letter.lower() in self.alphabet:
                    cipher_text = self.alphabet.find(letter.lower())
                    original_symbol_index = (cipher_text - shift) % 33
                    result.append(self.alphabet[original_symbol_index])
                else:
                    result.append(letter)
            return ''.join(result)


cipher_master = CipherMaster()
print(cipher_master.process_text(
    text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2,
    is_encrypt=True
))
print(cipher_master.process_text(
    text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3,
    is_encrypt=False
))
