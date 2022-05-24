# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])
# ???
print('')


# Вывести количество букв "а" в слове
word = 'Архангельск'
word1 = word.lower()
print(word1.count('а'))
# ???
print('')

# Вывести количество гласных букв в слове
word = 'Архангельск'
vowel = ['а', 'е', 'ё' ,'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
n_vowel = 0
for letter in word.lower():
    if letter in vowel:
        n_vowel +=1
    else:
        pass
print(n_vowel)

print('')
# ???


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
sen = sentence.split()
n_words = 0
for word in sen:
    n_words += 1
print(n_words)

print('')
# ???


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
sen = sentence.split()
for word in sen:
    print(word[0])

print('')
# ???


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.replace(' ', '')) / len(sentence.split()))

# ???