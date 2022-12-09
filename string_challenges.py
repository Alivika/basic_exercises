# # Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])

# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'

def countVowels(word):
   vowels = {'а', 'е', 'ё', 'и', 'о', 'у', 'э', 'ю', 'я'}
   count = 0
   for letter in word.lower():
      if letter in vowels:
         count += 1
   print(count)

countVowels(word)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split(' ')))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for word in sentence.split(' '):
   print(word[0])



# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
def avg_word(sentence):
   avg_len = 0
   words_sum = 0
   for word in sentence.split(' '):
      words_sum += len(word)
      avg_len = words_sum / len(sentence.split(' '))
   print(avg_len)

avg_word(sentence)