from helpers import *


class PolySubstitution:
    def PolySubstitution(self):
        self.keys = None

    def get_keys(self):
        self.keys = input('enter the key(s)').split(' ')
        for i in range(len(self.keys)):
            self.keys[i] = int(self.keys[i])
        return self.keys

    def encrypt(self, lines, keys):
        cipher_lines = []
        for line in lines:
            line = line.lower()
            charachters = list(line)
            key_counter = 0
            for charachter_index in range(len(charachters)):
                key = keys[key_counter%len(keys)]
                charachter = charachters[charachter_index]
                if charachter in alphapet:
                    charachters[charachter_index] = alphapet[(alphapet.index(charachter) + key)%ALPHAPET_LENGTH]
                key_counter += 1
            cipher_line = "".join(charachters)
            cipher_lines.append(cipher_line)
        return cipher_lines

    def decrypt(self, lines, keys):
        cipher_lines = []
        for line in lines:
            line = line.lower()
            charachters = list(line)
            key_counter = 0
            for charachter_index in range(len(charachters)):
                key = keys[key_counter%len(keys)]
                charachter = charachters[charachter_index]
                if charachter in alphapet:
                    charachters[charachter_index] = alphapet[(alphapet.index(charachter) - key)%ALPHAPET_LENGTH]
                key_counter += 1
            cipher_line = "".join(charachters)
            cipher_lines.append(cipher_line)
        return cipher_lines

    def solve(self, encrypted_lines):
        #check the letters frequency every certaing interval and compare to the normal frequency as numbers only
        temp_encrypted_lines = []
        #assume length
        minimum = 1000
        minimum_length = 0
        for cipher_length in range(25):
            for line in encrypted_lines:
                line = line.lower()
                charachters = list(line)
                new_charachters = []
                if cipher_length != 0:
                    for i in range(len(charachters)):
                        if i%cipher_length == 0:
                            new_charachters.append(charachters[i])
                else:
                    new_charachters = charachters
                temp_encrypted_lines.append("".join(new_charachters))
            #calculate statistics
            cipher_statistics = calculate_statistics(temp_encrypted_lines)
            variance = calculate_variance(cipher_statistics, statistics)
            if minimum > variance:
                minimum = variance
                minimum_length = cipher_length
        print("predicted length is:")
        print(minimum_length)
        #solve as ceaser
        pass

if __name__ == "__main__":
    polysubstitution = PolySubstitution()
    try:
        keys = polysubstitution.get_keys()
    except Exception:
        print('error in key, would you like to re-enter key?(y/n)')
    print(keys)
    input_file_text = get_lines_from_file('text.txt')
    cipher_file_text = polysubstitution.encrypt(input_file_text, keys)
    write_lines_to_file('cipher(polysubstitution).txt', cipher_file_text)
    write_lines_to_file('de-cipher(polysubstitution).txt', polysubstitution.decrypt(cipher_file_text, keys))
    #polysubstitution.solve(cipher_file_text)
