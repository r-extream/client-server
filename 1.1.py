some_words = ['разработка', 'сокет', 'декоратор']

for item in some_words:
    print(item, type(item))

print('\n\nUnicode values:')

unicode_some_words = [
    '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
    '\u0441\u043e\u043a\u0435\u0442',
    '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440',
]

for item in unicode_some_words:
    print(item, type(item))
