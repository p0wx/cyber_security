
import re
import pandas as pd
import numpy as np
import time


start_time = time.time()

# шифровка текста
def code(text):
	code_text = ''

	for i, j in enumerate(text):
		if j in dict_alphabet:
			code_text += dict_alphabet[j]
		else:
			code_text += ' '

	return code_text



key_word = list('федя') 

#clean_ex = re.compile('[^а-яА-Я ]')

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщьъыэюя'							# обычный алфавит

code_alphabet = key_word + [i for i in alphabet if i not in key_word]		# шифрованный алфавит

dict_alphabet = dict(zip(list(alphabet), code_alphabet)) 					# словарь алфавит : шифрованный алфавит

text = ''

with open('war_peace_clean.txt', 'r', encoding='utf-8') as f:			
	text = f.read()														# обычный текст



code_text = code(text)													# зашифрованный текст



# частота букв
letters = pd.DataFrame([ [i, text.count(i), code_text.count(i), dict_alphabet[i], code_text.count(dict_alphabet[i])]  for i in alphabet], columns = ['letter', 'text', 'code_text', ' code_letter', 'code_text'])

print('\n\nЧАСТОТА БУКВ\n\n')
print(letters)


# биграммы
bigrams = pd.DataFrame( [[i+j, text.count(i+j), code_text.count(i+j)]  for j in alphabet for i in alphabet], columns = ['bigram', 'text', 'code_text'])

print('\n\n ТОП 5 БИГРАМ В ТЕКСТЕ\n\n')
print(bigrams.sort_values('text', ascending=False).head().to_string(index=False))


print('\n\n ТОП 5 БИГРАМ В ЗАШИФРОВАННОМ ТЕКСТЕ\n\n')
print(bigrams.sort_values('code_text', ascending=False).head().to_string(index=False))



print("\n\n\n--- %s seconds ---" % (time.time() - start_time))





