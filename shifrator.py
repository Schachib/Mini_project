class CipherMaster:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def process_text(self, text, shift, is_encrypt):
        result = ''
        for word in text:
            if word.lower() in self.alphabet:
                if is_encrypt:
                    word_index = (self.alphabet.index(word.lower()) +
                                  shift) % len(self.alphabet)
                else:
                    word_index = (self.alphabet.index(word.lower()) -
                                  shift) % len(self.alphabet)
                result += self.alphabet[word_index]
            else:
                result += word
        return result


cipher_master = CipherMaster()
print(cipher_master.process_text(
    text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2, is_encrypt=True
))
print(cipher_master.process_text(
    text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3, is_encrypt=False
))
