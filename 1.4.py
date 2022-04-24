some_words = ['разработка', 'администрирование', 'protocol', 'standard']
byte_some_words = []

print('слова для преобразования:', *some_words)

print('преобразование в байты:')
for item in some_words:
    byte = item.encode('utf-8')
    print(byte)
    byte_some_words.append(byte)

print('обратное преобразование:')

for item in byte_some_words:
    print(item.decode('utf-8'))
