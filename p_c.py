

with open('corpus.txt', 'r', encoding='utf-8') as f:
    data = f.read()

english_only = ''.join(x for x in data if ord(x) < 256)

print(english_only)

with open('corpus2.txt', 'w', encoding='utf-8') as f:
    f.write(english_only)