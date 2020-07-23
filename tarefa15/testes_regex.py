import re



text_to_search = '''
abcdefghijklmnopqrstuvwxyz 
ABCDEFGHIJKLMOPQRSTUVWXYZ

''' 


sentence = 'Comece com uma frase e depois termine'

pattern = re.compile(r'abc')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

