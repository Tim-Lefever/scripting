# Write your solution in this file
'''open words.txt'''
import re

all_words = set()
with open('words.txt', encoding='utf-8') as f:
    for word in f:
        word = word.replace('\n', '')
        all_words.add(word)

removed = set()
for word in all_words:
    remove = False
    if not re.fullmatch(r'....x...', word):
        remove = True
    
    if 'a' not in word or 'b' not in word or 'c' not in word or 'd' not in word:
        remove = True

    '''a cant be at first position'''
    if word[0] == 'a':
        remove = True
        
    '''b cant be at second position'''
    if word[1] == 'b':
        remove = True
    
    '''c cant be at third position'''
    if word[2] == 'c':
        remove = True
    
    '''d cant be at fourth position'''
    if word[3] == 'd':
        remove = True

    if 'e' in word or 'f' in word or 'g' in word or 'h' in word:
        remove = True

    '''only one x'''
    if word.count('x') != 1:
        remove = True

    if remove:
        removed.add(word)

all_words = all_words - removed

print(all_words)
'''sort all_words'''
all_words = sorted(all_words)

'''print to output.txt'''
with open('output.txt', 'w', encoding='utf-8') as out:
    for word in all_words:
        out.write(word + '\n')