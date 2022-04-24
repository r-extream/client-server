some_words = ['class', 'function', 'method']

for item in some_words:
    curr = eval(f"b'{item}'")
    print(f'Item: {curr} type: {type(curr)} length in bytes {len(curr)}')
