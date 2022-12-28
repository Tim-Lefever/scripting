# Write your solution in this file
not_in_dict = set()
words_in_text = set()
words_in_dict = set()

with open('text.txt', encoding='utf-8') as g:
    for line in g:
        for word in line.split():
            word = word.replace('\n', '').replace('.', '').replace(',', '')
            words_in_text.add(word)

with open('dictionary.txt', encoding='utf-8') as f:
    for line in f:
        word = line.replace('\n', '')
        words_in_dict.add(word)

'''get all words in text.txt that are not in dictionary.txt'''
not_in_dict = words_in_text - words_in_dict

'''get sorted list of all words in text.txt that are not in dictionary.txt'''
not_in_dict = sorted(not_in_dict)

'''write to output.txt'''
with open('output.txt', 'w', encoding='utf-8') as out:
    for word in not_in_dict:
        out.write(word + '\n')