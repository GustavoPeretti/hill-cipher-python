print('Welcome to Hill Cipher encryptor and decryptor')

mode = int(input('Insert:\n(1) for encrypting\n(2) for decrypting\n'))

alphabet = 'abcdefghijklmnopqrstuvwxyz'

alphabet_table = {key: value for key, value in zip(alphabet, range(1, 26))}
alphabet_table['z'] = 0

reversed_alphabet_table = {key: value for key, value in zip(range(1, 26), alphabet)}
reversed_alphabet_table[0] = 'z'

message = input('Insert the message you want to {}: '.format('encrypt' if mode == 1 else 'decrypt')).lower()
print()

key = [[1, 1], [1, 1]]
while not key[0][0] * key[1][1] - key[0][1] * key[1][0] == 1:
    print('Insert the four numbers of 2×2 matrix key: ')
    key = [list((int(input(': ')), int(input(': ')))), list((int(input(': ')), int(input(': '))))]
i_key = [[key[1][1], -key[0][1]], [-key[1][0], key[0][0]]]


def split_list(iter_list, n):
    for i in range(0, len(iter_list), n):
        yield iter_list[i: i + n]


def module_number(number, n):
    return number % n


numeric_message = [alphabet_table[c] for c in message]
numbers = list(split_list(numeric_message, 2))


if mode == 1:
    encrypted_nums = [[n[0] * key[0][0] + n[1] * key[0][1], n[0] * key[1][0] + n[1] * key[1][1]] for n in numbers]
    module_numbers = [module_number(encrypted_nums[l][n], 26) \
                      for l in range(len(encrypted_nums)) for n in range(len(encrypted_nums[l]))]

if mode == 2:
    decrypted_nums = [[n[0] * i_key[0][0] + n[1] * i_key[0][1], n[0] * i_key[1][0] + n[1] * i_key[1][1]] for n in numbers]
    module_numbers = [module_number(decrypted_nums[l][n], 26) \
                      for l in range(len(decrypted_nums)) for n in range(len(decrypted_nums[l]))]

output = ''.join(reversed_alphabet_table[n] for n in module_numbers)

print('\nOutput:', output)
