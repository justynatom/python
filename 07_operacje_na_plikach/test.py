filename = 'tekst.txt'

with open(filename, 'r', encoding="utf-8") as f:
  content = f.read()
print(content)

items = ['tent', 'money', 'bag']
with open('save.txt', 'w') as f:
    f.write('\n'.join(items))
