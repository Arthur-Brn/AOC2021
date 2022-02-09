def run(list_of_bytes):
    gamma_bin = ''.join([mostPresent(list_of_bytes, i) for i, _ in enumerate(list_of_bytes[0])])
    return int(gamma_bin, 2) * int(''.join([f"{abs(int(n)-1)}" for n in gamma_bin]), 2)


def mostPresent(list_of_bytes, i):
    return '1' if sum([int(byte[i]) for byte in list_of_bytes]) > len(list_of_bytes) / 2 else '0'
