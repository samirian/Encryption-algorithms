from monoalphapetic import *


if __name__ == "__main__":
    input_file_text = get_lines_from_file('text.txt')
    key = generate_key()
    print('key:')
    print(key)
    cipher_file_text = encrypt(input_file_text)
    write_lines_to_file('cipher.txt', cipher_file_text)
    write_lines_to_file('de-cipher.txt', decrypt(cipher_file_text))
    key_dash = mapping(cipher_file_text)
    print('predicted key:')
    print(key_dash)
    print(decrypt(cipher_file_text, key_dash))
    answer = 'y'
    while answer == 'y' or answer == 'Y':
        print("key similarity:")
        print(calculate_similarity(key, key_dash))
        print(calculate_similarity(input_file_text,decrypt(cipher_file_text, key_dash)))
        answer =  input('can you handle manual? [y/n]\n')
        if answer == 'y' or answer == 'Y':
            line = input('enter a replacement, example : a b\n')
            argments = line.split(' ')
            print('old key:')
            print(key_dash)
            a = alphapet.index(argments[0])
            b = alphapet.index(argments[1])
            temp = key_dash[a]
            key_dash[a] = key_dash[b]
            key_dash[b] = temp
            print('new key:')
            print(key_dash)
            print(decrypt(cipher_file_text, key_dash))