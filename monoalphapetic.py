import random
from helpers import *


key = ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-']

def generate_key():
    i = 0
    while i < ALPHAPET_LENGTH:
        index = random.randint(0,25)
        if alphapet[index] not in key:
            key[i] = alphapet[index]
            i += 1
    return key

class MonoAlphapetic:
    def __init__(self):
        self.sample_plaintext_filename = 'sample-plaintext.txt'

    def encrypt(self, input_lines, key):
        cipher_lines = []
        for line in input_lines:
            cipher_line = line.lower()
            charachters = list(cipher_line)
            for charachter_index in range(len(charachters)):
                charachter = charachters[charachter_index]
                if charachter in alphapet:
                    charachters[charachter_index] = key[alphapet.index(charachter)]
        
            cipher_line = "".join(charachters)
            cipher_lines.append(cipher_line)
        return cipher_lines

    def decrypt(self, input_lines, key):
        new_key = []
        for i in range(ALPHAPET_LENGTH):
            new_key.append(alphapet[key.index(alphapet[i])])
        output_lines = self.encrypt(input_lines, new_key)
        return output_lines

    def mapping(self, input_file_text):
        text_statistics = calculate_statistics(input_file_text)
        key = ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-']
        print('calculated statistics for the encrypted text:')
        for element in text_statistics:
            print(element)
        #calculating statistic from sample text
        sample_text = get_lines_from_file(self.sample_plaintext_filename)
        sample_text_statistics = calculate_statistics(sample_text)

        print('calculated statistics for the sample text:')
        for element in sample_text_statistics:
            print(element)

        print('general english statistics:')
        print(statistics)
        for element in statistics:
            print(element)
        #mapping the charachters according to statistics (predicting the key)
        for i in range(ALPHAPET_LENGTH):
            max = 0
            max_index = 0
            for j in range(ALPHAPET_LENGTH):
                if text_statistics[j][1] >= max:
                    max = text_statistics[j][1]
                    max_index = j

            key[alphapet.index(sample_text_statistics[i][0])] = text_statistics[max_index][0]
            text_statistics[max_index][1] = -1
        return key

if __name__ == "__main__":
    monoalphapetic = MonoAlphapetic()
    input_text = get_lines_from_file('text.txt')
    key = generate_key()
    print('key:')
    print(key)
    cipher_text = monoalphapetic.encrypt(input_text, key)
    write_lines_to_file('cipher.txt', cipher_text)
    write_lines_to_file('de-cipher.txt', monoalphapetic.decrypt(cipher_text, key))

    predicted_key = monoalphapetic.mapping(cipher_text)
    print('predicted key:')
    print(predicted_key)
    print(monoalphapetic.decrypt(cipher_text, predicted_key))
    answer = 'y'
    while answer == 'y' or answer == 'Y':
        print("key similarity:")
        print(calculate_similarity(key, predicted_key))
        print(calculate_similarity(input_text, monoalphapetic.decrypt(cipher_text, predicted_key)))
        answer =  input('can you handle manual? [y/n]\n')
        if answer == 'y' or answer == 'Y':
            line = input('enter a replacement, example : a b\n')
            argments = line.split(' ')
            print('old key:')
            print(predicted_key)
            a = alphapet.index(argments[0])
            b = alphapet.index(argments[1])
            temp = predicted_key[a]
            predicted_key[a] = predicted_key[b]
            predicted_key[b] = temp
            print('new key:')
            print(predicted_key)
            print(monoalphapetic.decrypt(cipher_text, predicted_key))