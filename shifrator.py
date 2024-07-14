class CipherMaster:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def cipher(self, original_text, shift):
        # Метод должен возвращать зашифрованный текст
        # с учетом переданного смещения shift.
        result = ''
        for word in original_text:
            if word.lower() in self.alphabet:
                word_index = (self.alphabet.index(word.lower()) +
                              shift) % len(self.alphabet)
                result += self.alphabet[word_index]
            else:
                result += word
        return result

    def decipher(self, cipher_text, shift):
        # Метод должен возвращать исходный текст
        # с учётом переданного смещения shift.
        result = ''
        for word in cipher_text:    
            if word.lower() in self.alphabet:
                word_index = (self.alphabet.index(word.lower()) -
                              shift) % len(self.alphabet)
                result += self.alphabet[word_index]
            else:
                result += word
        return result


cipher_master = CipherMaster()
print(cipher_master.cipher(
    original_text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2
))
print(cipher_master.decipher(
    cipher_text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3
))
