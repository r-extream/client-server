from chardet import detect

FILE = 'test_file.txt'


def get_file_encoding(file):
    with open(file, 'rb') as file_in:
        return detect(file_in.read())['encoding']


with open(FILE, 'w') as file_out:
    for line in ['сетевое программирование', 'сокет', 'декоратор']:
        file_out.write(f'{line}\n')

encoding = get_file_encoding(FILE)
print(encoding)

with open(FILE, 'r', encoding=encoding) as file_in:
    print(file_in.read())
